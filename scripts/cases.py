"""Chapter adapters: actual public inputs or explicit user-supplied data contracts."""
from __future__ import annotations

import io
import json
import re
import zipfile
from datetime import date, timedelta

import numpy as np
import pandas as pd

from data import NeedsData
from methods import finite, group_time_att, iv2sls, regression, synthetic_control, two_period


def energy(case, ctx):
    path = ctx.public("owid-energy-data.csv", "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv", "csv")
    f = pd.read_csv(path)
    output = {}
    for outcome in ("fossil_share_elec", "nuclear_share_elec"):
        panel = f.pivot(index="year", columns="country", values=outcome)
        fit, series = synthetic_control(panel, "Japan", case["donors"], range(2000, 2011), range(2011, 2016), [2009, 2010])
        fit["series"] = ctx.csv(f"chapter02_{outcome}.csv", series)
        output[outcome] = fit
    return {"status": "descriptive_comparison", "analyses": output,
            "conclusion": "Estimated mix changes relative to a fitted comparison; the compound shock and counterfactual remain identification limitations."}


def kelp(case, ctx):
    # Preserve the original matched-site design if a documented extract arrives.
    if (ctx.inputs / case["input"]).exists():
        return {"status": "conditional_effect_estimate", "analysis": two_period(ctx.local(case), case.get("controls", [])),
                "conclusion": "Matched-site comparison; assignment and exchangeability still require justification."}
    url = "https://static-content.springer.com/esm/art%3A10.1038%2Fs42003-021-01827-6/MediaObjects/42003_2021_1827_MOESM4_ESM.xlsx"
    path = ctx.public("McPherson2021_SupplementaryData.xlsx", url, "zip")
    raw = pd.read_excel(path, sheet_name="Figure 2d - Canopy Area", header=2)
    frame = raw[["Year", "Full ROI Area (km^2)"]].rename(columns={"Year":"year", "Full ROI Area (km^2)":"canopy_km2"})
    if frame.isna().any().any() or frame.year.tolist() != list(range(1985,2020)) or (frame.canopy_km2 < 0).any():
        raise ValueError("Unexpected kelp years, missing canopy data, or invalid area")
    pre = float(frame.loc[frame.year.between(2008,2012),"canopy_km2"].mean())
    post = float(frame.loc[frame.year.between(2017,2019),"canopy_km2"].mean())
    return {"status":"descriptive_outcome_only", "primary_status":"needs_comparison_data",
            "area":"Mendocino and Sonoma counties, published region of interest", "units":"km²",
            "pre_window":[2008,2012], "post_window":[2017,2019], "pre_mean":pre, "post_mean":post,
            "absolute_change":post-pre, "percent_change":100*(post/pre-1), "inference_reported":False,
            "series":ctx.csv("chapter03_kelp_canopy.csv",frame.set_index("year")),
            "conclusion":"Observed regional canopy collapse only. A single exposed regional series has no verified untreated counterfactual; it does not isolate predator loss, heat, or a maintenance mechanism."}


