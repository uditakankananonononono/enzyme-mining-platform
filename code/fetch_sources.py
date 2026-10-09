#!/usr/bin/env python3
"""G0 feasibility + leg-1 retrieval for enzyme-mining-platform (lock-1).

Analysis-selection rule recorded in this script before retrieval
(local commit 865ad2b); data/SOURCES.md was not actually created then:
  C1: MGYS00005625 (all <=12 assembly analyses), MGYS00005970 (all 3),
      MGYS00006544 (44 assemblies -> deterministic subset: analyses sorted
      by accession, every 6th, indices 0,6,...,42 => 8 analyses).
  C2: MGYS00002316, MGYS00005985, MGYS00005997 (1 analysis each).
      MGYS00006000: no predicted-CDS analysis exposed via MGnify v1 API at
      retrieval date -> contributes nothing (recorded, pre-outcome).
  C3: feasibility search; drop if < 5000 protein records (pre-declared).
Resumable: completed downloads (with recorded sha256) are skipped.
"""
import hashlib, json, os, subprocess, sys, time
import gzip
import requests

BASE = "https://www.ebi.ac.uk/metagenomics/api/v1"
ROOT = "/home/sandbox/enzyme-mining-platform"
FASTA_DIR = f"{ROOT}/data/sources/fasta"
STATE = f"{ROOT}/data/sources/g0_counts.json"
os.makedirs(FASTA_DIR, exist_ok=True)

SELECTION = {
    "MGYS00005625": ("C1", "all"),
    "MGYS00005970": ("C1", "all"),
    "MGYS00006544": ("C1", "every6th"),
    "MGYS00002316": ("C2", "all"),
    "MGYS00005985": ("C2", "all"),
    "MGYS00005997": ("C2", "all"),
}

def get(url, **kw):
    timeout = kw.pop("timeout", 120)
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=timeout, **kw)
            if r.status_code in (200, 206):
                return r
        except Exception as e:
            print("retry", attempt, url, e, flush=True)
        time.sleep(5 * (attempt + 1))
    return None

def assembly_analyses(study):
    r = get(f"{BASE}/studies/{study}/analyses?page_size=100")
    if not r:
        raise RuntimeError(f"Cannot verify analyses for {study}")
    return [a for a in r.json().get("data", [])
            if "assembly" in (a["attributes"].get("experiment-type") or "")]

def pick_analyses(study, rule):
    asm = sorted(assembly_analyses(study), key=lambda a: a["id"])
    if rule == "all":
        return asm
    return [a for i, a in enumerate(asm) if i % 6 == 0]

def cds_download(analysis_id):
    r = get(f"{BASE}/analyses/{analysis_id}/downloads")
    if not r:
        raise RuntimeError(f"Cannot verify downloads for {analysis_id}")
    all_cds = []
    split_cds = []
    for d in r.json().get("data", []):
        alias = d["attributes"].get("alias", "")
        if alias.endswith(".faa.gz") and "predicted_cds" in alias:
            all_cds.append((d["links"]["self"], alias))
        elif alias.endswith(("_CDS_annotated.faa.gz", "_CDS_unannotated.faa.gz")):
            split_cds.append((d["links"]["self"], alias))
    return all_cds or sorted(split_cds, key=lambda x: x[1])

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def count_proteins(path):
    # Reading to EOF validates the gzip CRC as well as counting records.
    with gzip.open(path, "rb") as f:
        return sum(line.startswith(b">") for line in f)

def download(url, dest):
    # Atomic completion; resume interrupted bytes only when the server
    # honors Range. No outcome-dependent source/analysis changes.
    partial = dest + ".part"
    if os.path.exists(dest):
        os.replace(dest, partial)
    offset = os.path.getsize(partial) if os.path.exists(partial) else 0
    if offset:
        try:
            n = count_proteins(partial)
        except (EOFError, gzip.BadGzipFile, OSError):
            pass
        else:
            # A foreground timeout can land after the full payload but before
            # CRC/readback. Confirm source length before accepting that file.
            # HEAD stalls on some MGnify objects; a one-byte range provides
            # authoritative total length without re-downloading the payload.
            h = requests.get(url, headers={"Range": "bytes=0-0"}, stream=True, timeout=30)
            h.raise_for_status()
            length = int(h.headers.get("Content-Range", "").rsplit("/", 1)[-1]) if h.status_code == 206 else int(h.headers.get("Content-Length", -1))
            h.close()
            if length == offset:
                os.replace(partial, dest)
                return n
    r = get(url, stream=True, timeout=90,
            headers={"Range": f"bytes={offset}-"} if offset else {})
    if r is None:
        raise RuntimeError(f"download failed: {url}")
    # get() also accepts 206 after the transport fix below.
    with r:
        append = offset and r.status_code == 206
        if append and not r.headers.get("Content-Range", "").startswith(f"bytes {offset}-"):
            raise RuntimeError("Range response offset mismatch")
        with open(partial, "ab" if append else "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)
    n = count_proteins(partial)
    os.replace(partial, dest)
    return n

def main():
    state = json.load(open(STATE)) if os.path.exists(STATE) else {"records": []}
    done = {(r["analysis"], r.get("alias", "")) for r in state["records"] if r.get("complete")}
    legacy_done = {r["analysis"] for r in state["records"] if r.get("complete") and not r.get("alias")}
    only_study = sys.argv[sys.argv.index("--only-study") + 1] if "--only-study" in sys.argv else None
    if only_study and only_study not in SELECTION:
        raise ValueError("Study not in preregistered selection")
    for study, (cls, rule) in SELECTION.items():
        if only_study and study != only_study:
            continue
        for a in pick_analyses(study, rule):
            aid = a["id"]
            if aid in legacy_done:
                continue
            downloads = cds_download(aid)
            if not downloads:
                state["records"].append({"study": study, "class": cls, "analysis": aid,
                                         "complete": False, "reason": "no CDS FASTA download objects"})
                json.dump(state, open(STATE, "w"), indent=1)
                continue
            for url, alias in downloads:
                if (aid, alias) in done:
                    continue
                dest = f"{FASTA_DIR}/{aid}.faa.gz" if "predicted_cds" in alias else f"{FASTA_DIR}/{aid}_{alias}"
                print("downloading", aid, alias, flush=True)
                n_proteins = download(url, dest)
                rec = {"study": study, "class": cls, "analysis": aid, "alias": alias, "url": url,
                       "retrieved_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                       "sha256": sha256_file(dest), "bytes": os.path.getsize(dest),
                       "protein_records": n_proteins, "complete": True}
                state["records"].append(rec)
                json.dump(state, open(STATE, "w"), indent=1)
                print("done", aid, rec["protein_records"], "proteins", rec["bytes"], "bytes", flush=True)
                if "--one" in sys.argv:
                    return
    json.dump(state, open(STATE, "w"), indent=1)
    print("TOTAL", sum(r.get("protein_records", 0) for r in state["records"]), flush=True)

if __name__ == "__main__":
    main()
