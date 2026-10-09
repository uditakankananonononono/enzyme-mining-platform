# Amendment 2 (partial): revised review copy, not locked

Date: 2026-10-10 IST. Supersedes no locked document until publicly committed,
reviewed, and tagged. No outcome run has occurred. G0 source retrieval only.

## Why amendment is needed
The original rediscovery corpus did not guarantee presence of held-outs; its
novelty filter would reject the known controls. Labels, ranking and ties were
not fixed. The published-method attribution and C3 chemistry were wrong.

## Separate benchmark and discovery
A benchmark FASTA must contain 10 experimentally PET-positive and 5 PTE-positive
held-outs plus independently assayed same-family negative proteins. It must be
separate from unlabelled environmental source proteins. No environmental protein
is assigned a negative label merely because activity is unknown.

Held-outs are removed by sequence identity from our training, templates and
adversarial panels before building our search references. Benchmark excludes G2
only; discovery applies G2 against the complete frozen reference collection,
including benchmark positives. This benchmark exemption is a CHANGED G2 scope;
discovery retains the locked <30% exclusion threshold against the class collection. The phrase "every experimentally validated
 enzyme" cannot be established by a database alone; report exact collection
coverage and unresolved omissions, not global proof of novelty.

G1 recovery thresholds remain 7/10 PET and 4/5 PTE. G3 and G4 thresholds remain
unchanged. Benchmark budget remains exactly 20 slots per class. NEW precision definition:
precision denominator 20, with empty slots counted as zero. A top-20 ranking does not change eligibility.
Before lock, freeze one labelled accession/sequence table, de-duplication rule,
rank score, tie rule, structural tool/settings and catalytic-atom table.
The locked templates remain C1 6EQE/FAST-PETase lineage, C2 1HZY, C3 1ZRN;
only the exact catalytic-atom/register/settings table is pending. Benchmark
held-outs must exclude all locked templates/lineage members used by G3/G4,
so removal cannot delete the template and invalidate those gates.
Those choices are still pending and no run may use this proposal as a default.

## Genuine published baseline
PlasticEnz: Krzynowek, Snoeks & Faust (2026), PLoS Comput Biol e1013892,
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013892
Authors' source: https://github.com/msysbio/PlasticEnz
Pin: 3ee1dc515f62fd7ece31b8ad06de49124974e1b1.
Use shipped PET custom-HMM + default classifier route, including the absence of a PET DIAMOND database as observed by the builder
at this pin. Authors' run_diamond.py maps PBSA/PBS/PCL/PES/PHBV/PLA/PVA,
not PET, and returns an empty list for unsupported polymers. Source file hash
b310b9829aba84b06d8baefc04c058df99362b559ab733c9b5948cb576bcb452;
file inventory is data/methods/plasticenz_shipped_files.json. Intent is unproved. Do not invent a PET DIAMOND leg. A classifier
resource failure means baseline UNSATISFIED, not substitution by homology-only.

CHANGED G5 scope: named-baseline margin >=10 percentage points applies to PET only, under the
same frozen benchmark FASTA. PTE has no PlasticEnz class; its comparison is
ablation-only and cannot satisfy the named-baseline bar. This weakens the original
both-class G5 requirement for PTE; PET changes from reimplemented single-leg
comparator to the real published tool, a stricter completion/resource dependency.
If it cannot complete, report UNSATISFIED or BLOCKED, never a substitution win.
The Pfam/mmseqs
single-leg comparator remains a separately labelled ablation for both classes.

Baseline training independence requires provenance against HMM build and
classifier training members. Exact absence from train.fasta alone is insufficient.
35/50 PET-positive author-test sequences are already in the author PET DB.
LEAKAGE-UNVERIFIED comparisons cannot support clean-win or project success claims.

