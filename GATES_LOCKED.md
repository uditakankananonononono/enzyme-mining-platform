# GATES_LOCKED - enzyme-mining-platform

Locked 2026-10-10 (IST) before any real-data compute. Tag: `lock-1`.
Any deviation must be written to DEVIATIONS.md with its reason before results.

- G0 FEASIBILITY: all listed data sources reachable; per-study protein counts
  recorded in data/STUDIES.md. PASS = fetch completes with counts > 0 for C1
  and C2 study sets. If C3 yield < 5,000 protein records, C3 is dropped and
  the drop is recorded (allowed deviation, pre-declared here).
- G1 POSITIVE CONTROL: with the masked panel removed from every reference set,
  the pipeline rediscovers >= 70% of the masked known enzymes per class
  (C1: >= 7/10 masked PET hydrolases; C2: >= 4/5 masked PTEs).
- G2 NOVELTY (homolog-exclusion): every reported candidate has < 30% mmseqs2
  identity to EVERY experimentally validated enzyme of its class (validated
  set frozen in data/validated_sets/ before outcomes).
- G3 FAILURE-AWARE ADVERSARIAL REJECTION: every reported candidate's best
  identity to the positive template panel strictly exceeds its best identity
  to the adversarial same-family panel (margin > 0, both measured with the
  same mmseqs2 settings).
- G4 STRUCTURAL ADJUDICATION: >= 60% of candidates passing G2+G3 pass all
  three structural legs: (a) fold match to class template (TM score >= 0.5
  or RMSD <= 4.0 A over the catalytic core, measured with a recorded tool);
  (b) catalytic register: template active-site residues align to
  chemically compatible residues in the candidate; (c) catalytic geometry:
  key catalytic-atom distances within 2.0 A of the template's distances
  (per-residue tolerance, recorded per class).
- G5 BASELINE BEAT: precision on the masked-panel benchmark at candidate
  budget 20/class exceeds the single-leg homology comparator by >= 10
  percentage points, computed once, verbatim.
- G6 DISCOVERY: >= 10 candidates passing G2+G3+G4 across >= 2 pollutant
  classes; each reported with sequence, source study, all gate metrics.
- G7 TOOL + NOMINATION: `polymine` CLI reproduces the candidate table from
  committed inputs; one lab-testable nomination (enzyme + substrate + assay)
  written into the paper.

Negatives: every failed gate is preserved verbatim in results/ with its raw
numbers. The paper leads with what passed; failures appear once, as limits
and next experiments, never as the centerpiece.
