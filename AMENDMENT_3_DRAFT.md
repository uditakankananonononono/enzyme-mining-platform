# Amendment 3: synthetic-negative rediscovery design

Date: 2026-10-10 IST. Status: DRAFT, UNLOCKED, NOT EXECUTABLE.
Gate review is required before freeze. No new lock tag exists. No benchmark,
classifier, HMM, structure or discovery outcome computation has occurred.
G0 transport is complete; its CRC, counts and sequence-membership checks are
pre-outcome preparation, not a benchmark run.

## Decision and immediate limits

Replace the unavailable measured-negative benchmark with a PET spike-in
rediscovery experiment using unlabelled study proteins as the background.
This is a **synthetic-negative design**, not measured-negative validation.
The background proteins are real public sequences, not synthetic sequences.
Only their benchmark role is synthetic: non-spike entries receive an operational
zero for spike recovery. Unknown PET activity is never called experimentally
negative. No assay specificity, true precision or false-positive-rate claim
can follow from these operational zeros.

**PTE inferential gate: NOT ASSESSABLE by design.** Retain the 25-entry,
5-positive, top-20 diagnostic geometry. Even all five recovered has exact
random-ranker upper-tail p = 2584/8855 = 0.29181253529079615, above 0.05.
PTE is descriptive only. The 20 background entries in this diagnostic are
unlabelled, not measured negatives. Do not present PTE as a significant
validation or as satisfying the named-baseline success bar.

ACS assay-source retrieval stopped at Cloudflare/HTTP 403; the author-linked
Zenodo archive route stopped at HTTP 429. No valid measured-negative panel was
recovered. Those routes remain terminal for this design, with no polling,
retry or substitution of VenusMine pNPB negatives for PET-negative assays.
PANTS remains a lead, not label evidence. This amendment removes the measured
negative requirement for this benchmark, not the lack of biological validation.

## Changes relative to amendment 2

1. CHANGED PET benchmark universe: the 30-entry measured-labelled design is
   replaced by 10 known PET-positive spikes plus the frozen C1 study background.
   Background entries have unknown catalytic labels. The required floor of 20
   measured same-family benchmark negatives is withdrawn, explicitly.
2. CHANGED endpoint: use spike recovery and spike yield at a 20-slot budget,
   not biological precision. Spike yield = recovered injected positives / 20;
   empty slots and non-spike entries contribute zero to this operational metric.
3. ADDED PET chance test: exact upper-tail hypergeometric p < 0.05, in addition
   to >=7/10 recovery. No post-score changes to p, budget or corpus.
4. PTE NOT ASSESSABLE: the retained 25/5/top-20 diagnostic cannot meet p<0.05
   even at 5/5. Its >=4/5 floor remains a descriptive number only.
5. CHANGED G5 endpoint: >=10 percentage-point PET margin becomes a descriptive
   spike-yield margin against actual PlasticEnz, not measured precision. This
   change does not by itself establish better biological selectivity.
6. G2 remains discovery-only. Benchmark controls are exempt from novelty.
   Discovery retains <30% identity against the complete frozen class reference
   collection, including benchmark positives. Collection coverage, omissions
   and limits must be stated; global novelty is not proven.
7. G3/G4 thresholds, G6 >=10 candidates across >=2 classes and G7 tool plus
   lab-testable nomination are not relaxed. Unknown-activity study proteins
   cannot become the biological G3 adversarial panel merely by being non-spikes.

Original PROTOCOL.md and GATES_LOCKED.md remain immutable historical lock-1
records. AMENDMENT_PROPOSED.md remains amendment-2 historical review copy.
This draft supersedes none of them until review and a complete freeze.

## PET corpus construction, before any outcome score

Use the fixed C1 accession selection already retrieved under G0, not an
outcome-selected subset. Source selector is
`data/sources/expected_analysis_selection.json`; source counts are
`data/sources/G0_COMPLETION.json`; payload identities are
`data/sources/G0_ALL_PAYLOADS.sha256`. G0 C1 has 6,468,866 raw protein records.
That count is not the deduplicated benchmark N.

