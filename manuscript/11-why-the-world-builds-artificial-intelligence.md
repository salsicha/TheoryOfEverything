# Chapter 11 — Why the World Builds Artificial Intelligence

Ada Lovelace needed three copies of an eight. In an 1843 diagram for Charles Babbage’s proposed Analytical Engine, the first operation doubled a number and sent the result to three columns. Start with four. Subtract one from the first eight, add one to the second, and the Engine has a seven, a nine and an eight to use later.[1]

Lovelace was working out how the Engine could calculate a Bernoulli number. On paper, a mathematician could use the same symbol in three places. The Engine had to find a number in the right column when a card called for it. Overwrite the only eight and the next operation would fetch a seven.[1]

Babbage offered to do the Bernoulli algebra for her. She sent it back to him for correction. He tells the story in his memoir and leaves out which calculation she corrected. The Engine itself was never completed.[1][2]

Babbage borrowed punched cards from the loom. As Lovelace explained, one set could specify the operation and another the columns that held the numbers. The cards would tell the Engine which eight to keep.[1]

Lovelace thought an Engine could do what people knew how to specify. She also thought that expressing mathematics for a machine might help mathematicians discover something. In 1950 Alan Turing took up what he called Lady Lovelace’s objection. Machines often surprised him. He might assume two points in a circuit would have the same voltage and skip the calculation. By the time he tried the circuit he might even have forgotten his assumption. Running it could teach him something about a machine whose workings he knew.[1][3]

I expect artificial cognition to emerge naturally once a society can afford machines and has accumulated enough work that the machines can learn from it. There is an economic and a technical reason. A judgment that has to be bought anew each time is expensive to use widely. If some of the work of acquiring it can be done once, retained and used on many cases, it can pay to spend far more on acquiring it in the first place. Lovelace could store a procedure. The harder case is a judgment for which nobody can supply the steps.

## Before anybody types

What is 98 plus 45? Tom Brown and his colleagues printed this question in their 2020 study of a language model. They could show it several questions paired with correct answers before giving it a fresh sum. None of the examples needed an instruction to add the eight and the five and carry one. An answer of 143 would pass the check however the machine arrived at it.[4]

During training the model had tried to predict the next piece of a passage. Whoever wrote the passage had supplied the answer simply by finishing it. A book written centuries before there was such a machine could help train one.[4]

Each discrepancy between prediction and text gave the training program a way to adjust numbers called *weights*. A change to a weight affects future predictions. The process can teach the model to continue a calculation correctly. It can also teach a common error. Brown’s team could use arithmetic to tell which it had learned.[4]

Once trained, the weights can travel as a file. Each keeps its place in the calculation on a second compatible machine. That relation is the Platonic part of the assembly. It took hardware, electricity and time to produce the file and takes all three again to use it.[4][5]

The gain extends beyond making copies. People doing ordinary work have already made a great many judgments and left records of them. Predicting one part of a record from another can supply millions of occasions for correction without an expert writing a rule for each case. Computing power makes that search affordable. The structure in the records determines what it can learn. I would expect this route to develop sooner for tasks with repeatable, checkable outcomes than for one-off decisions whose consequences nobody records. Giving a machine more electricity does nothing to remove that difference.[4][5]

A file on a disk can sit there indefinitely. A person, a timer or another program has to initiate a calculation. Shunyu Yao and his colleagues gave a running language model another action it could take. It could search Wikipedia and read the response.[6]

One of the worked examples the team supplied concerned an ancient episode of mountain building in Colorado. What was the elevation range of the land it reached in the east? The first article identified the High Plains. A search for *High Plains* led to a choice between two regions. Only when the search specified the United States did an article give the elevations, from about 1,800 to 7,000 feet. Each return from the encyclopedia changed what it made sense to ask next. The researchers gave the machine examples of how to make that change, as well as the means to look up fresh questions.[6]

During an ordinary exchange, the weights usually stay fixed. The service can keep a search result in the text it supplies for the next step. It can also train the model again on new evidence, which changes the weights and may affect an answer in a fresh conversation. Keeping a record and learning from it are separate operations.[4][6]