def class_size(case, ctx):
    p = ctx.public("final5.dta", "https://economics.mit.edu/sites/default/files/inline-files/final5.dta", "stata")
    ctx.public("AngristLavy_Table3.do", "https://economics.mit.edu/sites/default/files/inline-files/AngristLavy_Table3.do", "text")
    f = pd.read_stata(p)
    n_raw = len(f)
    for outcome, size in [("avgmath", "mathsize"), ("avgverb", "verbsize")]:
        f.loc[f[outcome].gt(100), outcome] -= 100
        f.loc[f[size].eq(0), outcome] = np.nan
    # Author Table 3 cleaning rules, including verbal-score availability.
    f = f[(f.classize > 1) & (f.classize < 45) & (f.c_size > 5)
          & f.c_leom.eq(1) & f.c_pik.lt(3) & f.avgverb.notna()].copy()
    if not f.groupby("schlcode").c_size.nunique().eq(1).all():
        raise ValueError("Inconsistent grade enrollment within school")
    output = {}
    for bandwidth in (10, 5, 15):
        local = f[(f.c_size - 40.5).abs() < bandwidth].copy()
        results = {}
        for outcome in ("avgmath", "avgverb"):
            sample = local.dropna(subset=[outcome, "classize", "c_size", "schlcode", "tipuach"])
            x = (sample.c_size - 40.5).to_numpy()
            z = (x > 0).astype(float)
            w = 1 - np.abs(x) / bandwidth
            controls = np.column_stack([np.ones(len(x)), x, x * z])
            results[outcome] = iv2sls(sample[outcome], sample.classize, controls, z,
                                    sample.schlcode.to_numpy(), weights=w)
            results[outcome]["reduced_form"] = regression(sample[outcome], np.column_stack([z, controls]),
                                                         ["threshold", "intercept", "running", "slope_change"],
                                                         sample.schlcode.to_numpy(), weights=w)
            results[outcome]["excluded_missing"] = len(local) - len(sample)
        # Balance/count checks count each school once, not once per classroom.
        schools = local.drop_duplicates("schlcode").dropna(subset=["tipuach"])
        x = (schools.c_size - 40.5).to_numpy()
        z = (x > 0).astype(float)
        results["disadvantage_balance"] = regression(schools.tipuach,
            np.column_stack([np.ones(len(x)), z, x, x * z]),
            ["intercept", "threshold", "running", "slope_change"], schools.schlcode.to_numpy(),
            weights=1 - np.abs(x) / bandwidth)
        results["schools_by_enrollment"] = {str(int(k)): int(v) for k, v in schools.c_size.value_counts().sort_index().items()}
        output[str(bandwidth)] = results
    return {"status": "conditional_effect_estimate", "raw_classrooms": n_raw,
            "classrooms_after_author_filters": len(f), "primary_bandwidth": 10,
            "cutoff": 40.5, "analyses_by_bandwidth": output,
            "conclusion": "Local first-threshold reanalysis; read first stage, balance, and bandwidth sensitivity before any causal interpretation."}


def read_card_archive(path):
    """Read field positions from the distributed codebook; no whitespace guess."""
    with zipfile.ZipFile(path) as archive:
        codebook = archive.read("codebook").decode("cp437")
        columns = re.findall(r"^([A-Z][A-Z0-9_]*)\s+(\d+)\s+(\d+)\s+\d+\.\d+", codebook, re.M)
        if len(columns) != 46:
            raise ValueError(f"Unexpected Card/Krueger codebook: {len(columns)} fields")
        f = pd.read_fwf(io.StringIO(archive.read("public.dat").decode("ascii")),
                        colspecs=[(int(a) - 1, int(b)) for _, a, b in columns],
                        names=[name.lower() for name, _, _ in columns], na_values=["."])
    # Sheet 407 occurs once in each state in the actual archive. The composite
    # key is unique; rejecting or deduplicating the sheet number would lose data.
    if len(f) != 410 or f.duplicated(["state", "sheet"]).any() or not set(f.state) <= {0, 1}:
        raise ValueError("Unexpected restaurant count, duplicate IDs, or invalid state")
    f["unit"] = f.state.astype(str) + ":" + f.sheet.astype(str)
    return f


def minimum_wage(case, ctx):
    p = ctx.public("njmin.zip", "https://davidcard.berkeley.edu/data_sets/njmin.zip", "zip")
    f = read_card_archive(p)
    f["pre"] = f.empft + f.nmgrs + .5 * f.emppt
    f["post"] = f.empft2 + f.nmgrs2 + .5 * f.emppt2
    audit = []
    for state, group in f.groupby("state"):
        audit.append({"state": "NJ" if state else "PA", "raw": len(group),
                      "missing_pre_fte": int(group.pre.isna().sum()),
                      "missing_post_fte": int(group.post.isna().sum()),
                      "status2_counts": {str(int(k)): int(v) for k, v in group.status2.value_counts().items()}})
    output = {}
    for label, permanent_zero in [("complete_pairs_as_recorded", False), ("confirmed_permanent_closures_zero", True)]:
        sample = f.copy()
        if permanent_zero:
            sample.loc[sample.status2.eq(3), "post"] = 0.
        sample = sample.dropna(subset=["pre", "post"])
        rows = []
        for period, col in [(0, "pre"), (1, "post")]:
            rows.append(pd.DataFrame({"unit": sample.unit, "period": period,
                         "outcome": sample[col], "exposure": sample.state, "cluster": sample.state}))
        fit = two_period(pd.concat(rows, ignore_index=True))
        fit["excluded_restaurants"] = len(f) - len(sample)
        fit["state_means"] = sample.groupby("state")[["pre", "post"]].mean().to_dict("index")
        fit["state_n"] = {str(int(k)): int(v) for k, v in sample.state.value_counts().items()}
        output[label] = fit
    return {"status": "descriptive_comparison", "missingness_audit": audit, "analyses": output,
            "conclusion": "Two state policy assignments: employment DiD points only; restaurant-level policy significance is not reported."}


