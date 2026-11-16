# Dataset acquisition and remaining gaps

Search and acquisition update: **November 15, 2026** (local date; some retrieval timestamps are November 16 UTC). This records what was located and obtained in this environment, not a claim that an unsuccessful search proves no public copy exists. No restricted records were obtained, login controls bypassed, or messages sent to researchers. Published estimates were not substituted for observations.

## Acquired and analyzed

### Chapter 3: northern California kelp

The [original McPherson et al. article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7935997/) links a public [supplementary workbook](https://static-content.springer.com/esm/art%3A10.1038%2Fs42003-021-01827-6/MediaObjects/42003_2021_1827_MOESM4_ESM.xlsx). The `Figure 2d - Canopy Area` sheet contains annual regional canopy areas for 1985–2019; `Year` and `Full ROI Area (km^2)` are the selected fields. The manuscript's component design retains its original 2008–2012 and 2017–2019 comparison windows.

The mean falls from 2.606788 to 0.04615 km², or 98.23%. The [annual output](results/chapter03_kelp_canopy.csv) and [result/provenance](results/chapter03.json) are tracked. The workbook is cached locally with its download URL, timestamp, and SHA-256. `run.py run --chapter 3 --fetch` acquires it on a fresh checkout.

This resolves missing outcome observations, not causal identification. The workbook does not establish a preselected untreated comparison or exogenous site exposure. Its other spatial and biological series cannot simply be declared independent controls. The separately located [historical central-California archive](https://doi.org/10.5061/dryad.xpnvx0khq) is not a substitute for the northern California design. Next requirement: documented site coverage, independently defined exposure, and comparable sites, with the compound heat/predator-loss shock addressed.

### Chapter 12: fatal crashes and daylight-saving time

All sixteen [NHTSA FARS](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars) national CSV archives for 2000–2015 were downloaded. Their URLs follow `https://static.nhtsa.gov/nhtsa/downloads/FARS/{year}/National/FARS{year}NationalCSV.zip`. Each contains one national accident file. The builder selects crash identifiers, state/county, and date fields; it validates census coverage and identifiers before aggregation.

The 555,134 national crash records yield 541,122 known-date retained crashes, 64 retained incomplete-date crashes, 12,043 Indiana exclusions, and 1,905 Arizona county exclusions. The daily calendar has 292,200 rows. Indiana is excluded throughout because its rules changed and previously varied locally. Arizona excludes Apache, Coconino, and Navajo counties, plus unknown county codes, to avoid a mixed DST classification. The two non-DST controls are Hawaii and the retained Arizona geography; the other 48 geographic units observe DST.

Geographic/rule references: [US Department of Transportation time rules](https://www.transportation.gov/regulations/time-act), [NIST daylight-saving guidance](https://www.nist.gov/pml/time-and-frequency-division/popular-links/daylight-saving-time-dst), and the [Arizona Department of Education tribal/county report](https://www.azed.gov/sites/default/files/2026/04/OIEAnnualReport_SY2023_Final%20-%20MU%20Review.pdf). These establish coding choices, not exchangeability of the controls.

The [builder](acquire.py) preserves source hashes, date and exclusion audits, and construction metadata. The [result](results/chapter12.json) embeds that provenance and reports all yearly contrasts; [aggregate output](results/chapter12_dst_contrasts.csv) is tracked. Rebuild with `scripts/acquire.py --chapter 12 --fetch` before running chapter 12. Existing extracts are preserved; choose a fresh input directory to rebuild.

The mean event contrast is +0.03525 known-date fatal crashes per geography-day; the earlier placebo is −0.13374. Incomplete-date accounting bounds do not remove the larger placebo contrast. Two controls, raw unnormalized counts, seasonality, and inseparable daylight/sleep/travel/weather mechanisms prevent a clean causal interpretation. This acquires the required crash observations, not the extra exposure and weather variables needed for a stronger design.

## Primary extracts still missing

| Chapter | Sources checked and observed access | Required next input |
| --- | --- | --- |
| 1 — Blockade | [AEA article](https://www.aeaweb.org/articles?id=10.1257/aer.20151730), [author research page](https://www.rjuhasz.com/research/), and [openICPSR archive 113114](https://www.openicpsr.org/openicpsr/project/113114/version/V1/view). The indexed archive lists `replication_files_20151730_update1`; its download route redirected to ICPSR login. Direct archive/legacy retrieval returned 403 or no file. | Authorized replication download and documented mapping to regional 1803/1812 spindle counts, baseline capacity, and predetermined protection measure. |
| 4 — Scientist deaths | [NBER working paper](https://www.nber.org/papers/w14577), [MIT publication record](https://dspace.mit.edu/entities/publication/c829b4e8-be93-4f84-8590-0b89563ec39b), and [author study page](https://plum-apricot-hn5c.squarespace.com/posts/superstar-extinction). The paper describes licensed AAMC Faculty Roster inputs alongside publication data. No usable matched panel was located. | Predetermined collaborator networks, unexpected-death classifications, publication outcomes, and same-calendar matched controls; licensing and network overlap documented. |
| 5 — Electrification | [AEA article](https://www.aeaweb.org/articles?id=10.1257/aer.101.7.3078) and [openICPSR archive 112474](https://www.openicpsr.org/openicpsr/project/112474/version/V1/view). The public inventory lists `20080791_dataset`; direct retrieval and a legacy AEA data URL returned 403. No package was acquired. | Authorized replication download with community electrification/employment changes, terrain, baseline controls, and districts. |
| 9 — Schooling and IQ | [Brinch–Galloway study](https://doi.org/10.1073/pnas.1106077109) and [Statistics Norway research-data access policy](https://www.ssb.no/en/data-til-forskning). The required linked schooling/conscription extract was not obtained; SSB microdata access is institutionally controlled. | Authorized municipality/cohort outcomes and reform exposure, with migration, participation, and scale documentation. General public education statistics do not replace this linkage. |
| 13 — AI access | [Updated study](https://arxiv.org/abs/2403.01964), [author research site](https://davidkreitmeir.github.io/), and [Monash project page](https://www.monash.edu/business/impact-labs/soda-labs/our-projects/the-heterogeneous-productivity-effects-of-generative-ai). No usable daily fixed-cohort coding panel was located. | Pre-ban-defined developer cohort and daily per-developer contributions. The paper's country/sample specification differs from this repository's proposed donor pool; a supplied extract would require explicit reconciliation. Quarterly totals and reported coefficients cannot replace daily observations. |
| 14 — Data-center fire | [OVHcloud incident record](https://corporate.ovhcloud.com/en-gb/newsroom/news/informations-site-strasbourg/) and [RIPE historical prefix API](https://stat.ripe.net/docs/data-api/api-endpoints/announced-prefixes). The event and provider-wide diagnostic are available; a pre-fire facility-mapped service panel was not located. | Service availability for affected and matched unaffected facilities, with mappings, backups, and exclusions fixed before the fire. ASN prefix counts do not provide these outcomes. |

The chapter 13 Tor and chapter 14 BGP diagnostics remain runnable and explicitly secondary. The unresolved chapter 3 comparison is additional to the six primary extracts listed above. Access failures are recorded as such; they are not numerical null results.

## Evidence boundaries that are not missing-data downloads

Chapter 6 needs a model linking the ontological proposal to distinguishing observables. Chapter 7 records a published controlled granular mechanism without a new raw-data fit. Chapter 8 records a published conditional Oklo bound; optional predictions must come from specified physical models. No additional CSV alone would turn these records into identified natural experiments for the emergence of the universe.

Chapters 2, 10, and 11 already have usable public inputs and were rerun with the full registry. The [results summary](results/summary.md) and per-chapter JSON files report both their findings and identification limits.