Planned deterministic construction:
- Normalize FASTA sequences by removing formatting whitespace and uppercasing.
  Reject empty or non-standard amino-acid strings; record every rejection and
  reason without using model scores. No length-based sampling or class-hit
  prefilter defines the statistical benchmark universe.
- Collapse exact normalized sequence duplicates by SHA256. Preserve all source
  accessions for provenance; choose the lexicographically smallest
  `(analysis accession, original FASTA identifier)` as representative.
- Remove exact copies of the ten selected spike sequences from background
  before adding each selected spike once. Keep the removed natural-occurrence
  provenance. This prevents double counting, not homology leakage.
- Sort the combined canonical sequence records by sequence SHA256 ascending.
  Freeze the FASTA, source map, label-role table and their checksums before any
  search or scoring. PET K is exactly 10; PET N is the number of unique eligible
  background sequences plus 10. Require N >= 30 and at least 20 records for
  the fixed budget. N and the precomputed tail table must be recorded pre-run.

A protein with PET activity that was not an injected positive remains a
non-spike in this metric, not a false positive biologically. Any post-run assay
or literature discovery is separate evidence; it must not alter this run's
spike-role labels or inflate its recovery result.

## Positive-panel selection and leakage

Positive sequences require primary PET assay provenance with accession,
sequence hash, substrate, conditions and source reference in a frozen table.
Selection occurs without PlasticEnz or pipeline outcome scores. Exclude locked
6EQE/FAST-PETase lineage templates and all exact template-panel members.
Eligible entries are ordered by canonical accession, then sequence SHA256;
select the first ten satisfying the provenance rules. If ten cannot be
verified, PET is BLOCKED. Never fill missing positives with unassayed sequences.

For a clean G5 comparison, establish absence of all ten spikes from both the
PlasticEnz HMM-build members and classifier-training members. The shipped
baseline stays unmodified. Absence from train.fasta alone is insufficient.
If the provenance cannot be established, G5 is NOT ASSESSABLE and the comparison
is LEAKAGE-UNVERIFIED. It cannot support a clean win or project success claim.
Background training overlaps must also be reported; this is not an independently
assayed generalization test even when spike provenance is established.

Remove exact spike members from our search/training/reference panels using
sequence SHA256, independently checked with mmseqs2 identity 1.0, both query
and target coverage 1.0, alignment-mode 3. Report per-spike maximum identity to
remaining references. Call the result rediscovery after exact-member removal,
not homology-independent validation. The ten sequences and complete panels
are still pending, so these rules are not an executable freeze.

## Ranking, slots and inference

Both methods receive the same frozen PET FASTA and the same 20-slot budget.
Rank all eligible outputs once. An ineligible or missing record is not secretly
replaced by a less demanding tool. Do not discard background from N merely
because a method does not score it. If fewer than 20 eligible predictions exist,
empty slots are zero; show emitted count and empty count separately.

The PlasticEnz comparator is the shipped PET custom-HMM plus default XGB route
at commit `3ee1dc515f62fd7ece31b8ad06de49124974e1b1`, using the frozen settings
in `data/methods/plasticenz_settings.json`. Rank `PET_prediction_xgb` descending,
then sequence SHA256 ascending; missing probability is ineligible. PET DIAMOND
is absent from the shipped mapping and unused; intent is unproved. No
homology-only fallback can be counted as PlasticEnz. Resource failure is
UNSATISFIED/BLOCKED, not a substituted baseline victory.

Our ranking score, tie handling, class-profile hashes, complete G3 panel and
G4 tool/register/catalytic-atom settings remain pending, required for freeze.
Budget, label roles and chance-test denominator cannot be changed by those
implementation tables. Missing method settings keep outcome computation blocked.

For a uniform random order of the full frozen corpus, X has hypergeometric
parameters N (corpus size), K (injected positives), k = 20 (budget).
Report E[X] = k*K/N and

`P(X >= r) = sum_{x=r}^{min(K,k)} C(K,x)*C(N-K,k-x) / C(N,k)`

