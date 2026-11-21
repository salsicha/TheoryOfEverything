# Chapter 12 — The Machines That Build the Next Machines

The data center in Mäntsälä used more electricity in July 2016 than in January, yet it supplied more heat to the Finnish town in January. Jani Laine and his colleagues put two sets of records side by side. The center used 3,411 megawatt-hours of electricity in January and 4,034 in July. The municipal heat pump delivered 1,042 megawatt-hours of heat in January and 752 in July.[1]

Air from the servers passed over a heat exchanger and warmed water. The operator gives its temperature as 35 to 40 degrees Celsius. The municipal network requires about 55 to 60 degrees. The town owns the heat pump that raises it the rest of the way. In January the pump used 331 megawatt-hours of electricity. Customers on the other end of the pipes could use more of the heat in winter.[1]

The pipes were there when the operators chose the site. Cooling cost the data center money. Heating cost the town money. The distance to the pipes and the extra electricity needed for the last rise in temperature determined whether the trade could pay. At Whitehaven the corresponding calculation began with the cost of hauling low-value coal away from the pithead.[1][2]

These meters put a condition on the argument for data centers. Concentrating equipment can make something worth doing that is out of reach at a smaller site. The Finnish town could use the heat because the pipes, customers and heat pump were in place. That gain could exist at a center doing ordinary computing. To explain why artificial intelligence belongs in this history we have to identify something a learned decision changes in the physical plant.[1]

## Two plasmas in Lausanne

In a photograph from a fusion laboratory in Lausanne, two bodies of hot, electrically conducting gas hang one above the other in the same vessel. The physicists called them droplets. Jonas Degrave and his colleagues had trained a program to hold the plasmas apart in simulation. On the real machine the camera could see them. The controller had no camera.[3]

A moving electric charge responds to a magnetic field. Change the currents in the coils around the vessel and the plasma can change position or shape. The program had practiced the timing of those adjustments in a simulation. Now it would have to work from magnetic and electrical readings taken on the machine itself. The researchers asked it to keep the locations of the two droplets steady while the current in each rose. The shapes could change.[3]

The photograph caught the droplets 0.55 seconds into the discharge. The controller kept them in position for the full fifth of a second the team had specified, adjusting to magnetic and electrical readings about two thousand times.[3]

Electrical power and a vessel were already available in Lausanne. What training added was the ability to choose coil currents from readings fast enough to hold the two shapes. That is a physical capacity purchased with computation. A fifth of a second of control supplies no evidence of an energy surplus that could finance another machine. A more demanding case would let us follow a learned decision into the construction of the next apparatus.[3]

## Laying out a chip

The first layouts Anna Goldie showed her fellow chip designers curved across the rectangular chip. Some engineers doubted they could be manufactured. They hardly wanted to evaluate them, Goldie recalled in 2021.[4]

The blocks contained circuitry. Bringing two blocks closer can shorten the path a signal travels between them. It can also leave too little room for the wires serving their neighbors. Goldie and Azalia Mirhoseini wanted to let a machine try arrangements a designer might pass over.[4]

The researchers and their colleagues trained a system to place the large blocks one at a time. It knew which connections the circuit required. Each placement changed where the remaining blocks could go. The system scored an arrangement partly on estimates of wire length and congestion. Cheap estimates let it try many arrangements. The engineers could then spend more time on a promising layout, using detailed software to place the smaller components and work out where the wires would run.[4]

In January 2021 a chip carrying several of the machine’s placements came out of manufacture. It was a Google processor for machine learning. Computation on one generation of hardware had helped decide where signals would travel on the next. By 2024 Google said the method had contributed to three generations of its processors.[4]

In Lyon, when Moulin marked a square on paper, he was choosing which warp thread the loom would lift. When a designer moves a block in a file, she changes the distance a signal will have to travel on a chip. This is what I mean by an assembly being jointly material and Platonic. A relation can be specified on paper or in a file. To affect the picture or the timing of the signal, it has to be built into silk or silicon.[4][5]

Chung-Kuan Cheng and colleagues compared the publicly released system with an older search method called simulated annealing. In an updated assessment, they fine-tuned the released model. On seven of nine cases the older method gave shorter total lengths of routed wire. On six of the nine, the learned method did better at meeting timing requirements. An engineer choosing between them would need to know which problem was more serious on the particular chip.[6]

This comparison matters because a firm can adopt an algorithm for more than one reason. A new layout that meets a timing limit can be worth manufacturing even where another method uses less wire. The fact of manufacture establishes one part of the creation argument. Choices made on the old machines affected the capacities of the new ones. To establish an energetic advantage as well, we would need to count the cost of design and measure the work the resulting chips could do on the same supply of electricity.[4][6]

