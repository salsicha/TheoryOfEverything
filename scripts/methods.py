"""Small, auditable estimators. Identification assumptions live in experiments.json.

No function converts a fit, a placebo rank, or a historical event into a causal
claim. Synthetic-control placebos are descriptive; few policy clusters do not
acquire valid inference by counting individual observations as assignments.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import t as student_t
import statsmodels.api as sm


def finite(*arrays):
    for a in arrays:
        if not np.isfinite(np.asarray(a, dtype=float)).all():
            raise ValueError("Missing or nonfinite numeric values; select/report exclusions first")


def full_rank(a):
    if np.linalg.matrix_rank(a) < a.shape[1]:
        raise ValueError("Rank-deficient design; the requested coefficient is not identified")


def regression(y, x, names, clusters=None, weights=None, inference=True):
    y, x = np.asarray(y, float), np.asarray(x, float)
    finite(y, x)
    full_rank(x)
    if len(y) <= x.shape[1]:
        raise ValueError("Insufficient residual degrees of freedom")
    weights = np.ones(len(y)) if weights is None else np.asarray(weights, float)
    finite(weights)
    if (weights <= 0).any():
        raise ValueError("Weights must be strictly positive")
    g = len(np.unique(clusters)) if clusters is not None else None
    fit = sm.WLS(y, x, weights=weights).fit()
    # 20 is a conservative reporting rule, not a theorem about adequate clusters.
    inference = bool(inference and (g is None or g >= 20))
    out = {"n": len(y), "clusters": g, "inference_reported": inference,
           "coefficients": dict(zip(names, map(float, fit.params)))}
    if inference:
        if clusters is None:
            fit = fit.get_robustcov_results(cov_type="HC1", use_t=True)
        else:
            fit = fit.get_robustcov_results(cov_type="cluster", groups=clusters,
                                          use_correction=True, use_t=True)
        out["standard_errors"] = dict(zip(names, map(float, fit.bse)))
        out["ci95"] = dict(zip(names, fit.conf_int().tolist()))
    else:
        out["inference_note"] = "Point estimates only; assignment-level inference is unavailable or suppressed."
    return out


def iv2sls(y, treatment, exogenous, instrument, clusters, weights=None):
    """One endogenous regressor / one excluded instrument; cluster sandwich.

    WLS is implemented by transforming *all* variables with sqrt(weight).
    Xhat = projection of X on Z. Scores are Xhat_i * structural residual_i.
    Wald intervals are suppressed with <20 clusters or first-stage t^2 <10.
    That threshold is only a warning screen; passing it does not prove strong IV.
    """
    y, d, c, z = map(lambda a: np.asarray(a, float),
                    (y, treatment, exogenous, instrument))
    finite(y, d, c, z)
    x, instruments = np.column_stack([d, c]), np.column_stack([z, c])
    w = np.ones(len(y)) if weights is None else np.asarray(weights, float)
    finite(w)
    if (w <= 0).any():
        raise ValueError("Weights must be positive")
    root = np.sqrt(w)
    xw, zw, yw = x * root[:, None], instruments * root[:, None], y * root
    full_rank(zw)
    xhat = zw @ np.linalg.lstsq(zw, xw, rcond=None)[0]
    full_rank(xhat)
    bread = np.linalg.inv(xhat.T @ xw)
    beta = bread @ (xhat.T @ yw)
    resid = yw - xw @ beta
    labels, idx = np.unique(clusters, return_inverse=True)
    g, n, k = len(labels), len(y), x.shape[1]
    if n <= k or g < 2:
        raise ValueError("IV needs residual degrees of freedom and >=2 independent clusters")
    scores = np.zeros((g, k))
    np.add.at(scores, idx, xhat * resid[:, None])
    cov = bread @ (scores.T @ scores) @ bread.T * g / (g - 1) * (n - 1) / (n - k)
    se = float(np.sqrt(max(cov[0, 0], 0)))
    first = regression(d, instruments, ["instrument"] + [f"control_{i}" for i in range(c.shape[1])],
                       clusters=clusters, weights=w)
    first_se = first.get("standard_errors", {}).get("instrument")
    f = (first["coefficients"]["instrument"] / first_se) ** 2 if first_se and first_se > 0 else None
    out = {"n": n, "clusters": g, "effect_per_unit_treatment": float(beta[0]),
           "first_stage": first, "first_stage_cluster_t_squared": f,
           "inference_reported": bool(g >= 20 and f is not None and f >= 10),
           "inference_note": "Conventional cluster Wald inference, conditional on IV assumptions; t^2>=10 is not a weak-IV guarantee."}
    if out["inference_reported"]:
        q = student_t.ppf(.975, g - 1)
        out.update(standard_error=se, ci95=[float(beta[0] - q * se), float(beta[0] + q * se)])
    else:
        out["inference_note"] = "Wald interval suppressed: few clusters or weak/undetermined first stage. No weak-IV-robust interval implemented."
    return out


def two_period(frame, controls=()):
    """Unit changes regressed on fixed exposure; optional matching-set FE.

    period must be 0/1, not calendar years. Outcome is the unit's mean in the
    predeclared window. Each unit gets equal weight. Attrition is an error, not
    an invitation to silently select a complete-case causal sample.
    """
    required = ["unit", "period", "outcome", "exposure", "cluster", *controls]
    f = frame[required + (["stratum"] if "stratum" in frame else [])].copy()
    if f.isna().any().any() or f.duplicated(["unit", "period"]).any():
        raise ValueError("Missing values or duplicate unit-period observations")
    if set(f.period) != {0, 1} or not f.groupby("unit").period.nunique().eq(2).all():
        raise ValueError("Every unit needs both periods 0 and 1; report attrition upstream")
    for col in ["exposure", "cluster", *controls, *(["stratum"] if "stratum" in f else [])]:
        if not f.groupby("unit")[col].nunique().eq(1).all():
            raise ValueError(f"{col} must be fixed within unit")
    pre, post = (f[f.period.eq(p)].set_index("unit").sort_index() for p in (0, 1))
    delta = post.outcome - pre.outcome
    x = pd.DataFrame({"intercept": 1., "exposure": pre.exposure}, index=pre.index)
    for col in controls:
        x[col] = pre[col]
    if "stratum" in pre:
        x = pd.concat([x, pd.get_dummies(pre.stratum, prefix="stratum", drop_first=True, dtype=float)], axis=1)
    # A single treated policy assignment does not support conventional cluster inference.
    cluster_exposure = pre.groupby("cluster").exposure.agg(["min", "max"])
    g_t = int((cluster_exposure["max"] > 0).sum())
    g_c = int((cluster_exposure["min"] == 0).sum())
    result = regression(delta, x, list(x.columns), pre.cluster.to_numpy(),
                        inference=(g_t >= 2 and g_c >= 2))
    result.update(treated_clusters=g_t, zero_exposure_clusters=g_c,
                  mean_pre=float(pre.outcome.mean()), mean_post=float(post.outcome.mean()))
    return result


def group_time_att(frame, horizon=4):
    """Unadjusted group-time DiD with never/not-yet-treated controls.

    Uses g-1 as baseline; placebo contrasts compare g-2 with g-1. No already
    treated controls, no TWFE, no claim to replicate covariate-adjusted C&S.
    Cohort weights are nonnegative. This adapter reports points, not intervals.
    """
    f = frame[["unit", "period", "adoption", "outcome"]].copy()
    if f.isna().any().any() or f.duplicated(["unit", "period"]).any():
        raise ValueError("Missing or duplicate unit-period observations")
    finite(f.period, f.adoption, f.outcome)
    if not f.groupby("unit").adoption.nunique().eq(1).all():
        raise ValueError("Adoption cohort must be fixed within municipality")
    adoption = f.groupby("unit").adoption.first()
    wide = f.pivot(index="unit", columns="period", values="outcome")
    rows = []
    for g in sorted(adoption[adoption.gt(0)].unique()):
        for event in [-1, *range(horizon + 1)]:
            baseline, end = (g - 2, g - 1) if event == -1 else (g - 1, g + event)
            if baseline not in wide or end not in wide:
                continue
            treated = adoption.eq(g)
            control = adoption.eq(0) | adoption.gt(max(g, end))
            eligible = treated | control
            pair = wide.loc[eligible, [baseline, end]]
            if pair.isna().any().any():
                raise ValueError("Unbalanced municipality pairs; specify and audit attrition before analysis")
            change = wide[end] - wide[baseline]
            if treated.sum() and control.sum():
                rows.append({"cohort": float(g), "event": event, "treated_units": int(treated.sum()),
                             "control_units": int(control.sum()),
                             "att": float(change[treated].mean() - change[control].mean())})
    if not rows:
        raise ValueError("No identified cohort-time comparisons")
    effects = pd.DataFrame(rows)
    average = {str(int(e)): float(np.average(s.att, weights=s.treated_units))
               for e, s in effects.groupby("event")}
    return {"group_time": rows, "weighted_by_event": average, "inference_reported": False,
            "note": "Unadjusted group-time points, conditional on no anticipation and parallel trends; no uncertainty estimate implemented."}


def synth_weights(treated, donors):
    y, x = np.asarray(treated, float), np.asarray(donors, float)
    finite(y, x)
    if x.ndim != 2 or len(y) != len(x) or x.shape[1] < 2 or len(y) < 4:
        raise ValueError("Synthetic control requires >=4 preperiods and >=2 donors")
    # Center using sum(weights)=1 and scale the *whole* quadratic. Scaling by
    # treated variance alone is unstable for a near-constant placebo series.
    differences = x - y[:, None]
    a = differences / max(float(np.abs(differences).max()), 1.)
    hessian_half = a.T @ a / len(y)
    fit = minimize(lambda w: float(w @ hessian_half @ w),
                   np.ones(x.shape[1]) / x.shape[1],
                   jac=lambda w: 2 * hessian_half @ w,
                   bounds=[(0., 1.)] * x.shape[1],
                   constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1,
                                 "jac": lambda w: np.ones(len(w))}],
                   method="SLSQP", options={"ftol": 1e-12, "maxiter": 5000})
    if not fit.success or abs(fit.x.sum() - 1) > 1e-7:
        raise ValueError(f"Synthetic control optimizer failed: {fit.message}")
    return fit.x


def synthetic_control(panel, treated, donors, pre, post, validation=()):
    """Fit only pre-treatment data; keep prespecified dates/donors unchanged.

    No p-values: donor assignment is not random. Placebo gaps and RMSPE ratios
    are diagnostics, and poor-fit comparisons must not be treated as evidence.
    """
    panel = panel.sort_index()
    pre, post, validation = list(pre), list(post), list(validation)
    if set(pre) & set(post) or not set(validation).issubset(pre):
        raise ValueError("Pre/post overlap or validation outside preperiod")
    if treated in donors or len(set(donors)) != len(donors):
        raise ValueError("Donors must be unique and exclude the treated unit")
    selected = panel.loc[pre + post, [treated, *donors]]
    finite(selected)
    y0, x0 = panel.loc[pre, treated], panel.loc[pre, donors]
    w = synth_weights(y0, x0)
    series = panel.loc[pre + post, [treated]].copy()
    series["synthetic"] = panel.loc[pre + post, donors].to_numpy() @ w
    series["gap"] = series[treated] - series.synthetic
    rms = lambda a: float(np.sqrt(np.mean(np.asarray(a) ** 2)))
    out = {"weights": dict(zip(donors, map(float, w))),
           "pre_rmspe": rms(series.loc[pre, "gap"]),
           "post_mean_gap": float(series.loc[post, "gap"].mean()),
           "post_rmspe": rms(series.loc[post, "gap"]), "n_pre": len(pre), "n_post": len(post),
           "inference_reported": False, "note": "Descriptive synthetic-control comparison; no random-assignment p-value."}
    if validation:
        train = [p for p in pre if p not in validation]
        wv = synth_weights(panel.loc[train, treated], panel.loc[train, donors])
        out["heldout_pre_rmspe"] = rms(panel.loc[validation, treated] - panel.loc[validation, donors].to_numpy() @ wv)
    leave_out = {}
    if len(donors) > 2:
        for excluded in donors:
            remaining = [d for d in donors if d != excluded]
            wl = synth_weights(y0, panel.loc[pre, remaining])
            leave_out[excluded] = float((panel.loc[post, treated] - panel.loc[post, remaining].to_numpy() @ wl).mean())
    out["leave_one_donor_out_post_gaps"] = leave_out
    placebos = []
    for pseudo in donors:
        remaining = [d for d in donors if d != pseudo]
        if len(remaining) < 2:
            continue
        wp = synth_weights(panel.loc[pre, pseudo], panel.loc[pre, remaining])
        e0 = panel.loc[pre, pseudo] - panel.loc[pre, remaining].to_numpy() @ wp
        e1 = panel.loc[post, pseudo] - panel.loc[post, remaining].to_numpy() @ wp
        r0, r1 = rms(e0), rms(e1)
        placebos.append({"unit": pseudo, "pre_rmspe": r0, "post_rmspe": r1,
                         "post_mean_gap": float(e1.mean()), "rmspe_ratio": r1 / r0 if r0 > 1e-8 else None})
    out["donor_placebos_descriptive"] = placebos
    return out, series
