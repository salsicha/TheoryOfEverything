# Chapter 18 — Do Data Centers Maximize Entropy Production?

The data center in Mäntsälä used more electricity in July 2016 than it did in January. Yet it supplied more heat to the Finnish town in January. Jani Laine and his colleagues put two sets of records side by side. The center used 3,411 megawatt-hours of electricity in January and 4,034 in July. The municipal heat pump delivered 1,042 megawatt-hours of heat in January and 752 in July. Someone looking only at the power bill would have picked the wrong month for the greater delivery.[1]

Air from the servers passed over a heat exchanger and warmed water. The operator gives its temperature as 35 to 40 degrees Celsius. The municipal network needs about 55 to 60 degrees. The town owns the heat pump that raises the temperature the rest of the way. In January the pump used 331 megawatt-hours of electricity. The municipal figures record heat leaving that second machine. They tell us what the network received and how much extra electricity the town had to buy to deliver it.[1]

The pipes were there when Yandex chose the site. Its head of infrastructure told researcher Julia Velkova what the company had come for. The fiber connections could carry its traffic. The road links made it easier to bring equipment across the border, and Finland’s cold air could cool the servers. It was Nivos, the local utility, that suggested selling the heat. Yandex agreed to try it. Each party saw a use for something the other had already decided to build. In summer, the servers could go on working after much of that particular advantage had gone.[1]

## Why put 4,096 chips together?

The sale of heat explains why Nivos built a heat pump. It could have taken heat from servers running almost any computer program. To explain why large centers arise specifically in the history of artificial intelligence, we have to identify a constraint in the work being done inside them.

When thousands of chips share a calculation, a chip that finishes its arithmetic early may have to wait for the others. A faster chip can spend much of the time it saves waiting for a message. Google’s TPU v4 supercomputer had 4,096 chips. Small movable mirrors in optical switches could change which groups of chips communicated directly. The chips stayed bolted in place. Operators could change the network to suit the job by turning the mirrors.[2]

This gives a reason to expect data centers to form when many parts of an expensive calculation must meet again before the next part can begin. Keeping the chips close and connecting them to suit the job can release computing time otherwise lost to waiting. Common power and cooling equipment can serve many jobs. These benefits make concentration worth paying for under particular conditions. A small device beside a sensor faces a different calculation. If a decision has to be made there before a message can get to the center and back, a roomful of faster processors at the far end of the connection will do it little good.[2]

A center can also make its own location more attractive to later users. Power has been brought in, engineers know the site, and a heating company may have built a pump to receive its waste heat. Each investment changes what the next user would have to pay to get started. The fact that the tenth customer follows the ninth tells us something about the choices open to that tenth customer. It leaves the merits of other possible sites at the time of the first decision an open question.[1][3]

## What the winter operator changed

At a Google data center, Dan Fuenffinger watched a control system make colder water than the plant usually supplied. Normally that would cost electricity. In winter the plant could use the air outside. Fuenffinger reported in 2018 that the colder water reduced the power the plant needed for cooling.[4]

Operators had been carrying out the program’s recommendations by hand, including one to spread a cooling load over more pieces of equipment. Useful recommendations took up so much of the shift that the operators asked to let the program act on them. The revised system took sensor readings every five minutes. Each adjustment had to pass checks at the service and the site. An operator could take over. Repeated recommendations had brought about a different arrangement for running the plant. Something learned on computers now changed what some of the computers’ own supporting machinery did.[4]

Google compared nine months of cooling performance with the plant’s historical baseline. Its measure was electrical power per unit of cooling. The reported improvement grew from about twelve percent when autonomous operation began to about thirty percent. The company had a reason to keep using the controller. Those figures leave open where the saved electricity went. Fuenffinger could see the effect on the cooling system during his shift. Whether a computing customer bought additional work or the power station reduced generation lay outside his control room.[4]

Sam Eyde faced the same gap between two accounts. With the new ammonia plants, Hydro could make more fertilizer for each unit of electricity it spent. Then it had to get enough orders to put the capacity to use. An owner who can sell another hour of computing has reason to fill the space a more efficient cooling plant has freed. An owner without another order can simply enjoy the lower bill. The efficiency improvement is real in either case. Only the first gives an immediate reason to expand production.[4][5]

## Which rate do the meters measure?

In Mäntsälä, heat from the data center displaced natural gas the town had burned in its boilers. The electricity for the heat pump still had to come from somewhere. Laine’s group showed why an emissions estimate changes when it includes the generator supplying the extra power. A drop in gas use at a town boiler and a drop in emissions across the power system are two claims requiring different records.[1]