## C3 correction and feasibility
C3 is INCLUDED for haloacid pollutants, with L-2-haloacid dehalogenase 1ZRN, not
DehI or chlorinated-solvent/PCE/TCE degradation. Source:
https://data.rcsb.org/rest/v1/core/entry/1ZRN
The preselected MGYS00005009 assembly's first annotated partition yields 60,935
CRC-valid proteins, exceeding 5,000. Inclusion cannot be dropped for low yield.
All four fixed partitions now CRC-complete,211621 proteins total; payload
hashes recorded in data/sources/c3_counts.json and C3_MANIFEST.sha256. Habitat alone proves no catalytic activity.

## Discovery and prior art
G6 remains >=10 candidates passing G2+G3+G4 across >=2 classes. G7 remains CLI
reproduction plus enzyme/substrate/assay nomination. Proposed nominees are
unvalidated until lab tests; substrate-match must be evidence-based.
Success-section numbering is G5 baseline and G6 discovery, not G4/G5.

Structure-guided PET screening is existing work (VenusMine 2025):
https://www.nature.com/articles/s41467-025-61599-z
Remaining proposed contribution is cross-pollutant screening plus independently
assayed same-family rejection and strict reference exclusion, requiring measured
validation. Architecture alone is not discovery or proof of originality.

## Fixed readiness floors, before labels or scores are used

Amendment 3 must name and SHA256-record 10 PET positives, 5 PTE positives,
and at least 20 measured same-family negatives per class. Select entries from
primary assay evidence without consulting PlasticEnz or our model scores;
record a deterministic accession-order rule and assay conditions in the table.
No outcome score exists yet. Below 20 measured negatives in either class is
BLOCKED, never a relaxed floor. Templates are retained: held-outs cannot include 6EQE, the FAST-PETase lineage
reference used by G3/G4, 1HZY, or 1ZRN. Same-family means the same catalytic-family
Pfam accession as that class's positive template, assessed using pyhmmer and a
frozen Pfam HMM with full-sequence E-value <=1e-5. Pfam accession/profile hashes
remain deferred to amendment 3, so this criterion is not currently executable.

Benchmark corpus: exactly 10+20=30 deduplicated PET proteins and 5+20=25 PTE
proteins, all labelled under named primary assay conditions. G1 recovery is
within the top 20 eligible predictions of each respective corpus, not among
unlabelled metagenome proteins. Repeated sequence hashes have one entry;
conflicting positive/negative assay evidence is excluded as contested, not
resolved by score. Do not add extra negatives after scores are seen.

CHANGED masked-panel removal definition: remove held-outs from our reference
panels by exact sequence equivalence (no broader homology exclusion implied):
mmseqs2 alignment identity 1.0 with both query and target coverage 1.0,
alignment-mode 3; exact SHA256 sequence matching independently verifies removal.
This is exact-member exclusion, not homology-cluster independence. It does NOT
remove members from shipped PlasticEnz HMM/classifier training; those models
stay unmodified. A clean G5 PET comparison requires all 10 positives and 20
negatives documented absent from baseline HMM-build and classifier-training
members. Fewer independently proven entries = G5 NOT ASSESSABLE, not a win.
Unverifiable training provenance = LEAKAGE-UNVERIFIED and no clean-win claim.

Precision at 20 is TP/20, including empty slots as zero. One positive changes
precision by 5 percentage points; with 10 PET positives the maximum is 50%.
The >=10-point margin is a directional descriptive gate, not statistical
significance. Report an exact binomial interval for TP/20 as a descriptive
interval only, with the note that selected correlated proteins are not an
independent random trial sample. PTE 4/5 recovery is a coarse 80% floor with
20-point recovery increments. Neither PTE recovery nor its ablation satisfies
the named-baseline gate. PlasticEnz default settings and ranking are frozen in
data/methods/plasticenz_settings.json and its SHA256 file; no --sensitive.
Our pipeline ranking/tie rule and all structural/catalytic settings remain
DEFERRED to amendment 3 before any benchmark or discovery run.

C3 selected partitions are fixed, not outcome-selected: MGYA00375579
ERZ795384_FASTA_CDS_annotated.faa.gz and ERZ795384_FASTA_CDS_unannotated.faa.gz;
MGYA00375580 ERZ795386_FASTA_CDS_annotated.faa.gz and
ERZ795386_FASTA_CDS_unannotated.faa.gz. Record every payload SHA256 before any
run; all partition hashes are now recorded in C3_MANIFEST.sha256 and must be
included in amendment3.

