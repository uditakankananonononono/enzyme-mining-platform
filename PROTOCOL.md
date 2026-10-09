# PROTOCOL - enzyme-mining-platform (Project 10 of 13)

Status: PREREGISTERED before any real-data compute. Locked by `lock-1` tag.
Date locked: 2026-10-10 (IST). Executor: bioplex13 dedicated executor agent.

## Question
Can a failure-aware, multi-leg computational screen discover genuinely novel
enzyme candidates for pollutant degradation across MORE THAN ONE pollutant class,
from public metagenomic sequence data only, where "novel" is proven by
homolog-exclusion against every experimentally validated enzyme in the class,
and where candidates survive structure-based catalytic adjudication?

## Why this is not a rebuild of existing tools
Prior art (see PRIOR_ART.md) is single-class or single-leg:
PlasticEnz (homology + ML, plastics only), XenoBug (ML classifier, pollutant
enzymes generally), PlasticDB/PAZy (databases, not screens). None of them
(1) work cross-pollutant in one locked protocol, (2) gate novelty by explicit
homolog-exclusion against the validated set, or (3) apply failure-aware
adversarial-family rejection - the exact failure mode that turned the program's
earlier PET screen (doc-1-016) into a neighbouring-esterase list.
The twist: cross-pollutant mining + failure-aware novelty gating + register-aware
structural adjudication, shipped as one reusable tool.

## Pollutant classes (locked)
- C1 PLASTICS: PET hydrolases as the primary leg (reference: PAZy + PlasticDB
  validated sets; positive templates IsPETase 6EQE / FAST-PETase lineage).
- C2 ORGANOPHOSPHATE PESTICIDES: phosphotriesterase class (reference: PTE/OPH
  family, template 1HZY; methyl-parathion/paraoxon degradation literature).
- C3 CHLORINATED SOLVENTS: haloacid dehalogenase class (template 1ZRN / DehI),
  included only if G0 feasibility shows adequate public sequence yield;
  inclusion/exclusion decision and its evidence are recorded verbatim.

## Data sources (public, free)
- MGnify API: predicted proteins from bounded, pollution-relevant public
  studies (plastic-contaminated sites, agricultural soils, activated sludge).
  Study accessions chosen and recorded BEFORE outcome data, in data/STUDIES.md.
- UniProtKB API: validated-enzyme reference sets per class.
- PDB/AlphaFold DB + ESMFold free API: structural templates and candidate folds.
- Every input recorded with URL + retrieval date + sha256 in data/SOURCES.md.

## Pipeline legs (locked order)
1. RETRIEVAL: pyhmmer profile search of study protein sets against
   class-specific HMMs (Pfam family profiles for the catalytic families above).
2. NOVELTY GATE: mmseqs2 easy-search (static binary) of survivors vs the full
   validated-enzyme set for the class; keep identity < 30% (locked).
3. FAILURE-AWARE ADVERSARIAL REJECTION: adversarial panel = catalytically
   competent but non-pollutant-degrading members of the same enzyme family
   (e.g. broad-substrate esterases for C1, lactonases for C2), assembled from
   UniProt annotations BEFORE outcomes. A candidate is rejected if its best
   mmseqs2 identity to the adversarial panel >= its identity to the positive
   template panel (margin rule, locked).
4. STRUCTURAL ADJUDICATION (3 legs, from doc-1-016's validated rule):
   ESMFold fold of the candidate; (a) fold match to class template
   (TM-align-style superposition, threshold locked in GATES_LOCKED.md);
   (b) catalytic register conservation vs template active-site residues;
   (c) catalytic geometry (triad/dyad distances within locked cutoffs).
5. SCORING + REPORT: verbatim JSON per gate, no rerun selection.

## Benchmark design for the baseline-beat gate (locked)
Masked-panel rediscovery: hold out a panel of known validated enzymes per class
(10 PET hydrolases for C1, 5 PTEs for C2) by removing them from ALL reference
sets, then run (a) the homology-only single-leg comparator (PlasticEnz-style:
HMM hit + identity threshold as described in Gambarini et al. 2025,
reimplemented from the paper text - disclosed as reimplementation, not the
authors' code) and (b) the full multi-leg pipeline, on the same study data.
Metric (locked): precision on the masked panel at a fixed candidate budget of
20 per class, computed once, reported verbatim.

## Success (locked, her bar: beat a named published baseline AND find something new)
- Beats baseline: gate G4 (precision margin >= 10 points over the single-leg
  comparator at matched budget).
- Finds something new: gate G5 (>=10 fully gated novel candidates across >=2
  classes) + one lab-testable nomination (specific enzyme, substrate, assay).
- Tool: `polymine` CLI candidate adjudicator in tool/.

## Discipline
- Gates locked in GATES_LOCKED.md BEFORE outcome data; lock tag `lock-1`.
- Run once; verbatim results; no metric shopping; no threshold edits after outcomes.
- Honest negatives preserved in the record but never the paper's centerpiece.
- If G4/G5 fails: pivot within the project per standing rule and document the pivot.
- Public repo, free tiers only, results to repo + Drive.