with impossible combinations contributing zero. Use integer combinations and
exact rational arithmetic; emit numerator, denominator and decimal. Require
PET r>=7 and PET p<0.05. Freeze every attainable recovery tail before scores.
The tail is a chance-ranking diagnostic, not a paired significance test of our
method versus PlasticEnz, not biochemical validation, and not a discovery p-value.
Underfilled output uses the fixed 20-slot test with zero-filled slots, a
conservative chance diagnostic; also report actual emitted count. No
eligibility-conditioned test can replace the full-corpus preregistered test.

Report our PET recovery, baseline recovery, each spike yield, the paired
per-spike recovered/not-recovered table and descriptive yield margin. G5's
numerical margin remains >=10 percentage points, equivalent to two more spikes
at the fixed denominator. No binomial precision interval over correlated
selected proteins is offered as assay-validation evidence.

## PTE diagnostic, separate from the PET test

Planned panel: 5 primary-assay PTE-positive sequences, excluding the 1HZY
locked template, and 20 unlabelled C2 study proteins. Sort eligible canonical
C2 background sequences by sequence SHA256, exclude exact spike members, take
the first 20; deduplicate before selection. Freeze all 25 identities and role
labels pre-run. Do not call the 20 entries experimentally negative or invoke
them as a G3 adversarial panel.

N=25, K=5, k=20 gives E[X]=4; P(X>=4)=13243/17710 and
P(X>=5)=2584/8855. Therefore PTE inferential gate is NOT ASSESSABLE as a
design consequence, including at perfect recovery. Report the 4/5 descriptive
floor and all actual counts verbatim; neither PTE nor its single-leg ablation
can satisfy the named published baseline bar. Do not expand the panel or
lower p after outcomes. A larger inferential PTE study would be another
pre-outcome amendment, not a reinterpretation of this diagnostic.

## Discovery and success remain gated

C3 remains INCLUDED for haloacid pollutants with L-2-haloacid dehalogenase
1ZRN, not chlorinated solvents/DehI. Four G0 partitions total 211,621 records;
C2 totals 758,003; all classes total 7,438,490 raw records. Source and partition
hashes must carry through the final freeze manifest.

G3 still needs a biologically supported same-family adversarial reference
panel. Lack of measured benchmark negatives neither proves nor replaces G3
specificity. Pfam accession/profile SHA256, pyhmmer settings and primary
reference evidence must be frozen. G4 retains >=60% passing all structural
legs (TM>=0.5 or catalytic-core RMSD<=4 A; compatible catalytic register;
key atom distances within 2 A). Tools, versions, catalytic atoms, handling of
missing structures and reference hashes must be explicit before compute.

G6 and G7 require the existing threshold, full metrics, reproducible CLI and
a substrate-matched lab-testable nomination. Candidates remain unvalidated
hypotheses. The overall portfolio success claim additionally requires an
independently accepted named-baseline win and something new. A PET spike-yield
margin alone is not proof of that broader claim or measured-negative rejection.

## Review/freeze checklist: all required before execution

- Review acceptance of the explicitly weakened synthetic-negative endpoint,
  PTE NOT ASSESSABLE and the distinction from biological precision.
- Ten PET and five PTE primary-assay positive identities/hashes and conditions;
  baseline training-provenance verdict; no outcome-based selection.
- Canonical FASTAs/role tables/source maps/hashes and actual PET N; pre-score
  exact-tail table; final PTE 25-entry role table.
- Complete positive/adversarial/validated reference panels and profile hashes;
  scope-limited novelty claims; locked templates retained.
- Our ranking/tie implementation; structural tool versions/settings and exact
  catalytic-register/atom table; complete handling of failures.
- PlasticEnz pinned files/settings plus a no-outcome resource-feasibility plan.
- Final immutable amended protocol/gate tables, complete input manifest,
  separate gate review, then lock tag before any outcome computation.

Until this checklist is satisfied: amendment 3 remains DRAFT/UNLOCKED,
G1/G5 outcome execution remains BLOCKED, and no success/discovery claim is made.