PET novelty is only the stated frozen reference-exclusion protocol. G6/G7
nominees are unvalidated lab-testable hypotheses, not proven new chemistry.
Contribution claims must be restricted to the gates actually tested/passed.

## Preservation statement, scoped precisely

G1 7/10, 4/5, budget 20, and 10pp unchanged; G5 narrowed to PET with real
baseline (PTE ablation-only); G2 discovery-only; zero-fill precision definition
added. Other preserved threshold values do not imply unchanged gate scope.
C3 is INCLUDED under locked G0 yield rule, with a recorded chemistry scope
reduction from unsupported solvent/DehI framing to haloacid pollutants/1ZRN.

## Original-to-corrected cross-reference

| Original location | Original wording/reference | Correct reference | Change |
| --- | --- | --- | --- |
| GATES_LOCKED G1 | Positive-control recovery | G1 | ID/threshold unchanged |
| GATES_LOCKED G3 | Adversarial margin >0 | G3 | ID/threshold unchanged |
| GATES_LOCKED G4 | Structure >=60%, TM>=0.5 or RMSD<=4A, geometry<=2A | G4 | ID/threshold unchanged |
| PROTOCOL Success | baseline beat gate G4 | G5 | Fix mistaken cross-reference, not renumbering |
| PROTOCOL Success | discovery gate G5 | G6 | Fix mistaken cross-reference, not renumbering |
| GATES_LOCKED G6 | >=10 across >=2 classes | G6 | ID/threshold unchanged |
| GATES_LOCKED G7 | CLI + lab nomination | G7 | ID/threshold unchanged |

Original lock files are immutable: GATES_LOCKED.md SHA256
 d62fa5d3d4f04eec50367a365e671a356b02823df26e65cce28a289f38190fb1,
PROTOCOL.md SHA256 0fb8de0db39184ef7d4abe0a3e48b9d0f18e21d8655ed8491c0273e6b7e0bb36.

## Hard readiness blockers
Measured PET-negative labels are not recovered. ACS source XLSX route blocked
by Cloudflare/403, author Zenodo range recovery stopped HTTP429 after 433 headers
(221,696 bytes) with no assay table. Both routes parked without polling/retry.
PANTS is a lead only, not a label authority. VenusMine's pNPB-negative prefilter
is not a PET-negative assay. Panels/ranking/catalytic settings are unfrozen.
Thus G1/G5 are BLOCKED, not failed, and no outcome run is allowed. G0 ongoing.
No lock-2 tag may falsely imply these missing inputs/settings are frozen.

## Geometry defect: readiness remains BLOCKED
At 30 proteins, G1 7/10 is at chance; a pass here is uninformative.
Exact hypergeometric PET expectation6.6667, P(recovery>=7)=0.5603394107;
PTE expectation4, P(recovery>=4)=0.7477696217. These were calculated without
any model scores. Amendment3 must fix this before any run. Proposed additional
criterion: exact upper-tail random-ranker p<0.05 per class, alongside original
recovery floors and20-budget. This is an ADDED gate, not original protocol.
No outcome run; labelled tables and inferential correction remain unfrozen.
Rediscovery means after exact-member removal, never independent held-out proof;
per-positive max identity to remaining references must be reported descriptively.

02:04 geometry consequence (no model scores): at N30/K10/k20 PET, the added
p<0.05 criterion needs10/10 recovery, effectively a perfect-recovery requirement;
P>=9 is0.0620521 and P=10 is0.0061493. At N25/K5/k20 PTE even5/5 has
p=0.2918125, so p<0.05 is impossible. PTE inferential gate is NOT ASSESSABLE
at current proposed geometry; it remains descriptive unless amendment3 enlarges
the corpus before any scores. No post-score relaxation of p is permitted.
Corpus/label readiness remains BLOCKED; this note does not authorize a run.
