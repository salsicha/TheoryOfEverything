#!/usr/bin/env python3
"""Acquire public primary data and build documented chapter analysis inputs."""
from __future__ import annotations

import argparse
import json
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from data import Context, ROOT, sha256, write_json

FARS_STATES = [1,2,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,
               27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,53,54,55,56]


def fars_daily(frame, year):
    """Count crashes on a complete calendar, after fixed geographic exclusions.

    Zero counts mean zero known-date crash records in a complete annual census.
    Unknown dates are retained separately for measurement bounds, never imputed.
    """
    f = frame.copy()
    f.columns = f.columns.str.upper()
    required = ['STATE', 'ST_CASE', 'COUNTY', 'YEAR', 'MONTH', 'DAY']
    if set(required) - set(f):
        raise ValueError('FARS accident file lacks required fields')
    if f[required].isna().any().any() or not f.YEAR.eq(year).all():
        raise ValueError('Missing accident identifiers/date fields or wrong year')
    if f.duplicated(['STATE', 'ST_CASE']).any():
        raise ValueError('Duplicate crashes would inflate daily counts')
    if set(f.STATE) != set(FARS_STATES):
        raise ValueError('Expected all 50 states and DC in the national census')
    if not f.MONTH.isin([*range(1,13),99]).all() or not f.DAY.isin([*range(1,32),99]).all():
        raise ValueError('Unexpected unknown-date coding')
    f['date'] = pd.to_datetime(f[['YEAR', 'MONTH', 'DAY']].rename(columns=str.lower), errors='coerce')
    if (f.date.isna() & f.MONTH.ne(99) & f.DAY.ne(99)).any():
        raise ValueError('Invalid known calendar date')
    audit = {'year': year, 'national_crashes': len(f), 'indiana_excluded': int(f.STATE.eq(18).sum())}
    # Exclude Indiana throughout: changing and county-dependent pre-2006 rules.
    # Exclude all AZ counties intersecting the Navajo Nation, plus unknown county.
    excluded_az = f.STATE.eq(4) & f.COUNTY.isin([0, 1, 5, 17, 999])
    audit['arizona_county_exclusions'] = int(excluded_az.sum())
    f = f[~f.STATE.eq(18) & ~excluded_az].copy()
    f['state'] = f.STATE.map(lambda v: f'{int(v):02d}')
    f.loc[f.STATE.eq(4), 'state'] = '04_excluding_001_005_017'
    unknown = f[f.date.isna()].groupby(['state','MONTH','DAY']).size().rename('crashes').reset_index()
    unknown['year'] = year
    unknown = unknown.rename(columns={'MONTH':'month','DAY':'day'})
    units = sorted(f.state.unique())
    f = f[f.date.notna()].copy()
    if len(units) != 50:
        raise ValueError('Expected 50 geographic units after excluding Indiana')
    index = pd.MultiIndex.from_product([units, pd.date_range(f'{year}-01-01',f'{year}-12-31')],names=['state','date'])
    daily = f.groupby(['state','date']).size().reindex(index,fill_value=0).rename('crashes').reset_index()
    daily['observes_dst'] = (~daily.state.isin(['15','04_excluding_001_005_017'])).astype(int)
    if daily.crashes.sum() != len(f):
        raise ValueError('Aggregation lost crashes')
    audit.update(retained_known_date_crashes=len(f), unknown_date_crashes=int(unknown.crashes.sum()), geographic_units=len(units), zero_known_date_event_days=int(daily.crashes.eq(0).sum()))
    return daily, audit, unknown


def acquire_fars(fetch, cache, inputs):
    def year_data(year):
        ctx = Context(fetch=fetch,cache=cache)
        name = f'FARS{year}NationalCSV.zip'
        url = f'https://static.nhtsa.gov/nhtsa/downloads/FARS/{year}/National/{name}'
        path = ctx.public(name,url,'zip')
        with zipfile.ZipFile(path) as archive:
            members = [n for n in archive.namelist() if Path(n).name.lower()=='accident.csv']
            if len(members)!=1:
                raise ValueError(f'Ambiguous accident file for {year}')
            with archive.open(members[0]) as stream:
                frame = pd.read_csv(stream,usecols=lambda c:c.upper() in ['STATE','ST_CASE','COUNTY','YEAR','MONTH','DAY'])
        daily,audit,unknown = fars_daily(frame,year)
        print(f'FARS {year}: {audit["national_crashes"]:,} crashes; {len(daily):,} calendar rows',flush=True)
        return daily,audit,ctx.provenance[0],unknown
    # No partial extract is written if any annual download/validation fails.
    with ThreadPoolExecutor(max_workers=4) as pool:
        annual = list(pool.map(year_data,range(2000,2016)))
    frame = pd.concat([d for d,_,_,_ in annual],ignore_index=True)
    inputs.mkdir(parents=True,exist_ok=True)
    path = inputs/'chapter10.csv'
    if path.exists():
        raise FileExistsError(f'{path} exists; choose a new --inputs directory to preserve the existing extract')
    frame.to_csv(path,index=False,date_format='%Y-%m-%d')
    meta = {
        'sources':[p for _,_,p,_ in annual],
        'construction':'Complete national ACCIDENT.csv records, 2000–2015, one row per fatal crash. Count by fixed geography and date; complete the calendar with zeros for known-date records. Retain unknown-day/month records separately without date imputation; bound their possible effect on window contrasts. Reject invalid known dates, missing identifiers, duplicate crashes, or absent states. No crash microdata are committed.',
        'coverage':'2000–2015; 48 DST geographic units and two non-DST controls: Hawaii and Arizona excluding counties 001, 005, 017, plus county unknown codes 000/999. Exclude Indiana in every year. Arizona is a partial-state aggregate, not a full-state estimate.',
        'assignment':'Spring DST transition by applicable US rule (first Sunday in April through 2006, second Sunday in March thereafter). Geography is classified by policy, not by outcomes. No random assignment; seasonal travel, weather, daylight, and control comparability remain threats.',
        'units':'Fatal crashes per geographic unit per local calendar day; not fatalities, rates per mile, or individual cognitive measurements.',
        'geography_sources':['https://www.transportation.gov/regulations/time-act', 'https://www.nist.gov/pml/time-and-frequency-division/popular-links/daylight-saving-time-dst', 'https://www.azed.gov/sites/default/files/2026/04/OIEAnnualReport_SY2023_Final%20-%20MU%20Review.pdf'],
        'annual_audit':[a for _,a,_,_ in annual],
        'unknown_date_counts':pd.concat([u for _,_,_,u in annual],ignore_index=True).to_dict('records'),
        'builder':'scripts/acquire.py','builder_sha256':sha256(__file__),
        'built_utc':datetime.now(timezone.utc).isoformat(),'output_sha256':sha256(path),
    }
    write_json(path.with_suffix('.metadata.json'),meta)
    print(f'Wrote {path} ({len(frame):,} rows)',flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chapter',choices=['10'],required=True)
    parser.add_argument('--fetch',action='store_true')
    parser.add_argument('--cache',type=Path,default=ROOT/'data')
    parser.add_argument('--inputs',type=Path,default=ROOT/'inputs')
    args=parser.parse_args()
    acquire_fars(args.fetch,args.cache,args.inputs)

if __name__=='__main__':
    main()
