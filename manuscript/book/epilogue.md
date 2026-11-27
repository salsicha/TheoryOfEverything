# Epilogue — From Cybernetics to AI and Data Centers

The water leaving the data center in Mäntsälä, Finland, was too cool for the town’s heating pipes. Air from the servers had warmed it to about 35–40 degrees Celsius. Nivos, the local utility, needed 55–60. In January 2016 it bought 331 megawatt-hours of electricity to run a heat pump across that gap. A meter at the center’s heat-recovery connection registered 663 megawatt-hours from the site. Another, on the town side of the pump, registered 1,042 megawatt-hours delivered to the network.[1]

Yandex had chosen Mäntsälä for its fiber connections, road access and cold air. Nivos found a use for some of the heat the company paid to remove. That January the data center used 3,411 megawatt-hours of electricity. Spread over the month, that much electrical work dissipating as heat comes to about 4.58 megawatts, day and night. The measured share recovered from the site averaged 0.89 megawatts. The other heat went elsewhere.[1]

In 2025 the world’s data centers used an estimated **485 terawatt-hours** of electricity, an average draw of about **55 gigawatts**. The International Energy Agency put the year’s growth at 17 percent for all data centers and **50 percent** for those focused on AI. Nearly all the electrical work consumed on site ends up as heat. In Mäntsälä the heat meter records how much the town can use.[1]

## The machines people could build

In 1943 Arturo Rosenblueth, Norbert Wiener and Julian Bigelow followed a feedback signal through a simpler movement, a hand bringing a glass to the mouth. A correction that arrived late or went too far could spill the water. In 1948 Wiener called the wider study of control and communication *cybernetics*. The same questions apply to a cooling plant. Which temperature does it measure, and can it act before that reading goes out of date?[2]

Darwin noticed that observations against his theory were the ones he tended to forget. He made a practice of writing them down while he still remembered them. A mind observing how its own memory works, then using that observation to change how it works next time, illustrates the book’s definition of intelligence as a hierarchical and recursive self-modeling system. A thermostat can respond to a change in temperature long before anything in it can represent why its own reading went wrong.[12]

In 1955 John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon proposed a summer project on *artificial intelligence*. Their questions included language, abstraction and neural networks. A programmer writing rules for recognizing an object and a programmer training a network could apply under the same name. To train a network took examples, a way of scoring errors and machines able to adjust many connections.[2][3]

Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton had labeled images and graphics processors that could do many similar operations at once. In Toronto their network would not fit on one card. They split the work across two and restricted where the halves exchanged information. In the 2012 ImageNet competition their winning entry missed the correct label among its first five guesses on 15.3 percent of the images. The next team missed on 26.2 percent.[3]

At Google in 2013 engineers estimated the cost of running speech recognition on the processors they already owned. If people used neural voice search for three minutes a day, the company projected that it would need roughly double its data-center capacity. Google could buy more general-purpose machines or build a chip for the arithmetic its speech recognizer kept repeating. Norman Jouppi and his colleagues describe the chip they built. It plugged into existing servers and was serving requests by 2015.[4]

In the later TPU v4 system, a chip could finish its share of a calculation and still have to wait for another chip’s result. Operators could change the connections among 4,096 chips. Small mirrors in optical switches redirected the signals. The same chips, still in their racks, could exchange results along paths better suited to the job.[4]

Training consumes power while a network learns from examples. A trained model still needs a request or another trigger before it does more work. At inference, sampling and checking extra answers costs time and electricity, sometimes for no better answer. A service that pays for its chips and power can support another installation. A system that pursues purposes of its own has a further job, to set those purposes, model its progress and correct its course.[4][5]

At another data center, operator Dan Fuenffinger saw a controller turn the cooling water temperature down. That usually cost power. In winter the plant could use cold air from outside, and the lower setting saved electricity. Operators had spent enough of their shifts carrying out the program’s suggestions that they asked to let it make adjustments. The new controller received readings every five minutes. Operators could take over.[6]

The company compared electricity per unit of cooling with its historical baseline. Its reported saving grew from about twelve percent to about thirty percent over nine months. A customer waiting for space in a rack could put the freed watts to work. Without that customer the saving could lower demand at the power station.[6]