def oklo(case, ctx):
    bound = case["published_abs_fractional_bound"]
    result = {"status": "published_constraint_only", "published_bound": bound,
              "source_confidence_level": case["confidence_level"], "new_estimation": False,
              "origin_of_constants_identified": False, "models_checked": [],
              "conclusion": "A conditional late-time stability constraint; no experiment here identifies assembled origins."}
    if (ctx.inputs / case["input"]).exists():
        models = ctx.local(case)
        finite(models.fractional_alpha_change)
        for row in models.itertuples():
            result["models_checked"].append({"model": str(row.model),
                  "fractional_alpha_change": float(row.fractional_alpha_change),
                  "within_published_bound": bool(abs(row.fractional_alpha_change) < bound)})
    return result


def electrification(case, ctx):
    f = ctx.local(case)
    if f.unit.duplicated().any():
        raise ValueError("Duplicate communities")
    controls = np.column_stack([np.ones(len(f)), f.baseline_employment, f.baseline_population])
    fit = iv2sls(f.employment_change, f.electrification_change, controls, f.slope, f.district.to_numpy())
    reduced = regression(f.employment_change, np.column_stack([f.slope, controls]),
                         ["slope", "intercept", "baseline_employment", "baseline_population"], f.district.to_numpy())
    return {"status": "conditional_effect_estimate", "iv": fit, "reduced_form": reduced,
            "conclusion": "Local IV estimate conditional on terrain exclusion, independence, and monotonicity; not first-steam-engine evidence."}


def spring_transition(year):
    month, occurrence = (4, 1) if year <= 2006 else (3, 2)
    first = date(year, month, 1)
    return pd.Timestamp(first + timedelta(days=(6 - first.weekday()) % 7 + 7 * (occurrence - 1)))


def unknown_date_bounds(records, year, event, before, after, units, point):
    lower = upper = float(point)
    treated = {u for u, exposed in units.items() if exposed}
    controls = set(units) - treated
    calendar = pd.date_range(f"{year}-01-01",f"{year}-12-31")
    rel = (calendar-event).days
    signed = np.where((rel>=after[0]) & (rel<=after[1]),1.,
                      np.where((rel>=before[0]) & (rel<=before[1]),-1.,0.))
    affected = 0
    for row in records:
        if row["year"] != year or row["state"] not in units:
            continue
        possible = np.ones(len(calendar),dtype=bool)
        if row["month"] != 99: possible &= calendar.month == row["month"]
        if row["day"] != 99: possible &= calendar.day == row["day"]
        if not possible.any(): raise ValueError("Unknown-date record has no admissible calendar date")
        factor = (1/len(treated) if row["state"] in treated else -1/len(controls))/14
        contribution = signed[possible]*factor*row["crashes"]
        lower += float(contribution.min()); upper += float(contribution.max())
        if np.any(signed[possible]): affected += int(row["crashes"])
    return {"lower":lower,"upper":upper,"potentially_relevant_unknown_date_crashes":affected,
            "note":"Accounting bounds from assigning unknown-date crashes to all compatible dates; not sampling or causal confidence intervals."}


