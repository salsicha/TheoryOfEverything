# Could a mine pay for its next shift?

Chapter 2 imagines two crews that both reach coal. A pump rod breaks. One crew can spend earlier proceeds on a replacement. Does that access to money make it more likely to resume work? The US coal and wind records below let us observe later production and changes in the financial reward for producing. **The effect of retaining proceeds on restart remains unknown.** None of these records follows the same dollar from sale to spare part to a dated restart.

## A tax change at operating coal mines

In 2019 the US federal black-lung excise tax on eligible domestic coal sales fell from $1.10 to $0.50 per ton underground and from $0.55 to $0.25 at the surface. The sales-price cap fell from 4.4% to 2%. For eligible domestic sales at the full per-ton rates, underground coal received 30 cents more statutory relief per ton than surface coal. Both rates fell. Coal prices, export sales and contracts affect the benefit to each operator. The data leave actual relief and the cash retained at each mine unknown. [IRS Form 720 for 2019](https://www.irs.gov/pub/irs-prior/f720--2019.pdf) · [GAO testimony on the coal tax](https://www.gao.gov/assets/gao-22-105546.pdf)

Using five EIA workbooks, we selected mines classified as active with positive output from one extraction method in the prior year, in Appalachian areas excluding Pennsylvania anthracite. We followed each MSHA mine identifier into the next calendar year and looked for positive output from either underground or surface extraction. The comparison gives each of the 26 state/county areas with both methods in all four cohorts equal weight. The percentages are county averages. The counts are individual mines. [EIA mine production data](https://www.eia.gov/coal/data.php) · [Annual results and source fingerprints](../scripts/results/two_mines.json)

| Production year | Underground positive / baseline | Surface positive / baseline | County-weighted rates, underground / surface | Gap, percentage points |
| --- | ---: | ---: | ---: | ---: |
| 2016 | 95 / 96 | 129 / 139 | 98.08% / 95.14% | +2.93 |
| 2017 | 114 / 114 | 143 / 151 | 100.00% / 97.68% | +2.32 |
| 2018 | 123 / 123 | 153 / 155 | 100.00% / 99.24% | +0.76 |
| 2019 | 125 / 125 | 146 / 153 | 100.00% / 96.12% | +3.88 |

The gap in **recorded** continuation widened by **3.11 percentage points** in 2019. Underground continuation was already at 100%. The surface cohort had seven missing follow-up records in 2019 and two in 2018. No explicit zero accounted for either shortfall. Allowing each missing mine either outcome puts the change in the gap between **−0.76 and +3.88 points**. These are bounds on actual continuation given missing records. The earlier changes in the recorded gap were −0.62 and −1.55 points.

Leaving out one area at a time gives +2.44 to +3.81 points. Also matching initial size above or below 100,000 tons leaves 25 county/size cells and reduces the change to +1.00 point, with missing-outcome bounds of −1.33 to +2.33. Including producing mines of any baseline status yields +2.38 points across 38 areas and much wider bounds of −26.33 to +28.72. One national policy change, nonrandom mining methods, and changing power and export demand prevent treating the gap as a causal estimate. There is no independent series of policy assignments from which to estimate policy-level sampling uncertainty.

## Did a stopped mine resume?

**Annual records.** We followed previously producing mines through a full calendar year with an explicit zero-ton underground or surface record and then looked for positive output the next year. In the 2015–17 window one mine of each method reported zero in the middle year. They were in different areas, and both again reported zero in 2017. The windows ending in 2018 and 2019 contained no qualifying zero-year mines. Of three surface mines absent from the 2018 conventional-production records, one reappeared with production in 2019. Its missing year leaves the interruption unknown. This design supplies no comparison of restart rates under the tax cut. [Annual restart results](../scripts/results/two_mines_restart.json)

**Dated incidents.** MSHA records certain unplanned liquid or gas inundations and damage to shaft or slope hoists. We linked these notifications to previously active Appalachian mines that had produced in the preceding quarter, then examined incidents in January–September to keep the next quarter in the same tax year. Multiple reports from a mine in a quarter count as one incident-quarter. We found **28 in 2017, 24 in 2018 and 23 in 2019**. The corresponding numbers of distinct mines were 14, 13 and 12. All 75 incident-quarters were at underground mines. Every one recorded positive production both during the incident quarter and in the following quarter. [Linked observations and source fingerprints](../scripts/results/two_mines_events.json) · [MSHA reporting definitions](https://arlweb.msha.gov/codeaphone/Immediately%20Reportable%20Accidents%20and%20Injuries.pdf)

One working section can keep producing while another is down. A qualifying hoist incident can interrupt use of the hoist for as little as just over 30 minutes. The two files supply an incident date and quarterly tonnage. The field for return to work dates the injured worker’s return. Neither file dates a repaired pump’s first shift. A direct test would link work orders to shift logs, identify the original source of repair funds and compare otherwise similar faults exposed to a change in control of those funds. [Accident fields](https://arlweb.msha.gov/OpenGovernmentData/DataSets/Accidents_Definition_File.txt) · [Quarterly production fields](https://arlweb.msha.gov/OpenGovernmentData/DataSets/MineSProdQuarterly_Definition_File.txt)

## A comparison at wind plants

A US wind plant eligible for the federal production credit could earn it during the ten years beginning when the facility entered service. That offers a dated change in the reward for producing electricity at equipment already in service. Hamilton and colleagues published a plant-month dataset on US wind generation. Its recorded first generation supplies an approximate tenth birthday. The panel does not identify tax recipients or the amount retained at each site. [IRS credit instructions](https://www.irs.gov/instructions/i8835) · [Hamilton and colleagues, Berkeley Lab](https://eta.lbl.gov/publications/how-does-wind-project-performance)

We followed the **same 68 plants** reporting continuously at ages eight through eleven. Each comparison uses 12 months on either side of the stated birthday, or 1,632 plant-months. Capacity factor measures actual net generation as a percentage of what continuous operation at rated power could supply. The analysis accounts for modeled wind conditions, persistent plant differences and conditions shared in each calendar month. Each plant-month gets equal weight. [Wind results, estimates and intervals](../scripts/results/two_mines_wind.json)

| Birthday | Observed mean before / after | Adjusted change, percentage points | 95% interval, clustered by plant |
| --- | ---: | ---: | ---: |
| Ninth | 32.32% / 31.99% | +1.21 | −1.62 to +4.04 |
| Tenth | 31.99% / 30.92% | +0.96 | −2.43 to +4.35 |
| Eleventh | 30.92% / 29.89% | +0.99 | −1.10 to +3.08 |

At ten years the observed decline was 1.08 points. Adjusting for wind and plant alone gives −1.48 points (−3.05 to +0.08). Adding calendar-month effects changes the sign. Adjusting the outcome for curtailment as well gives +1.12 points (−2.22 to +4.47). The ninth and eleventh birthdays show similar adjusted changes. There is little evidence for a distinct age-ten break in this short-window comparison. Plants that stopped reporting before age twelve are outside its scope.

The authors asked a different question over a wider age window. Repeating their notebook’s specification with curtailment-adjusted output, plant and wind controls, 103 plants, and 6,051 observations from age seven through exactly twelve yields **−1.16 capacity-factor points** (our plant-clustered interval −2.14 to −0.18). Their paper expresses the decline relative to baseline generation, about 3.6%. A broad post-ten difference and a local change at a birthday need not agree. Regional conditions, warranties, dispatch and repowering remain alternative explanations. The records contain neither maintenance expenditure nor repair dates. [Paper](https://doi.org/10.1016/j.joule.2020.04.005) · [Authors’ data and analysis](https://drive.google.com/drive/folders/1MwKfsrPkeaf4I43ydZIK936vQW5Pbf4U)

## A historical lead

West Germany’s 1960s closure premiums reached owners whose other coal mines continued operating. Kai Fischer’s mine-level working paper relates larger net payments per remaining tonne to increased output and machinery at those surviving mines. The study reports changes in water management as well. Firms chose which mines to close, and cash could reach a sister mine or shareholders. This provides historical evidence of a route from funds to equipment, with its own selection and reallocation problems. Cornwall’s duty reports supply a different observation, the lift obtained per bushel. Neither source links a particular broken rod to payment and resumption. [Fischer, table 2 and figure 17](https://www.cerge-ei.cz/pdf/events/papers/Paper_20241031.pdf) · [Cornish records in S146](sources.md#s146)

## Reproduce the US comparisons

Use the Python environment in the [research guide](../scripts/README.md#run). The annual comparison verifies the five EIA workbooks. The wind comparison verifies the Berkeley Lab panel. Download the two public MSHA archives into the local data directory for the incident check. The incident result records the fingerprints of the specific snapshots used because the agency updates its files. [Accidents archive](https://arlweb.msha.gov/OpenGovernmentData/DataSets/Accidents.zip) · [Quarterly production archive](https://arlweb.msha.gov/OpenGovernmentData/DataSets/MinesProdQuarterly.zip)

```sh
.venv/bin/python scripts/two_mines.py --fetch
.venv/bin/python scripts/two_mines_restart.py
.venv/bin/python scripts/two_mines_events.py --accidents scripts/data/Accidents.zip --production scripts/data/MinesProdQuarterly.zip
.venv/bin/python scripts/two_mines_wind.py
```