The mine at Saltom could keep burning coal under the pump because buyers wanted the coal it brought up. In Mäntsälä the utility could earn money supplying server heat even when nobody buying heat wanted a computation.[1]

## From bare rock to a building full of computers

At the Apollo 15 landing site, astronauts put probes into the lunar soil. Heat from the Moon’s interior was crossing each square meter at about 21 milliwatts. At that local rate it would take roughly **220 square kilometers** of ground to carry the power drawn by the Finnish building. The Sun heats the lunar surface by day and the surface radiates to space. The probes isolated a smaller current that keeps coming up from below even through the lunar night.[7]

Beneath the ocean floor, microbes draw on chemical energy in buried organic matter. James Bradley and his colleagues estimated a median power of **1.5 × 10⁻²⁰ watts** per methane-producing cell there. These are living cells under modern conditions, a comparison for an early metabolism. Across the ocean sediments in the worldwide study, three forms of metabolism together used an estimated **37.3 gigawatts**, equivalent to some **8,100** buildings drawing power at the Mäntsälä rate. Reproduction can give even such a small reaction current a planetary reach.[8]

Antoine Lavoisier and Pierre-Simon Laplace put a guinea pig in a cotton-lined basket and measured the ice it melted. After five hours and thirty-six minutes they removed the animal, let the basket cool and collected the water. They repeated the trial with the same guinea pig. Their weighings gave about 400 grams of ice melted in ten hours, or **3.7 watts** of heat from the animal in the apparatus. At that rate it would take about **1.2 million** guinea pigs to match the Finnish building.[1][9]

On Béchervaise Island in East Antarctica, Adélie penguins bring fish and krill back to their chicks. Darren Southwell and his colleagues used thirteen years of records to estimate how much food the colony needed. Averaged over the breeding season, the food eaten by its 1,836 breeding pairs supplied about **190 kilowatts**. It would take about twenty-four colonies feeding at that rate to match the power entering the Finnish building.[1][9]

In Paul Warde’s account of England and Wales in 1560, feeding draught animals supplied about as much energy as burning firewood. Food, fodder, wood, coal, wind and water together supplied an average of **2.0 gigawatts**. By 1950 the same territory used **194 gigawatts**, about 166 from coal alone. Total use rose almost a hundredfold and use per person sevenfold. A farm had to grow another crop to feed its teams. A mine with a pump and a railway could send out fuel accumulated over geological time.[10]

How much entropy did these flows produce? A watt tells us how much energy moves each second. Its effect depends on the form in which it arrives and where it ends up. If 4.58 megawatts of heat pass from rock at 320 kelvins to rock at 300, the transfer produces **955 watts per kelvin** of entropy. If the same power arrives as electricity and the computers dissipate it into surroundings at 300 kelvins, the rate is **15,300 watts per kelvin**. Electricity can do work before it becomes heat. A patch of ground supplied with both the original heat current and the additional electricity would produce about **16,200 watts per kelvin** through those two processes.[7]

Each row gives the entropy produced per second by the named process, using the listed assumptions. For England and Wales it counts coal at the same temperatures in both years. The last column applies a single comparison to all six cases. If the listed power crossed the same 20-degree temperature drop as heat, what entropy would that transfer produce? The two columns are alternative estimates.[7][8][9][10]

| Example and power | Process counted | Entropy rate (W/K) | Same heat transfer, 320 to 300 K (W/K) |
| --- | --- | ---: | ---: |
| Lifeless rock · 210 W from the interior under one hectare at the Apollo 15 rate | Heat conducted from 320 to 300 K | 0.044 | 0.044 |
| Microbial life · 1.5 × 10⁻²⁰ W in one methane-producing cell | Chemical free energy fully dissipated at 300 K | 5.0 × 10⁻²³ | 3.1 × 10⁻²⁴ |
| Animal life · 3.7 W from one guinea pig | Body heat passing from about 310 K to melting ice at 273 K | 0.0016 | 0.00078 |
| Pre-industrial England and Wales · 200 MW from coal in 1560 | Coal heat passing from 1,000 to 300 K | 470,000 | 42,000 |
| Twentieth-century England and Wales · 166 GW from coal in 1950 | Coal heat passing from 1,000 to 300 K | 390 million | 35 million |
| Mäntsälä data center · 4.58 MW of electricity in January 2016 | Electrical work fully dissipated at 300 K | 15,300 | 955 |