def dst(case, ctx):
    f = ctx.local(case)
    metadata = ctx.provenance[-1]["metadata"]
    f["date"] = pd.to_datetime(f.date, format="%Y-%m-%d", errors="raise")
    if f.duplicated(["state", "date"]).any() or not set(f.observes_dst) <= {0, 1} or (f.crashes < 0).any():
        raise ValueError("Invalid daily state observations")
    if not f.groupby("state").observes_dst.nunique().eq(1).all():
        raise ValueError("Mixed/state-changing DST classifications; harmonize geography first")
    finite(f.crashes)
    output = {}
    for year in range(2000, 2016):
        event = spring_transition(year)
        year_data = f[f.date.dt.year.eq(year)].copy()
        if year_data.empty:
            continue
        year_data["relative_day"] = (year_data.date - event).dt.days
        # Two 14-day windows, each containing each weekday twice. Day 0 omitted.
        for label, before, after in [("event", (-14, -1), (1, 14)), ("placebo", (-42, -29), (-28, -15))]:
            rows = []
            for period, (start, end) in enumerate([before, after]):
                s = year_data[year_data.relative_day.between(start, end)]
                counts = s.groupby("state").size().reindex(year_data.state.unique(), fill_value=0)
                if not counts.eq(14).all():
                    raise ValueError(f"Missing daily state coverage in {year} {label}; absent days are not zeros")
                means = s.groupby("state").agg(outcome=("crashes", "mean"), exposure=("observes_dst", "first")).reset_index()
                means["unit"], means["cluster"], means["period"] = means.state, means.state, period
                rows.append(means)
            panel = pd.concat(rows, ignore_index=True)
            if not set(panel.exposure) == {0, 1}:
                raise ValueError("Need both DST and non-DST states")
            result = two_period(panel)
            # Few untreated policy groups; suppress even if generic threshold passed.
            result.pop("ci95", None)
            result.pop("standard_errors", None)
            result["inference_reported"] = False
            result["inference_note"] = "Few non-DST policy clusters; yearly point contrast only."
            if "unknown_date_counts" in metadata:
                result["unknown_date_bounds"] = unknown_date_bounds(metadata["unknown_date_counts"], year, event, before, after,
                    year_data.groupby("state").observes_dst.first().to_dict(), result["coefficients"]["exposure"])
            output[f"{year}_{label}"] = result
    if not output:
        raise ValueError("No observations in 2000–2015 study window")
    summaries = {}
    for label in ["event", "placebo"]:
        fits = [v for k,v in output.items() if k.endswith("_"+label)]
        summary = {"years":len(fits), "mean_contrast":float(np.mean([v["coefficients"]["exposure"] for v in fits]))}
        if all("unknown_date_bounds" in v for v in fits):
            summary["mean_unknown_date_bounds"] = {edge:float(np.mean([v["unknown_date_bounds"][edge] for v in fits])) for edge in ["lower","upper"]}
        summaries[label] = summary
    table = pd.DataFrame([{"comparison":key,"contrast":v["coefficients"]["exposure"]} for key,v in output.items()]).set_index("comparison")
    conclusion = "Schedule/performance component comparison; daylight, travel, weather, and sleep mechanisms are not separated."
    if abs(summaries["placebo"]["mean_contrast"]) > abs(summaries["event"]["mean_contrast"]):
        conclusion += " The earlier-window placebo is larger in absolute magnitude than the event contrast, weakening a clean causal interpretation."
    return {"status": "descriptive_comparison", "yearly_contrasts": output, "summary":summaries,
            "series":ctx.csv("chapter12_dst_contrasts.csv",table), "annual_data_audit":metadata.get("annual_audit", []),
            "conclusion": conclusion}


def country_comparison(panel, label, ctx, allow_missing=False):
    countries = ["it", "fr", "de", "es", "gb", "se"]
    calendar = pd.date_range("2023-01-01", "2023-04-27")
    panel = panel.reindex(index=calendar, columns=countries)
    missing = {c: int(panel[c].isna().sum()) for c in countries}
    if not allow_missing and panel.isna().any().any():
        raise ValueError("Primary coding panel needs all prespecified country-days; audit missingness upstream")
    complete = panel.dropna()
    omitted = [d.strftime("%Y-%m-%d") for d in panel.index.difference(complete.index)]
    pre = list(complete.index[complete.index < "2023-03-31"])
    post = list(complete.index[complete.index >= "2023-03-31"])
    validation = [d for d in pre if d >= pd.Timestamp("2023-03-17")]
    if len(pre) < 60 or len(post) < 20 or len(validation) < 7:
        raise ValueError("Insufficient common pre/post observations")
    fit, series = synthetic_control(complete, "it", countries[1:], pre, post, validation)
    fit.update(missing_by_country=missing, omitted_dates=omitted,
               missingness_policy="No interpolation or zero imputation; common observed dates only.",
               series=ctx.csv(f"chapter13_{label}.csv", series))
    return fit


