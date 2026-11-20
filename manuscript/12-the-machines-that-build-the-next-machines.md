# Chapter 12 — The Machines That Build the Next Machines

In January 2016 the municipal heat pump in Mäntsälä, Finland, delivered 1,042 megawatt-hours of heat. In July it delivered 752. The warmth came from a data center whose servers actually used more electricity in July. Jani Laine and his colleagues put the two records together. The computers produced heat all year. In winter the town’s heating network could use more of it.[1]

Warm air from the server rooms passed through heat exchangers. The municipal company used a heat pump to raise the temperature enough for its district heating network. The servers needed cooling and the town needed heat. Connecting the two systems gave the company something it could sell.[1]

The district heating network was one reason the data center went to Mäntsälä. The location mattered much as it had at an English colliery. At the pithead there was low-value coal to burn and water close by that someone would pay to pump. In Finland there was warm air beside a network of pipes that could take heat to customers.[1][2]

The most surprising use of the electricity in a computing hall happens inside. A computer can help design the next computer. To see how much responsibility to give the machine, consider two cases where researchers could follow its decisions into a laboratory and a factory.

## Two plasmas in Lausanne

In a fusion laboratory in Lausanne, physicists photographed two distinct bodies of plasma, one suspended above the other in the same vessel. They called them droplets. The controller holding them there had learned its job in simulation. On the actual machine it had no camera.[3]

Its job on the TCV machine was to keep the droplets in position as the current in each rose. The controller received magnetic and electrical readings and issued commands to coils ten thousand times a second. The shapes of the droplets could change as long as they stayed in position.[3]

Jonas Degrave and his colleagues published the photograph and the instrument record. The camera caught the droplets 0.55 seconds into the discharge. The controller kept them in place for the full fifth of a second the team had requested, adjusting to readings from the plasma about two thousand times.[3]

The team still needed electricity from outside the vessel for every discharge. What it gained was a way to produce and study a configuration it had practiced on a computer. In chip design, researchers could take a further step. The result of a computation could go into the equipment used for a later calculation.

## Laying out a chip

Azalia Mirhoseini and Anna Goldie faced a practical difficulty in chip design. Large blocks of circuitry took up space. The wires connecting them had to fit in the spaces left over. Moving two blocks closer together might shorten the wire between them and leave too little room for wires to their neighbors.[4]

The researchers and their colleagues trained a system to place the large blocks one at a time. It knew which connections the circuit required. Each placement changed where the remaining blocks could go. The system scored an arrangement partly on estimates of wire length and congestion. Cheap estimates let it try many arrangements. The engineers could then spend more time on a promising layout, using detailed software to place the smaller components and work out where the wires would run.[4]

In 2021 Goldie reported that a chip designed in part by this method had been manufactured. It was a processor for machine learning. By 2024 Google said the method had contributed to three generations of its processors. Some of the work done on one generation of chips had gone into deciding how to build the next.[4]

In Lyon, when Moulin marked a square on paper, he was choosing which warp thread the loom would lift. When a designer moves a block in a file, she changes the distance a signal will have to travel on a chip. This is what I mean by an assembly being jointly material and Platonic. A relation can be specified on paper or in a file. To affect the picture or the timing of the signal, it has to be built into silk or silicon.[4][5]

Chung-Kuan Cheng and colleagues compared the publicly released system with an older search method called simulated annealing. In an updated assessment, they fine-tuned the released model. On seven of nine cases the older method gave shorter total lengths of routed wire. On six of the nine, the learned method did better at meeting timing requirements. An engineer choosing between them would need to know which problem was more serious on the particular chip.[6]

People specified the operations the chip had to perform, set the timing requirements and authorized production. The learning system proposed where to put the blocks. Its contribution can be identified in a processor someone manufactured. A machine helped design its successor, and the comparison with the older method tells us when a designer might choose to do the job differently.[4][6]

## Connecting 4,096 chips

When thousands of chips share a job, a chip that finishes its arithmetic early may have to wait for the others. A faster chip can spend much of the time it saves waiting for a message.[7]

