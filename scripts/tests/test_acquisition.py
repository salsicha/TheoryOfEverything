"""Validate primary-data transformations with artificial records, not empirical evidence."""
import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from acquire import FARS_STATES, fars_daily
from cases import unknown_date_bounds


class AcquisitionTests(unittest.TestCase):
    def census(self):
        return pd.DataFrame([dict(STATE=s,ST_CASE=s*1000,COUNTY=3,YEAR=2000,MONTH=1,DAY=1) for s in FARS_STATES])

    def test_zero_calendar_unknown_dates_and_fixed_exclusions(self):
        frame=self.census()
        frame=pd.concat([frame,pd.DataFrame([
            dict(STATE=1,ST_CASE=1001,COUNTY=3,YEAR=2000,MONTH=4,DAY=99),
            dict(STATE=4,ST_CASE=4001,COUNTY=1,YEAR=2000,MONTH=1,DAY=1)])],ignore_index=True)
        daily,audit,unknown=fars_daily(frame,2000)
        self.assertEqual(len(daily),50*366)
        self.assertEqual(daily.crashes.sum(),50)
        self.assertEqual(unknown.crashes.sum(),1)
        self.assertEqual(audit['arizona_county_exclusions'],1)
        self.assertEqual(audit['indiana_excluded'],1)
        self.assertNotIn('18',daily.state.unique())
        self.assertEqual(daily.loc[daily.date.eq('2000-01-02'),'crashes'].sum(),0)
        self.assertEqual(daily.groupby('state').observes_dst.first().sum(),48)

    def test_incomplete_census_and_invalid_known_dates_fail(self):
        with self.assertRaisesRegex(ValueError,'all 50 states'):
            fars_daily(self.census().iloc[1:],2000)
        frame=self.census();frame.loc[0,['MONTH','DAY']]=[2,31]
        with self.assertRaisesRegex(ValueError,'Invalid known'):
            fars_daily(frame,2000)

    def test_unknown_date_bounds_preserve_all_possible_assignments(self):
        rows=[dict(year=2000,state='01',month=4,day=99,crashes=2)]
        bound=unknown_date_bounds(rows,2000,pd.Timestamp('2000-04-02'),(-14,-1),(1,14),{'01':1,'15':0},0.)
        self.assertAlmostEqual(bound['lower'],-2/14)
        self.assertAlmostEqual(bound['upper'],2/14)
        self.assertEqual(bound['potentially_relevant_unknown_date_crashes'],2)

if __name__=='__main__':unittest.main()
