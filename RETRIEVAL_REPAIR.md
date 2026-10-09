# Retrieval repair, 2026-10-10 IST

The initial download was interrupted without a recorded traceback. Its first
MGYA00572563 gzip file was truncated (38,797,312 bytes versus the server's
40,295,368 bytes). No counts or sequence-screen outcomes were recorded.

Transport-only changes: partial files have a .part suffix; Range resume is
accepted only with a matching Content-Range; otherwise the server response
restarts from zero. Reading the entire gzip checks CRC before completion is
marked. Files become final only after validation. Requests retain their timeout
across retry attempts. --one bounds a foreground run to one completed analysis.
No studies, accession selection, biological thresholds, or outcome gates changed.

Two completed gzip inputs are recorded in data/sources/g0_counts.json. Further
retrieval is pending. This is not a G0 pass or a benchmark run.

Second transport-only repair: a timeout left MGYA00572570's payload fully
downloaded but not yet renamed/recorded. A later Range request at exact EOF was
rejected. Verified gzip CRC and server Content-Length (45,235,745 bytes), then
accepted its 334,759 protein records. Complete .part files now receive that
CRC+source-length check before requesting more bytes. No sequence-screen run.

C2 metadata exposed the same older-pipeline naming issue found during C3
feasibility. MGYA00153745 has separate annotated/unannotated CDS FASTAs; the
original predicted_cds-only matcher reported no download incorrectly. That
negative observation remains in g0_counts.json as historical evidence, not a
source-unavailability claim. The matcher now selects both partitions if no
combined CDS file exists. Counts are recorded per analysis+alias. No filtering
by annotation/function and no biological source selection changed. First C2
partition transfer broke with IncompleteRead; partial bytes preserved, resumable.
--only-study changes retrieval order only within the preselected study list.