Google’s TPU v4 supercomputer had 4,096 chips. Small movable mirrors in optical switches could change which groups of chips communicated directly. The chips stayed bolted in place. Operators could change the network to suit the job by turning the mirrors.[7]

This helps explain why data centers arise naturally. Researchers can use a fast network, a reliable power supply and cooling equipment that few of them could afford to install for a single project. As at the colliery, having expensive equipment and cheap power in place can make it worth trying a new use that may take time to pay for itself.[2][7]

Other jobs are better done on a device beside the thing being measured. Sending the data away and waiting for an answer can take too long. There is a historical reason for the choice of location too. Once a site has staff, power and customers, later users can buy those services there. W. Brian Arthur showed in a model of competing technologies how an early lead could change what later adopters stood to gain. The number of firms at a site can reflect that early advantage as well as the merits of the equipment.[7][8]

## The winter operator

In 2018 Dan Fuenffinger, a Google data center operator, described an unexpected cooling decision. In winter the control system made colder water than the facility usually called for. That sounded expensive. Under the conditions Fuenffinger observed, the plant could use the cold outside and spend less electricity on cooling.[9]

At first the program recommended changes for the operators to make. One was to spread a cooling load over more pieces of equipment. As the recommendations improved, operators spent more time carrying them out. They asked for a change. Let the system make some adjustments itself. In the revised arrangement, it received sensor readings every five minutes. Each proposal had to pass checks at the service and at the site. Operators retained the ability to switch back to ordinary controls.[9]

There is a dialectical change here. Operators taught a system to advise them. As the number of useful recommendations grew, acting on them took up more of the shift. Giving the system authority to act within limits changed the kind of equipment it was. It could now run part of the plant, and the operators could decide when to take back control.[9]

Google compared nine months of cooling performance with the plant’s historical baseline. The measure was electrical power per unit of cooling. The reported improvement grew from about twelve percent when autonomous operation began to about thirty percent. To calculate the cost of a year’s useful computing we would also need the weather, the server workload and the cost of running the controls.[9]

At Fowey Consols the witnesses deducted three hours from the work credited to a pump whose bucket broke. The counters had kept recording strokes. In the data center, too, the choice of what to count matters. Electricity saved in cooling is a measurable gain. How much additional computing that gain bought is a separate question.[2][9]

## Where the saving went

In Mäntsälä, Laine and his colleagues could follow the heat as far as the municipal network. To estimate the change in emissions they had to ask how the town would otherwise have heated its buildings and how the electricity for the heat pump was produced. The same quantity of heat delivered could give different answers depending on which fuel it replaced.[1]

For the chips we can trace what came next more directly. Google identified blocks in three generations of processors designed with help from its placement system. The result of one round of production had changed how people could carry out the next.[4][6]

I expect powerful computers and the facilities that supply them to arise naturally where people can put enough electricity, equipment and prior work to this use. Finding a better layout or a use for waste heat is the creative step. Using part of the gain to try again helps explain why such arrangements recur. To establish that a particular arrangement maximized the rate of entropy production, we would have to measure what happened to the same available energy under competing arrangements as well.[9][10]

Who owns the equipment matters. Pommet could show a Lyon tribunal what her employer owed her for forty francs’ worth of work. Collecting it was another matter. In Mäntsälä, the municipal company could charge for heat it delivered. A gain creates new opportunities, and the people entitled to claim it choose which of them to pursue.[1][11]

A chip designer can still move a block before the plans go to the factory. Years later, a programmer working on that chip has to accept the time a signal takes to cross it. A relation that one person could change has become a physical constraint for another. Chapter 6 asks whether some laws and constants could have a history of that kind. For a chip we have the design records. For the universe we would have to identify something we can measure today that distinguishes an assembled relation from one that was always fixed.[10]

In Lyon, one weaver left just such a record of a choice. The first portrait of Jacquard carried no credit for the weaving. For the second silk we have the weaver’s name and the painter’s receipt.[5]

## Chapter notes