One Finnish building drew as much power as the share of about 7,200 people in the farms, workshops and households of 1560. About 440 such buildings would match the territory’s entire energy use that year and about 42,000 would match it in 1950. At the specified temperatures, the entropy produced by the coal heat alone rose more than eight hundredfold. In 2025 the world’s data centers drew about 27 times the entire 1560 supply of England and Wales and just over a quarter of its 1950 supply.[1][10]

Give a rack of computers and a bank of resistors equal power and let both dissipate it at the same temperature. They tie. An order for another computation could pay for more chips and help finance a generator. If the generator runs, another flow of electricity begins. The claim that AI maximizes the rate of entropy production turns on how much power this sequence and its rivals could bring into use over the same years. A signed order, a new grid connection and a meter reading can date those steps.[1][4][6][7]

On an oversubscribed grid a new connection may simply displace another user. Heat sold to homes may also displace fuel in a boiler. Count the alternative uses, the equipment and the displaced fuel over the same years. A growing order book and a utility’s connection schedule then offer a forecast someone could make before reading the meter.[1][4][6][7]

In Chapter 2, one five in a Sudoku column settled both gaps in a row. In Toronto a memory limit ruled out a single-card machine before anyone ran the network. Google’s voice-search forecast made a chip worth building, and a town with a use for warm water made a heat pump worth running. These are choices along the funnel that produced AI. Each has a constraint one could have named before learning the outcome.[1][3][4]

## What a dark data center could leave behind

The meter in Finland gives a measure of the difference between a connected site and a useful load. In July the site drew 4,034 megawatt-hours of electricity and sent 476 megawatt-hours of heat through the recovery connection. In January it drew less electricity and sent the town 663 megawatt-hours of heat. A nearby customer, a pipe and the season changed how much of the output another system could use.[1][11]

AI is a dissipative system at the scale of the running service. A request can set many processors to work, and keeping them within their temperature limits means carrying away heat. The demand paying for another rack can increase the rate at which electricity passes through the site. When the demand stops, an idle rack cannot stand in for the production of entropy measured while it was busy. A whole-system claim must count competing loads and displaced fuels as well.[1][4][6]

The dot-com crash left a distinction worth making in the next investment boom. A strand of dark fiber could wait for new equipment. A chip bought for a particular model may have little use by the time a second buyer appears. An energized substation, a fiber route, a building and a cooling connection could still save a later operator years of work. The question is which of those assets its next use requires, and what a tenant must spend to make them work together. That is a prediction about reuse, open to a later reading of the lease, the equipment list and the power meter.[1][13]

In Mäntsälä the town had a use for warm water as well as the company having a use for computation. If a hall goes dark and a new enterprise lights it again, the first operator will have helped determine what the second can build there. The power drawn on the first day of its new use will tell us when that inheritance became an operating system again.

## Notes

