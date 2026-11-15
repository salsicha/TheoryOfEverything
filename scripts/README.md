# Natural experiments for the book

This folder turns the twelve chapters into **twelve specific empirical research designs**, with runnable estimators, source records, input contracts, and explicit limits. The designs test parts of the argument. They do not establish a universal tendency to maximize entropy production, the inevitability of AI, or the assembled origin of the universe.

The current run contains **three primary empirical reanalyses/comparisons** (chapters 2, 8, 9), **two secondary data diagnostics** (11, 12), and **one published physical constraint check** (6). Six cases still need research datasets. The primary outcomes for 11 and 12 also need data. See the [generated results](results/summary.md), including results that weaken or fail to establish a proposed mechanism. No historical observations were invented; artificial observations exist only inside software tests.

The prologue, epilogue, and methodological afterword frame the twelve chapters; they are not additional empirical studies.

## Chapter map

| Chapter | Candidate natural experiment | What it tests | Current implementation |
| --- | --- | --- | --- |
| 1 — Bottlenecks | Napoleonic blockade and French mechanized cotton spinning | Can a restriction make a new productive assembly viable? | Regional change regression; needs replication extract |
| 2 — Gradients and barriers | Japan's 2011 disaster and nuclear shutdowns | Does closing an energy pathway redirect electricity production? | Public energy data; synthetic-control comparisons |
| 3 — Living renewal | California kelp collapse following predator loss and heatwaves | Can disrupted maintenance cause persistent loss of living conditions? | Matched-site changes; needs exposure and survey panel |
| 4 — Discovery | Unexpected deaths of leading scientists | Does disrupting a knowledge network reduce what its members can produce? | Matched-network changes; needs bibliometric panel |
| 5 — New pathways | South African rural electrification | Does making an energy pathway accessible change productive participation? | Terrain-instrumented 2SLS; needs community extract |
| 6 — Physical origins | Oklo's ancient natural reactors | Does a proposed varying-constant model satisfy an isotope-based bound? | Published-bound checker; cosmic origins remain unidentified |
| 7 — Human development | Norway's compulsory-schooling reform | Can a social change in development affect measured cognitive performance? | Cohort-specific DiD; needs authorized administrative extract |
| 8 — Collective intelligence | Maimonides' class-size rule | Does a formal constraint change teaching resources and learning? | Public author data; fuzzy regression discontinuity |
| 9 — Economic reproduction | New Jersey's 1992 minimum-wage increase | Does a changed wage guarantee disrupt employment in the affected sector? | Public author data; two-wave DiD points |
| 10 — Regulation and renewal | US daylight-saving transitions | Does disrupting a maintenance schedule impair regulated performance? | Daily crash comparison and placebo windows; needs FARS extract |
| 11 — AI dependence | Italy's 2023 ChatGPT restriction | What changes when access to an AI service is interrupted? | Primary coding-panel adapter; public Tor diagnostic only |
| 12 — Computational infrastructure | OVHcloud's Strasbourg fire | What changes when the physical support of computation fails? | Primary facility/service adapter; public BGP diagnostic only |

Full specifications, source links, predictions, competing explanations, and data requirements are in [experiments.json](experiments.json). These are proposed specifications informed by existing studies, **not preregistrations** and not exact reproductions of every published model.

## Run