The book’s conjecture concerns the rate of entropy production. A kilowatt-hour measures energy. Transferring a given amount of heat from a warm body to a cooler one produces entropy in an amount that depends on both temperatures. Delivering useful heat to houses at one temperature and releasing it to outdoor air at another involve different transfers. Between the server and the house sits a pump doing work. Beyond the walls of the center there may also be a generator burning fuel and a boiler that has stopped burning it. The figure on a meter can enter the account, but there is no reading on the Finnish bill that we can relabel “entropy per second.”[1][6]

Here the strongest version of the thesis takes a chance. For a given demand for computing and heat, compare the center in Mäntsälä with a feasible arrangement that does the same jobs at another site and heats the same buildings by other means. For tasks that could reasonably run on local devices, include that possibility too. Follow the systems over the same winter and summer, count the power they draw and the fuel they displace, and account for the temperatures at which heat leaves them. A comparison with one alternative could rule out a proposed maximum if that alternative sustained a higher rate. Finding a higher rate than one competitor would leave other possibilities open.[1][6]

I expect concentrations of computing equipment to arise where fast communication, reliable power and repeated demand reward them. That explains why anyone would order an optical switch. The book also proposes that assemblies which draw more energy into sustained activity tend to recur when the return pays for more of them. That claim requires us to follow what happens after the switch earns its keep. A strong claim that the arrangement yields the greatest feasible rate of entropy production goes further still. A center could keep attracting customers by giving them an answer sooner even if another arrangement produced more entropy. The customers’ choice, in that case, would weigh against the proposed maximum.[2][3][6]

When Heather Graham handed over her unidentified samples at the start of this book, the researchers had to say which traces they thought a repeated process of construction could leave. Only afterwards did they learn where the samples came from. The same discipline applies to a whole building that hums with computers. We know people built it. What we want to learn from it is why *this* arrangement of machines kept getting built, what work it made possible, and whether that work helped pay for the next one. In Mäntsälä one part of the answer turns up across town, on a heating company’s meter, in the middle of winter.[1][7]

## Chapter notes

1. Jani Laine, Kaisa Kontu, Jukka Heinonen and Seppo Junnila give the site history and the plant and district-heating records for 2016. Table 3 distinguishes data-center electricity, recovered heat, pump electricity and heat supplied by the pump. The operator describes the equipment and temperatures. Julia Velkova interviewed the data-center and utility teams about the choice of site and the origin of the heat-recovery scheme. [Laine and colleagues, site study and monthly records](https://www.sdewes.org/jsdewes/pid7.0301) · [Mäntsälä operator’s account](https://nebius.com/sustainability/turning-heat-into-a-resource) · [Velkova, “Thermopolitics of data”](https://doi.org/10.1080/09502386.2021.1895243) · [Source ledger](../../research/sources.md#s169)

2. Norman Jouppi and colleagues describe the 4,096-chip TPU v4 system and the optical switches in section 2. The comparison with time-sensitive jobs on local devices is the book’s application of the communication constraint. [Jouppi and colleagues, “TPU v4”](https://arxiv.org/abs/2304.01433)

3. W. Brian Arthur models how early adoption can alter the choices faced by later adopters. In Mäntsälä the heating network is a documented pre-existing asset. [Arthur, “Competing Technologies, Increasing Returns, and Lock-In by Historical Events”](https://www.jstor.org/stable/2234208)

4. Chris Gamble and Jim Gao record Fuenffinger’s account, operator authority and the company’s comparison of cooling power per unit of cooling delivered. The comparison concerns the cooling plant. [Google DeepMind, autonomous data-center cooling](https://deepmind.google/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/)

5. Hydro’s capacity and sales figures in the American and German process conversions refer to different quantities. [Chapter 17](17-why-did-sam-eyde-want-to-replace-his-own-furnace.md)

6. The entropy change for the transfer of heat between reservoirs at different temperatures is developed in MIT’s thermodynamics notes. The source ledger records the scope and assumptions of proposed maximum-entropy-production principles. [MIT, heat transfer between reservoirs](https://web.mit.edu/course/16/16.unified/www/FALL/thermodynamics/notes/node41.html) · [Thermodynamic proposals](../../research/sources.md#s07)

7. For Graham’s role and the authors’ interpretation of the blind-sample results, see the [molecular assembly study and source notes](../../research/sources.md#s161).

---

[← Why Did Sam Eyde Want to Replace His Own Furnace?](17-why-did-sam-eyde-want-to-replace-his-own-furnace.md) · [Contents](../../README.md) · [Afterword · What Would Make This a Theory? →](../afterword.md)