1. Laine and colleagues give separate electricity, recovered heat, pump electricity and heat-delivery records in table 3. January had 744 hours. The IEA’s 2026 report gives the 2025 worldwide estimates for all data centers and the year-on-year growth of AI-focused sites. The Finnish readings describe the facility’s workloads collectively. [Monthly meters](https://www.sdewes.org/jsdewes/pid7.0301) · [IEA, *Key Questions on Energy and AI*](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary) · [Site interviews](https://doi.org/10.1080/09502386.2021.1895243) · [Data and arithmetic](../../research/sources.md#s175)

2. Rosenblueth, Wiener and Bigelow analyze feedback in a reaching movement. The original Dartmouth proposal names both neural networks and symbolic problems. [Cybernetics sources](../../research/sources.md#s87) · [Dartmouth proposal and funding correspondence](../../research/sources.md#s90)

3. Krizhevsky, Sutskever and Hinton describe two-GPU training and distinguish the scores of individual networks from their competition entry. [Original paper](https://www.cs.cmu.edu/~jeanoh/16-785/papers/krizhevsky-nips2012-alexnet.pdf) · [Source ledger](../../research/sources.md#s183)

4. Jouppi and colleagues document the 2013 demand forecast, the first inference processor and later optical switching in TPU v4. [Forecast and first deployment](https://arxiv.org/abs/1704.04760) This is a separate installation from the Finnish heat-recovery case. [TPU v4](https://arxiv.org/abs/2304.01433)

5. For the budgets for training and inference and evaluation of extra computation, see [the computing sources and study notes](../11-why-the-world-builds-artificial-intelligence.md#chapter-notes).

6. Chris Gamble and Jim Gao give Fuenffinger’s account and identify the historical cooling baseline and the limits of automated control. [Operators and winter cooling](https://deepmind.google/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/)

7. Apollo 15’s local subsurface heat flux was about 21 ± 3 mW/m². The hectare and equivalent area use the central estimate. For heat current P between fixed temperatures, the entropy production rate is P × (1/Tcold − 1/Thot). For electrical work fully dissipated at T, it is P/T. At 320 and 300 K the first calculation gives P/4,800. The two table columns are alternative calculations for the same listed power. Only the separate, additional electrical supply in the powered-rock example is added to the original current. Solar heating, radiation to space and electricity generation lie outside those boundaries. [Apollo probe study](https://ntrs.nasa.gov/citations/19770051977) · [Local flux and uncertainty](https://doi.org/10.1029/2025JE009458) · [MIT thermodynamics](https://web.mit.edu/course/16/16.unified/www/FALL/thermodynamics/notes/node41.html) · [Worked example and maximum-rate hypothesis](../../research/sources.md#s175)

8. Bradley and colleagues estimated reaction rates and available chemical free energy in modern Quaternary-age subseafloor sediments. The 37.3 GW includes aerobic respiration, sulfate reduction and methane production. The cell estimate in the table assumes full dissipation at a common reference temperature. A growing cell can retain some of that free energy in new biomass. [Bradley and colleagues](https://pubmed.ncbi.nlm.nih.gov/32821818/) · [Scope of the comparison](../../research/sources.md#s176)

9. The investigators give the meltwater from both trials in article II and discuss cooling of the animal’s extremities and condensation in article IV. The 3.7 W counts the heat registered by the ice. The table approximates the transfer from a warm body to melting ice and excludes the chemistry of respiration. Southwell and colleagues’ separate colony estimate concerns ingested food energy over the breeding season. [Lavoisier and Laplace, *Mémoire sur la chaleur*](https://fr.wikisource.org/wiki/%C5%92uvres_compl%C3%A8tes_de_Laplace/M%C3%A9moire_sur_la_chaleur) · [Béchervaise Island study](https://www.bas.ac.uk/data/our-data/publication/a-bioenergetics-model-for-estimating-prey-consumption-by-an-adelie-penguin-population-in-east-antarctica/) · [Calculations](../../research/sources.md#s177)

10. Warde’s appendix I, tables 1 and 3, gives total primary energy, coal and energy per person for both years. Only the coal component enters the entropy table. Treating its heat as flowing from a 1,000 K source to a 300 K sink gives a common furnace example. Actual furnaces, engines and users delivered heat and work at different temperatures. The national totals in the text include the other fuels, food and mechanical sources that Warde counted. [Warde’s tables](https://histecon.fas.harvard.edu/energyhistory/data/Warde_Energy%20Consumption%20England.pdf#page=116) · [Conversions and boundaries](../../research/sources.md#s178)

11. The molecular study describes the blinded samples that opened the book. [Graham’s specimens](../../research/sources.md#s161)

12. Darwin describes the practice of recording contrary evidence in his autobiography. The definition of intelligence and the distinction from feedback are the book’s. [Self Modeling](08-self-modeling.md#knowing-when-to-look-again) · [Darwin’s own example in the earlier draft](../../editorial/archive/fourteen-chapter/self-modeling.md)

13. Cogent describes its use of unlit fiber and purchased network assets. Reuse of future AI sites is a conditional comparison. [Dot-com infrastructure and billing](12-bubbles-and-bursts.md)

---

[← Attractor Paradox](16-attractor-paradox.md) · [Contents](../../README.md#contents)
