# PRIOR_ART - enzyme-mining platform

Checked 2026-10-10 (web, live):

- PlasticEnz (Gambarini et al., PLOS Comput Biol 2025) - homology + ML screening
  of meta-omics for plastic-degrading enzymes; plastics only; single-class.
  https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013892
  Code: https://github.com/msysbio/PlasticEnz
- XenoBug (2025) - ML predictor of pollutant-degrading enzymes from
  metagenomes; a classifier, no novelty gating or structural adjudication.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12044416/
- PlasticDB (2022) - database of plastic-biodegradation proteins/microbes.
  http://plasticdb.org/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC9216477/
- PAZy - plastics-active enzyme database (validated reference set source).
  https://www.pazy.eu/
- enviPath / EAWAG BBD - biotransformation pathway resources (reference only).

Verdict: CROWDED on plastics-only screening; the angle survives per the
standing rule ("if something is already built, give it a unique twist"):
cross-pollutant scope + failure-aware novelty gating + register-aware
structural adjudication in one locked protocol is not what these tools do.
The baseline-beat comparator is a PlasticEnz-style single-leg screen,
reimplemented from the paper text and disclosed as a reimplementation.

Internal prior art: doc-1-016-pet-hydrolases (same program) - PET-only, and its
failed sequence/domain screen is the motivation for the adversarial-rejection
leg; this project generalizes its 3-leg structural rule across pollutant classes.
https://github.com/uditakankananonononono/doc-1-016-pet-hydrolases