## Connecting 4,096 chips

When thousands of chips share a job, a chip that finishes its arithmetic early may have to wait for the others. A faster chip can spend much of the time it saves waiting for a message.[7]

Google’s TPU v4 supercomputer had 4,096 chips. Small movable mirrors in optical switches could change which groups of chips communicated directly. The chips stayed bolted in place. Operators could change the network to suit the job by turning the mirrors.[7]

This gives a reason to expect data centers to form when many parts of an expensive calculation must meet again before the next part can begin. Keeping the chips close and connecting them to suit the job can release computing time otherwise lost to waiting. Sharing power and cooling spreads their cost over many jobs. Each effect makes it easier to justify the cost of the others. That is the argument for concentration. It makes a different prediction for a task whose data and users are far away and whose calculations rarely need to exchange results.[2][7]

Other jobs are better done on a device beside the thing being measured. Sending the data away and waiting for an answer can take too long. There is a historical reason for the choice of location too. Once a site has staff, power and customers, later users can buy those services there. W. Brian Arthur showed in a model of competing technologies how an early lead could change what later adopters stood to gain. The number of firms at a site can reflect that early advantage as well as the merits of the equipment.[7][8]

## The winter operator

At a Google data center, Dan Fuenffinger watched a control system make colder water than the plant usually supplied. Normally that would cost electricity. In winter the plant could use the air outside. Fuenffinger reported in 2018 that the colder water reduced the power the plant needed for cooling.[9]

Operators had been carrying out the program’s recommendations by hand, including one to spread a cooling load over more pieces of equipment. Useful recommendations began taking up so much of the shift that the operators asked to let the program act on them. The revised system took sensor readings every five minutes. Each adjustment had to pass checks at the service and the site. An operator could take over.[9]

That is a change from quantity to quality. Giving enough useful advice changed who did the adjusting. The program now controlled part of the plant.[9]

Google compared nine months of cooling performance with the plant’s historical baseline. The measure was electrical power per unit of cooling. The reported improvement grew from about twelve percent when autonomous operation began to about thirty percent. To calculate the cost of a year’s useful computing we would also need the weather, the server workload and the cost of running the controls.[9]

## Where the saving went

In Mäntsälä, heat from the data center displaced natural gas the town had burned in its boilers. The electricity for the heat pump still had to come from a power station. To estimate emissions, Laine’s group had to ask which generator would supply the extra electricity. The municipal meter could give them the quantity alone.[1]

I expect AI and data centers to emerge together where training needs frequent exchanges among machines and learned decisions can improve work done at those sites. The claim about their growth is more demanding. A saving on cooling can pay for useful computation, be paid out to investors or reduce demand on a power station. Only some of those outcomes put resources into building a successor. Goldie’s layouts reached later processors. Fuenffinger’s cooling change reached a meter. Neither record says that the saving on one financed the other. For the strongest claim, that the industry realizes a maximum rate of entropy production, we would also need accounts of competing uses over the same years.[4][7][9][10]

In Mäntsälä the municipal company owns the heat pump, pays for its electricity and can collect for heat delivered. In Lyon, Pommet had earned forty francs and still had to claim them. Who gains access to a resource matters to who gets to decide its next use.[1][11]

Before manufacture Goldie’s team could move a block. After manufacture a programmer had to allow for the time a signal took to cross it. There is the part of the argument we can follow all the way through. An arrangement open to choice for one generation becomes a physical constraint for another. I suspect some relations we measure as constants also have histories. In silicon we have evidence that would be very precious in cosmology. The engineers could compare the candidate layouts while a decision was still open. They could identify which one went into the chip.[4][6][10]

## Chapter notes

1. Jani Laine, Kaisa Kontu, Jukka Heinonen and Seppo Junnila describe site selection, the municipal heating company, its heat pump and the accounting assumptions. Table 3 distinguishes electricity used at the data center from heat supplied by the heat pump. The two monthly figures are heat delivered at the plant. The center used 3,411 MWh of electricity in January and 4,034 MWh in July. The operator describes the air-to-water heat exchangers. [Laine and colleagues, site records for 2016](https://www.sdewes.org/jsdewes/pid7.0301) · [Mäntsälä operator’s description](https://nebius.com/sustainability/turning-heat-into-a-resource)
2. For the cost of hauling colliery fuel, see [chapter 5](05-how-disequilibrium-builds-a-new-pathway.md).
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