## An extra consonant

The word was *raspberry*. Asked to count the r’s, a model in a 2025 paper found one at the start and one in seventh place. The eighth letter, it said, was a y. It gave its answer and tried to stop.[7]

Software interrupted it. The program suppressed the signal that would end that part of the response and added one word, *Wait*. The model spelled *raspberry* again. This time it found the two r’s together near the end and counted all three. The software had supplied no information about spelling. It would have interrupted a correct answer too.[7]

Niklas Muennighoff and his colleagues had started with an existing model and trained it further on a thousand problems with worked answers. That took twenty-six minutes on sixteen high-end processors. The time excluded the training of the original model and the preparation of the examples. Responding to *Wait* used additional computation on the question itself.[7]

In this case, part of what people call “thinking mode” really was a change to the prompt. Worked examples and instructions to proceed step by step can also improve some answers. Other methods involve additional training. The DeepSeek-R1 researchers, for instance, rewarded checkable answers while training the model. A service can also produce several answers and check them separately. Of these methods, additional training changes the weights used for future requests.[7][8]

Every attempt has a finite computing budget. A service can spend it on a longer answer, on several attempts, or on checking the results. Charlie Snell and colleagues found that the best choice depended partly on how difficult the problem was for the model. Jie Huang and colleagues found cases where asking a model to reconsider without giving it outside evidence caused it to abandon a correct answer.[9]

All nine letters of *raspberry* were on the page. Another attempt could recover the one the model had overlooked. If an error lies instead in the evidence supplied to every attempt, more time can make the wrong answer more elaborate. Calling both operations ‘thinking’ conceals a choice a designer has to make. A system can spend its next unit of work examining the same evidence again or obtaining a genuinely independent observation.[6][7][9]

## The unit that stayed on Earth

On September 23, 1999, the radio signal from NASA’s Mars Climate Orbiter fell silent forty-nine seconds early. The navigators had expected to lose contact for twenty-one minutes as Mars blocked the signal. It never came back. For two more days NASA tried to make contact.[10]

During the nine-month flight, sunlight had pressed unevenly on the solar array. Spinning wheels kept the craft pointed the right way. From time to time thrusters fired to unload momentum from the wheels. Each firing also nudged the spacecraft off course. A program on Earth recorded those impulses so the navigators could allow for them.[10]

The ground program supplied pound-force seconds. The navigation program read the same numbers as newton-seconds. One pound of force is about 4.45 newtons, so each nudge in the reconstruction was less than a quarter of its actual size. The firings also came much more often than expected. The errors accumulated all the way to Mars.[10]

The specification said newton-seconds. Checking it again would have confirmed the expected units. The spacecraft itself had been estimating its changes in velocity and sending them to Earth. The navigators learned of those figures well after launch. The board concluded that comparing them earlier might have exposed the mistake.[10]

The investigation board recommended testing actual transfers between programs, having the users sign off on the results, and calling in independent navigators. People had learned to question the way they checked their answers. Darwin’s rule for recording objections changed a practice of the same kind.[10][11]

Yao’s model could revise an answer when another article supplied a fact. The navigators had to revise the practice that decided which facts reached them at all. That is the distinction the account of intelligence requires. A running model can make a useful choice within an inquiry, while the capacity to redesign the inquiry can still reside with the people who give it tools. Putting the two together can yield a new ability in the organization even when the file of trained weights stays exactly as it was.[4][6][10][11]

It follows that there are two different returns to look for. Saving somebody the work of specifying every step helps explain why people will pay to train and use a model. Explaining why the next generation of machines gets built requires tracing the benefit back to people who can pay for equipment, power and another round of learning. A learning gradient tells a program how to change the weights. Only a physical system can deliver a saving in electricity or make a new task feasible. At a data center Dan Fuenffinger could compare the power needed to cool a room before and after a learned adjustment. That brought one part of the argument within reach of a meter.[4][5][12]

## Chapter notes