From the repository root, with Python 3.14 (tested on 3.14.5):

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/run.py list
.venv/bin/python scripts/run.py run --chapter all --fetch
.venv/bin/python -m unittest discover -s scripts/tests -v
```

`--fetch` permits network downloads from the public URLs recorded in the code. It never replaces an existing cache. A cached run needs no network:

```sh
.venv/bin/python scripts/run.py run --chapter all
.venv/bin/python scripts/run.py run --chapter 8 --output /tmp/toe-chapter8
```

Options: `--chapter 1` through `12` or `all`; `--inputs PATH`; `--cache PATH`; `--output PATH`; `--strict`. Without `--strict`, an audited missing-data result is a successful report, not a runtime error. Errors exit 1. With `--strict`, missing data, a secondary-only diagnostic, a published-summary-only constraint, or cohort points without inference exit 2. Exit 0 never certifies causal identification.

The latest invocation writes `summary.md` and `run_manifest.json` for its selected chapters. Each chapter JSON embeds its own complete run metadata, so later partial runs cannot erase its provenance. Use a separate output directory to retain a prior run. Raw downloads and local input extracts are ignored by Git. Small result tables, manifests, code, and specifications are tracked.

## Read the results correctly

- **`conditional_effect_estimate`**: an estimator ran; its causal interpretation still depends on the documented assumptions and diagnostics. This label does not certify the assumptions.
- **`descriptive_comparison`**: a comparison ran, but available assignment or measurement does not warrant a causal-effect claim.
- **`secondary_diagnostic_only`**: available data address a secondary question, not the primary chapter outcome.
- **`published_constraint_only`**: the code records a sourced bound and can compare supplied model predictions with it. It has not re-estimated the underlying physical evidence.
- **`conditional_point_estimate`**: cohort-specific change estimates are available, but uncertainty estimation is not implemented in that adapter.
- **`needs_data`**: a required dataset or its provenance is absent/inaccessible. No values are substituted.
- **`error`**: validation or execution failed; investigate before interpreting anything.

Current numerical findings and their limits:

- Chapter 2: Japan's 2011–2015 fossil electricity share averages **29.56 percentage points above** its fitted comparison, while nuclear share averages **22.29 points below** a separately fitted comparison. Removing the UK donor reduces the fossil gap to about 20.40 points. The two fits have different weights; their gaps are not an energy balance. The disaster, shutdowns, policy, demand, and international responses are not separated.
- Chapter 8: the primary math estimate is **−0.406 score points per additional pupil**, using 207 schools near the first threshold. The first-stage clustered t² is **9.50**, below the reporting screen, so no conventional IV interval is shown. Wider-bandwidth intervals include zero. This is inconclusive evidence for the component mechanism, not a confirmed cognitive law.
- Chapter 9: the NJ–PA employment-change contrast is **+2.75 FTE per restaurant**, using 384 paired observations. The archive already records permanent closures at zero; explicitly applying that rule does not change the result. Only two state policy assignments exist, so the report supplies no policy-level interval or p-value.
- Chapter 11: the Tor proxy has a mean fitted gap of only **+31 estimated users**, compared with pre-fit error around 1,238 users, and is sensitive to donors. It does not provide robust evidence of a circumvention increase in this specification. Nine missing January dates are omitted for every country; no values are interpolated. This says nothing directly about coding productivity.
- Chapter 12: provider-wide visible BGP prefixes range from **125 to 130**. Those counts do not identify the affected facility or whether services worked. The primary infrastructure effect remains unestimated.

These values describe the recorded data snapshot and specifications. Reruns with new snapshots belong in a new output directory and may differ. The generated JSON/CSV files are the authoritative numerical record.

## Supplying the missing primary data

Copy a header-only CSV and its JSON sidecar from [templates](templates) into `scripts/inputs/`. Populate real observations and fill the sidecar's `sources`, `construction`, `coverage`, and `assignment` fields. A bare CSV, empty template, or missing required value is rejected. Document the original version, licenses/access conditions, variable mapping, units, exclusions, and any upstream aggregation. Do not put restricted personal records in Git; use authorized, appropriately aggregated research extracts.

The sidecars are provenance records, not claims that assumptions have been proved. The analyst must substantiate the assignment process and pretrends. Merely filling a field cannot make a comparison causal.

### Chapters 1, 3, 4, and 12: paired changes

Required base columns: `unit,period,outcome,exposure,cluster`. Each unit has exactly one row for period `0` and one for `1`. `exposure` and the assignment-level `cluster` must be fixed before outcomes are observed. Units get equal weights. The estimator regresses each unit's change on its exposure. Inputs are window means only where specified; retain the source time series to inspect pretrends and exclusions.

Chapter 1 additionally requires a fixed `baseline_capacity`; chapters 3, 4, and 12 require a fixed matching-set `stratum`. Matching-set indicators are included as fixed effects. Controls must be predetermined. The code rejects duplicates, attrition between the two periods, missing values, changing assignments, or a rank-deficient comparison. It does not silently discard incomplete units.

- **1:** department-level mechanized spindles in **1803 and 1812**, baseline capacity, and the paper's geographically constructed trade-protection measure. [Juhász's study](https://www.aeaweb.org/articles?id=10.1257/aer.20151730) and [replication archive](https://doi.org/10.3886/E113114V1). The archive returned HTTP 403 here. Spatial dependence needs substantive attention; arbitrary administrative clusters do not guarantee independence. Our simplified change regression is not the full published analysis.
- **3:** fixed survey-site canopy hectares averaged over **2008–2012** and **2017–2019**, independently measured heat/disease exposure, and preselected comparable sites. [Rogers-Bennett and Catton](https://doi.org/10.1038/s41598-019-51114-y), [McPherson et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC7935997/), and a [historical kelp inventory](https://doi.org/10.5061/dryad.xpnvx0khq). Dryad metadata were accessible, but downloads returned 401/403. A canopy dataset alone supplies neither exogenous exposure nor comparable controls. Northern bull kelp and southern giant kelp cannot simply be interchanged. Ecosystem renewal is only an analogue for the chapter's organism-level claim.
- **4:** collaborators fixed before an unexpected active scientist's death; mean network output in years **−5 to −1** and **+1 to +5**, with same-calendar-year matched controls. [Azoulay, Graff Zivin, and Wang](https://www.nber.org/papers/w14577). Obtain/construct the publication and match panel, verify death classification, and account for overlapping networks before aggregation. No public usable panel was located. This tests a support dependency, not the proposed cause of relativity's convergence.
- **12:** services mapped to facilities **before the fire**; availability fractions for **March 1–8** and **March 10–17, 2021 UTC**. Omit March 9 because the fire began March 10 local time, still March 9 UTC. Match unaffected facilities on service and backup conditions. [OVHcloud's incident record](https://corporate.ovhcloud.com/en-gb/newsroom/news/informations-site-strasbourg/) establishes the event; [RIPE timelines](https://stat.ripe.net/docs/data-api/api-endpoints/announced-prefixes) supply the limited secondary check. Whole-ASN announcements are not facility or service outcomes. Few facilities prevent routine cluster inference even with millions of servers.

### Chapter 5: instrumented electrification

Columns: `unit,employment_change,electrification_change,slope,baseline_employment,baseline_population,district`. One community per row, changes over **1996–2001**, shares expressed consistently as fractions, slope in the source's units. [Dinkelman's study](https://www.aeaweb.org/articles?id=10.1257/aer.101.7.3078) and [archive](https://doi.org/10.3886/E112474V1) identify the source; the archive returned 403. Do not mix change-in-connection-share with a project's treatment indicator without explicitly redefining the estimand.

The adapter reports first stage, reduced form, and 2SLS with baseline employment and population controls, clustered by district. It is a deliberately limited component specification, not an asserted exact replication. Slope can affect agriculture, roads, and development directly; those threats survive a strong first stage. The modern comparison does not demonstrate why the first steam engine appeared in Britain.

### Chapter 6: physical constraint checker

No input is needed to record the [Davis–Hamdan conditional bound](https://arxiv.org/abs/1503.06011): **|Δα/α| < 1.1 × 10⁻⁸**, at the source's 95% confidence level and under its restriction involving changes in the quark-mass/QCD-scale ratio.

Optional `chapter06_models.csv` contains `model,fractional_alpha_change`; its sidecar must document the predicted history and how it satisfies the physical assumptions. The script compares the absolute prediction with the bound. It does not invent model predictions, convert the bound into a Gaussian likelihood, estimate a new interval, or infer a rate without a time-dependent model. A constant can be assembled and subsequently stable. **No identified natural experiment for cosmic origins has been found.**

### Chapter 7: schooling and cognitive development

Columns: `unit,period,adoption,outcome`. Municipality is the unit; `period` is **birth cohort**, and `adoption` is the first exposed birth cohort, constant across that municipality's rows (`0` for never treated). Do not insert calendar rollout dates without converting them to exposure cohorts. Outcome is mean conscript IQ on a consistent scale and at a consistent age; document participation and migration. The [Brinch–Galloway study](https://doi.org/10.1073/pnas.1106077109) motivates the case; the administrative extract has not been obtained.

The adapter compares each treated cohort with never/not-yet-treated municipalities, using `g−1` as baseline and horizons 0–4. A `g−2` to `g−1` placebo checks an earlier contrast. It reports equal-municipality-weighted cohort effects, then nonnegative treated-municipality-weighted averages by event time. It does not use ordinary staggered TWFE. This is an unadjusted reduced-form component analysis, not the original study's IV estimate or the full Callaway–Sant'Anna estimator. Uncertainty estimation remains to be added for a specific authorized dataset. This cannot identify prehistoric genetic self-domestication.

### Chapter 8: class-size threshold

No manual input: fetches `final5.dta` and the author's Table 3 cleaning instructions from the [MIT archive](https://economics.mit.edu/people/faculty/josh-angrist/angrist-data-archive). The script subtracts 100 from scores above 100, sets scores missing when no pupils were tested, and applies the author's classroom, school-sector, and verbal-score filters.

It studies only enrollment **40/41**, centered at **40.5**, with separate local-linear slopes and triangular weights. Bandwidth **10** is primary; **5** and **15** are sensitivity analyses. Math is primary and verbal secondary. Classrooms are observations, schools are clusters. The report includes the class-size first stage, score reduced forms, disadvantage-index balance using one row per school, and counts by integer enrollment. It is not a reproduction of all of [Angrist and Lavy's tables](https://doi.org/10.1162/003355399556061). Conventional local-linear bias and discrete-running-variable concerns remain; the intervals are not robust-bias-corrected RD intervals.

### Chapter 9: wages and employment

No manual input: reads [Card's public archive](https://davidcard.berkeley.edu/data_sets/njmin.zip), using fixed-width positions in its own codebook. Employment is full-time staff plus managers plus half of part-time staff; any missing component leaves FTE missing. The source reuses sheet number 407 across states, so the composite `(state,sheet)` is the store key.

Both as-recorded complete pairs and an explicitly confirmed-permanent-closure-zero sensitivity are reported, with attrition and closure counts. Unanswered surveys and temporary closures are not silently assigned zero. A complete-pair sample may still be selected; the audit does not cure attrition bias. No confidence interval is reported from the two policy-assignment clusters. This is an employment check, not evidence for every claim about taxation, money, or institutional collapse.

### Chapter 10: maintenance and regulation

Columns: `state,date,crashes,observes_dst`, dates `YYYY-MM-DD`, counts of fatal crashes, fixed binary DST classification. Use a documented [FARS](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars) extract with genuine zero-event days distinguishable from missing coverage. [Smith's study](https://www.aeaweb.org/articles?id=10.1257/app.20140100) and [archive](https://doi.org/10.3886/E113608V1) provide the research precedent; the archive returned 403 and no daily extract is supplied.

For available years **2000–2015**, the adapter computes the correct spring transition date, compares days **−14…−1** with **+1…+14**, and computes a separate **−42…−29 versus −28…−15** placebo. Both windows balance weekdays. Complete coverage is required for every included state/window. Exclude Indiana's changing pre-2006 rules and any geographically mixed observations. Arizona includes tribal exceptions; establish homogeneous geography before labeling an aggregate non-DST. The available adapter uses raw daily counts and equal state weights; driving-exposure-adjusted estimates and stronger weather/daylight separation require additional variables. Few non-DST states mean yearly contrasts are points only. Crashes are a performance outcome, not a measure of selfhood.

### Chapter 11: AI access

Primary columns: `date,country,outcome`, daily dates **January 1–April 27, 2023**, country codes `it,fr,de,es,gb,se`. Define a developer cohort using **pre-ban activity**, freeze its denominator, and supply daily contributions per developer. Do not use quarterly GitHub counts to estimate a month-long intervention. See the [updated productivity study](https://arxiv.org/abs/2403.01964); its heterogeneous effects should not be collapsed into a universal early headline.

The primary adapter fits Italy using the fixed donor pool before **March 31**, then measures gaps through **April 27**, excluding reopening day. The last two pre-ban weeks are held out for a diagnostic fit. Country-level assignment does not permit treating developers as independent policy assignments.

The secondary adapter downloads [Tor's official daily estimates](https://metrics.torproject.org/userstats-relay-country.html), reports country-day gaps, and uses only dates observed in every country. It neither infers missing days as zero nor interpolates them. Tor's user estimates and uncertainty have measurement limitations; the synthetic-control calculation does not propagate an independent person-level sampling error. These users are neither a count of ChatGPT users nor a measure of coding productivity. The [earlier ban study](https://arxiv.org/abs/2304.09339) motivates this diagnostic, but the current implementation does not reproduce every specification.

## Estimators, validation, and remaining work

[methods.py](methods.py) implements paired changes with optional matching-set effects, clustered 2SLS, unadjusted group-time DiD, and nonnegative synthetic-control weights that sum to one. [cases.py](cases.py) handles chapter-specific cleaning and designs. [data.py](data.py) verifies cached hashes, rejects invalid downloads, and records provenance.

Synthetic-control weights use **only pre-intervention outcomes**. Reports include pre-fit error, held-out preperiod error, leave-one-donor-out gaps, and donor placebo gaps. Donor placebos are descriptive; assignment was not randomized. No placebo p-values are manufactured. Outcome-only matching can overfit or omit important predictors even when pre-fit is good.

Conventional clustered intervals require at least 20 clusters in the generic regressions; treatment comparisons additionally require more than one exposed and one unexposed cluster. These are conservative reporting screens, **not sufficient conditions for valid inference**. IV intervals additionally require first-stage clustered t² ≥10; that is a warning screen, not a weak-instrument theorem. Weak-IV-robust intervals, spatial dependence, pretrend equivalence tests, and dataset-specific sensitivity analysis remain research work where applicable.

The tests use artificial data solely to check estimator behavior: agreement with an independent 2SLS implementation, the weighted-OLS limit and covariance, known DiD arithmetic, no post-treatment leakage into synthetic weights, invalid/missing inputs, correct staggered controls, and the DST rule change. **Passing software tests does not validate identification or the book.**

To turn a component finding into evidence for the central synthesis, a further study must measure the proposed energetic driver, assembly/maintenance mediator, and productive consequences within an explicit boundary, compare rival mechanisms, and specify accessible alternatives against which a maximizing claim could fail. These scripts provide executable component tests and expose the missing links; they do not fill them by assumption.
