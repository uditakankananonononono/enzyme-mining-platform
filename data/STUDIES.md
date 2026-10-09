# STUDIES - locked study selection (pre-outcome metadata only)

Selected 2026-10-10 from MGnify API metadata (study names, experiment types,
download availability). No outcome data has been fetched or inspected beyond
file existence/availability. Recorded per locked protocol; tag `lock-1` covers it.

## C1 PLASTICS (PET hydrolase leg)
- MGYS00006544 - TPA metagenomic assemblies of PRJNA777294: "Tracking Genomic
  Characteristics across Oceanic Provinces: Early and Mature Plastic Biofilm
  Communities". 44 assembly analyses (WGS, metaSPAdes). Confirmed: analysis
  MGYA00693733 exposes "Predicted CDS (aa) FASTA" download.
- MGYS00005625 - TPA metagenomics assembly of PRJEB15404 (Plastic Metagenome).
  12 assembly analyses.
- MGYS00005970 - "Polyethylene film incubated in situ marine condition".
  3 assembly analyses.

## C2 ORGANOPHOSPHATE PESTICIDES / INDUSTRIAL EFFLUENT (PTE leg)
Public shotgun agricultural-soil studies on MGnify are overwhelmingly amplicon
(verified: MGYS00000652 216 analyses all amplicon; MGYS00000998 211 amplicon).
Pesticide/industrial-chemical degradation hunting ground therefore uses
wastewater/activated-sludge assemblies, where xenobiotic degradation
pathways concentrate and predicted proteins are available:
- MGYS00002316 - Activated sludge microbial communities (TPA assembly).
  1 assembly analysis.
- MGYS00005985 - Sewage microbial community (PRJNA593593, hybrid assembly).
- MGYS00005997 - Sewage microbial community (PRJNA593594).
- MGYS00006000 - 20 biogas reactors, long+short read metagenomics
  (agro-industrial waste; assembly availability confirmed at G0).

## C3 CHLORINATED SOLVENTS (haloacid dehalogenase leg)
Evaluated at G0 per locked gate: included only if contaminated-site assembly
studies yield >= 5,000 protein records; otherwise dropped and the drop is
recorded (pre-declared allowed deviation in GATES_LOCKED.md).

## Validated-enzyme reference sets (frozen before outcomes)
- C1: PAZy + PlasticDB validated PET-active enzymes; templates IsPETase
  (PDB 6EQE) and FAST-PETase lineage. Masked benchmark panel: 10 known PET
  hydrolases (list frozen in data/validated_sets/ before outcomes).
- C2: experimentally validated PTE/OPH family (template PDB 1HZY).
  Masked benchmark panel: 5 validated PTEs.
- Adversarial panels (per locked G3): catalytically competent same-family
  non-degraders (broad-substrate esterases for C1; lactonases for C2),
  assembled from UniProt annotations before outcomes.

## Discipline note
Study selection used API metadata only. No protein sequences, annotations,
or analysis results have been downloaded or examined for any study above
beyond confirming that the "Predicted CDS (aa)" download object exists.