def ai_access(case, ctx):
    output = {"status": "secondary_diagnostic_only", "primary_status": "needs_data"}
    if (ctx.inputs / case["input"]).exists():
        f = ctx.local(case)
        f["date"] = pd.to_datetime(f.date, format="%Y-%m-%d", errors="raise")
        if f.duplicated(["date", "country"]).any():
            raise ValueError("Duplicate primary country-days")
        output["primary_coding"] = country_comparison(f.pivot(index="date", columns="country", values="outcome"), "coding", ctx)
        output.update(status="descriptive_comparison", primary_status="comparison_available")
    rows = []
    try:
        for country in ["it", "fr", "de", "es", "gb", "se"]:
            url = f"https://metrics.torproject.org/userstats-relay-country.csv?start=2023-01-01&end=2023-05-31&country={country}&events=off"
            path = ctx.public(f"tor_{country}.csv", url, "csv")
            f = pd.read_csv(path, comment="#")
            f["date"] = pd.to_datetime(f.date, format="%Y-%m-%d", errors="raise")
            if not f.country.eq(country).all():
                raise ValueError("Unexpected Tor country code")
            rows.append(f)
        tor = pd.concat(rows)
        if tor.duplicated(["date", "country"]).any():
            raise ValueError("Duplicate Tor country-days")
        output["tor_circumvention_proxy"] = country_comparison(tor.pivot(index="date", columns="country", values="users"), "tor", ctx, allow_missing=True)
    except NeedsData as error:
        if output["primary_status"] == "needs_data":
            raise
        output["secondary_status"] = str(error)
    output["conclusion"] = "Tor is a separate circumvention proxy, not a measure of AI use, productivity, or cognition. Primary coding data are needed to test productive dependence."
    return output


def infrastructure(case, ctx):
    output = {"status": "secondary_diagnostic_only", "primary_status": "needs_data"}
    if (ctx.inputs / case["input"]).exists():
        output["primary_availability"] = two_period(ctx.local(case))
        output.update(status="conditional_effect_estimate", primary_status="comparison_available")
    url = "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS16276&starttime=2021-03-01T00:00:00&endtime=2021-03-20T00:00:00"
    try:
        path = ctx.public("ovh_prefixes.json", url, "json")
        data = json.loads(path.read_text())
        if data.get("status") != "ok":
            raise ValueError("RIPE query did not succeed")
        rows = []
        for timestamp in pd.date_range("2021-03-01T12:00:00", "2021-03-19T12:00:00"):
            active = set()
            for entry in data["data"]["prefixes"]:
                if any(pd.Timestamp(t["starttime"]) <= timestamp < pd.Timestamp(t["endtime"])
                       for t in entry["timelines"]):
                    active.add(entry["prefix"])
            rows.append({"timestamp_utc": timestamp, "announced_prefixes": len(active)})
        table = pd.DataFrame(rows).set_index("timestamp_utc")
        output["asn_diagnostic"] = {"series": ctx.csv("chapter14_bgp_prefixes.csv", table),
            "minimum_visible_prefixes": int(table.announced_prefixes.min()),
            "maximum_visible_prefixes": int(table.announced_prefixes.max()),
            "service_effect_estimated": False,
            "measurement_warning": "Provider-wide prefix visibility is neither facility treatment nor hosted-service uptime; unchanged counts cannot refute an outage."}
    except NeedsData as error:
        if output["primary_status"] == "needs_data":
            raise
        output["secondary_status"] = str(error)
    output["conclusion"] = "A network-measurement feasibility check only unless facility-mapped service data are supplied."
    return output


def run_case(case, ctx):
    adapter = case["adapter"]
    if adapter == "evidence_record":
        return {"status": case["evidence_status"], "analysis_performed": False,
                "conclusion": case["evidence_summary"]}
    if adapter == "two_period":
        fit = two_period(ctx.local(case), case.get("controls", []))
        return {"status": "conditional_effect_estimate", "analysis": fit,
                "conclusion": "Change comparison conditional on assignment, parallel trends, and documented controls; code does not establish those assumptions."}
    if adapter == "schooling":
        return {"status": "conditional_point_estimate", "analysis": group_time_att(ctx.local(case)),
                "conclusion": "Unadjusted cohort-specific contrasts; no uncertainty estimate or ancient self-domestication effect."}
    dispatch = {"kelp": kelp, "energy": energy, "class_size": class_size, "minimum_wage": minimum_wage,
                "oklo": oklo, "electrification": electrification, "dst": dst,
                "ai_access": ai_access, "infrastructure": infrastructure}
    return dispatch[adapter](case, ctx)