1. Jani Laine, Kaisa Kontu, Jukka Heinonen and Seppo Junnila describe site selection, the municipal heating company, its heat pump and the accounting assumptions. Table 3 distinguishes electricity used at the data center from heat supplied by the heat pump. The two monthly figures are heat delivered at the plant. The center used 3,411 MWh of electricity in January and 4,034 MWh in July. The operator describes the air-to-water heat exchangers. [Laine and colleagues, site records for 2016](https://www.sdewes.org/jsdewes/pid7.0301) · [Mäntsälä operator’s description](https://nebius.com/sustainability/turning-heat-into-a-resource)
2. For colliery fuel, the counter readings, the witnesses’ deduction and the South Devon directors’ decision, see [chapter 5](05-how-disequilibrium-builds-a-new-pathway.md) · [Cornish witnesses’ account](../research/sources.md#s146) · [Brunel’s report](../research/sources.md#s156).
3. Jonas Degrave and colleagues describe the separate plasma domains, the 200-millisecond control window and the camera at 0.55 seconds in figure 4. The ten-kilohertz controller received magnetic and electrical measurements. [Published paper and figure 4](https://doi.org/10.1038/s41586-021-04301-9) · [EPFL authors’ manuscript](https://infoscience.epfl.ch/bitstreams/80aa6262-a6ef-4645-b589-c23ea5d23408/download)
4. Azalia Mirhoseini, Anna Goldie and colleagues describe the circuit representation, sequential placement, training score and more detailed evaluation. Goldie identified the manufactured processor. The later three-generation deployment is Google’s report. [Research paper](https://doi.org/10.1038/s41586-021-03544-w) · [Goldie’s interview](https://www.nature.com/articles/d41586-021-01558-y) · [Google DeepMind’s 2024 account](https://deepmind.google/blog/how-alphachip-transformed-computer-chip-design/)
5. For Moulin’s pattern, Carquillat’s weaving and the effect of the curtain see the [Lyon museum and Metropolitan Museum records](../research/sources.md#s147) · [Bonnefond’s receipt and the 1844 silk](https://pop.culture.gouv.fr/notice/joconde/10230001974).
6. The comparison of fine-tuned AlphaChip and simulated annealing is from table III and section VI.A of the updated paper. The quantities are total routed wire length and total negative slack, a measure of timing shortfall. The authors describe their circuit selection and training conditions. [Cheng and colleagues, “An Updated Assessment of Reinforcement Learning for Macro Placement”](https://vlsicad.ucsd.edu/Publications/Journals/j148.pdf) · [Earlier assessment](https://arxiv.org/abs/2302.11014v1)
7. Norman Jouppi and colleagues describe the 4,096-chip TPU v4 system and its mirror-based optical switches in section 2. The network example concerns this earlier system. Google’s later account of learned layouts in note 4 identifies v5e, v5p and Trillium. [Jouppi and colleagues, “TPU v4”](https://arxiv.org/abs/2304.01433) · [Berkeley Lab on physical provisioning](https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report)
8. W. Brian Arthur models how early adoption can influence later technological choice. The facilities comparison is the book’s application. [“Competing Technologies, Increasing Returns, and Lock-In by Historical Events”](https://www.jstor.org/stable/2234208)
9. Chris Gamble and Jim Gao give Fuenffinger’s account, the five-minute interval, the checks at the site and the operators’ authority. The company compares power per ton of cooling against a historical baseline over nine months. The accounting measure applies to cooling power. [Google DeepMind, “Safety-first AI for autonomous data centre cooling and industrial control”](https://deepmind.google/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/)
10. Extending biological autopoiesis to productive organization, the energetic preference and the conjecture about assembled constants are the book’s arguments. [Varela, Maturana and Uribe](../research/sources.md#s33) · [Production and closure](../research/sources.md#s124) · [Chapter 2 on energetic comparisons](02-the-gradient-and-the-barrier.md) · [Chapter 6 on assembled laws](06-from-uncertainty-to-an-assembled-universe.md)
11. For Pommet’s wage claim see the [Lyon tribunal report and source notes](09-the-system-that-produces-its-tomorrow.md#chapter-notes).

---

[← Why the World Builds Artificial Intelligence](11-why-the-world-builds-artificial-intelligence.md) · [Contents](../README.md) · [The World That Builds Its Next Question →](epilogue.md)