1. Lovelace’s Notes A and G explain operation and variable cards, the Engine’s capacities and the possible reciprocal influence on mathematical thought. The example with input four follows the first three rows of the Bernoulli diagram. [Lovelace’s notes to Menabrea, 1843](https://www.fourmilab.ch/babbage/sketch.html) · [Facsimile of the diagram](https://www.cs.ox.ac.uk/RIMC-Y9-2021/LovelaceProgramme/FirstComputerProgram.pdf) · [Moulin and the portrait](../research/sources.md#s147)
2. Babbage recalls the error and Lovelace’s intervention in chapter VIII of his 1864 memoir. He does not identify the step. [*Passages from the Life of a Philosopher*](https://www.fourmilab.ch/babbage/lpae.html)
3. Turing discusses surprise and gives the voltage illustration under “Lady Lovelace’s Objection” in section 6. [A. M. Turing, “Computing Machinery and Intelligence,” *Mind*, 1950](https://doi.org/10.1093/mind/LIX.236.433) · [Paper facsimile](https://www.cs.unibo.it/~nuzzoles/courses/intelligenza-artificiale/papers/Turing1950.pdf)
4. Brown and colleagues describe autoregressive language modeling and the use of examples in context. Section 3.9.1 and figure G.44 document the arithmetic tests and example. Vaswani and colleagues describe an architecture and its sequential generation. [“Language Models are Few-Shot Learners,” §§2–2.2](https://arxiv.org/abs/2005.14165) · [“Attention Is All You Need,” §3](https://arxiv.org/abs/1706.03762)
5. The energetic cost depends on the physical implementation of a computation. [David H. Wolpert, “Stochastic thermodynamics of computation”](https://arxiv.org/abs/1905.05669)
6. Shunyu Yao and colleagues describe using Wikipedia queries and retrieved observations on HotpotQA and FEVER. Their appendix gives the worked Colorado and High Plains example among the prompts supplied by the researchers. [“ReAct”](https://arxiv.org/abs/2210.03629)
7. Figure 3 in the January 2025 version gives the two counts in the raspberry example. Sections 2–4 report the training data, the cost of fine-tuning and the intervention when generation tries to stop. [Muennighoff and colleagues, *s1: Simple test-time scaling*, especially figure 3](https://arxiv.org/pdf/2501.19393v1#page=4)
8. The three papers distinguish worked examples in a prompt, a short reasoning instruction and training with reinforcement. [Wei and colleagues](https://arxiv.org/abs/2201.11903) · [Kojima and colleagues](https://arxiv.org/abs/2205.11916) · [DeepSeek-AI and colleagues](https://arxiv.org/abs/2501.12948)
9. These comparisons concern the particular models, problems and feedback conditions studied. [Snell and colleagues on allocating computation at inference](https://arxiv.org/abs/2408.03314) · [Huang and colleagues on self-correction](https://arxiv.org/abs/2310.01798)
10. The mishap board identifies the ground-software unit mismatch, the factor of 4.45 and weaknesses in verification and communication. Sections 2, 4 and 5 give the times of the expected occultation, the spacecraft’s independent estimates and the missed opportunity to compare them. [NASA, Mars Climate Orbiter mishap report](https://discovery.larc.nasa.gov/pdf_files/MCO_report_2.pdf) · [NASA’s record of the loss of contact](https://nssdc.gsfc.nasa.gov/planetary/news/mco_19990923.html)
11. The definition and the distinction between monitoring and recursive self-modeling are developed in [chapter 10](10-the-system-that-models-itself.md). For a learned system whose proposed mathematical steps can be checked independently, see [Hubert and colleagues on AlphaProof](https://www.nature.com/articles/s41586-025-09833-y).
12. The industrial extension of autopoiesis and the energetic preference are the book’s hypotheses. [Varela, Maturana and Uribe](../research/sources.md#s33) · [Chapter 2 on physical gradients and useful work](02-the-gradient-and-the-barrier.md) · [Fuenffinger and the winter cooling change](https://deepmind.google/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/)

---

[← The System That Models Itself](10-the-system-that-models-itself.md) · [Contents](../README.md) · [The Machines That Build the Next Machines →](12-the-machines-that-build-the-next-machines.md)
