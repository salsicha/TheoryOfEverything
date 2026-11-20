# Chapter 11 — Why the World Builds Artificial Intelligence

Ada Lovelace needed three copies of the same number. In a diagram she published in 1843 for Charles Babbage’s proposed Analytical Engine, the first operation doubled a number and put a copy in each of three columns. The next operation subtracted one from the first copy. Another added one to the second. Starting with four gave her three eights, then a seven, a nine and the eight she had kept for later.[1]

Lovelace was working out how the Engine could calculate a Bernoulli number. Settling the algebra was only part of her job. Every intermediate result had to be in the place where a later operation would look for it.[1]

Babbage recalled offering to do the Bernoulli algebra to save Lovelace some trouble. She sent it back. He had made a mistake. He admitted as much in his memoir, although he left out which calculation she had corrected. The Engine was never completed. Lovelace had already caught an error its inventor would have asked it to carry out.[1][2]

Babbage borrowed the idea of punched cards from the loom. Lovelace explained how one set of cards could tell the Engine which operation to perform and another where to find the numbers it needed. In Lyon, Moulin could make a pattern for a curtain and a weaver could follow it elsewhere. Lovelace could do much the same for a calculation. The cards would specify which eight to keep and which two to change.[1]

Lovelace thought an Engine could do what people knew how to specify. She also thought that expressing mathematics for a machine might help mathematicians discover something. In 1950 Alan Turing took up what he called Lady Lovelace’s objection. Machines often surprised him. He might assume two points in a circuit would have the same voltage and skip the calculation. By the time he tried the circuit he might even have forgotten his assumption. Running it could teach him something about a machine whose workings he knew.[1][3]

Learning introduced a further possibility. People could specify how to train a machine and end up with a machine that performed a task they still couldn’t write adequate instructions for.

## Before anybody types

In an appendix to a 2020 paper, Tom Brown and his colleagues printed a question from their test of a language model. What is 98 plus 45? The answer they would accept was 143. They could give the model examples of additions in the text of a prompt, then ask for a fresh sum and check it by ordinary arithmetic. Lovelace had specified the operations and where to find the numbers. Brown’s team could show a trained machine what a sum looked like on the page and start finding out how much addition it could already do.[4]

A passage of text contains examples a training program can check for itself. Given the beginning of a sentence, the model predicts the next piece. The writer has already supplied the answer. Books and correspondence written for other purposes could now be used to train a machine to continue sentences it had never seen.[4]

When a prediction differed from the text, the training program adjusted numbers called *weights*. The design determined how a change to one weight would affect future predictions. This practice could teach the model to continue a calculation correctly. It could also teach it to repeat a common error. Brown’s team used arithmetic to find out which answers were right.[4]

The learned relations can travel as a file. A numerical weight has the same place in the calculation on a second compatible machine. That is the Platonic character of the assembly in the sense used here. Its material character shows up in every training run. Operations take time, electricity and equipment. The new capability consisted in giving those resources an organization under which the examples could do work on the next problem.[4][5]

At Whitehaven, mine operators already had fuel they could burn to pump water. The people who trained the language model also had to spend electricity before they knew what they could accomplish. In this case, what directed the work was a simple condition. A prediction could be compared with what someone had actually written, sometimes centuries earlier.[4][5]

A trained model on storage produces no answer until something initiates a computation. An input can come from a person, a timer or another program. Shunyu Yao and his colleagues built a service that could turn a model’s requests into searches of Wikipedia. On question-answering and fact-checking tasks, the result of a search became part of the material available for the next step. The model could now acquire a fact during a run. That capability came into existence when the researchers joined it to a source of observations and gave it a way to ask.[6]

During an ordinary exchange, the weights usually stay fixed. The service can keep a search result in the text it supplies for the next step. It can also train the model again on new evidence, which changes the weights and may affect an answer in a fresh conversation. Keeping a record and learning from it are separate operations.[4][6]

## An extra consonant

The word was *raspberry*. Asked to count the r’s, a model in a 2025 paper found one at the start and one in seventh place. The eighth letter, it said, was a y. It gave its answer and tried to stop.[7]

Software interrupted it. The program suppressed the signal that would end that part of the response and added one word, *Wait*. The model spelled *raspberry* again. This time it found the two r’s together near the end and counted all three. The software had supplied no information about spelling. It would have interrupted a correct answer too.[7]

Niklas Muennighoff and his colleagues had started with an existing model and trained it further on a thousand problems with worked answers. That took twenty-six minutes on sixteen high-end processors. The time excluded the training of the original model and the preparation of the examples. Responding to *Wait* used additional computation on the question itself.[7]

In this case, part of what people call “thinking mode” really was a change to the prompt. Worked examples and instructions to proceed step by step can also improve some answers. Other methods involve additional training. The DeepSeek-R1 researchers, for instance, rewarded checkable answers while training the model. A service can also produce several answers and check them separately. Of these methods, additional training changes the weights used for future requests.[7][8]

Every attempt has a finite computing budget. A service can spend it on a longer answer, on several attempts, or on checking the results. Charlie Snell and colleagues found that the best choice depended partly on how difficult the problem was for the model. Jie Huang and colleagues found cases where asking a model to reconsider without giving it outside evidence caused it to abandon a correct answer.[9]

An extra attempt helped with *raspberry* because the missing r was still on the page. More computation by itself gives a model no new evidence. A navigation team at NASA once faced a much more costly version of that problem.[7][9]

## The unit that stayed on Earth

On September 23, 1999, NASA lost contact with the Mars Climate Orbiter as it reached Mars. Among the things the investigators examined was a file produced on the ground. Small thruster firings had given the spacecraft a succession of nudges during its journey. To reconstruct the orbit, navigators needed to know how much impulse those firings had supplied. The figures delivered in the file were in pound-force seconds. The navigation calculations expected newton-seconds. To the receiving program each nudge appeared smaller than it was by a factor of about 4.45.[10]

The specification gave the units the navigators expected. The software producing the file used different units. Reading the specification again would only have confirmed the intended units. The investigation board also found missed opportunities to check the spacecraft’s trajectory against independent observations while the team still had time to act.[10]

The same figures in the file described two different trajectories depending on which units the navigators used. The digits alone could never settle which was right. Checking an actual transfer between the programs could have done so. Yao’s Wikipedia searches gave the question-answering system a way to obtain similarly independent evidence.[6][10]

The investigation board recommended changes for the Mars Polar Lander team. The people using the ground software should sign off on its products. Transfers between programs should be checked, and independent navigators should review the trajectory. Like Darwin writing down the observations he was likely to forget, the board changed how the next error could be discovered.[10][11]

This suggests a test for artificial self-modeling. Can a system detect a recurring failure in its own checks and change what it consults next time? In the Mars investigation, people did that work. In the Wikipedia service, people provided the means to look something up. An account of machine intelligence has to say who recognized the problem and who supplied the new capacity.[6][10][11]

I propose that artificial cognition arises naturally in societies that have enough power, suitable equipment and enough previous work in a form machines can learn from. A physical energy gradient supplies power. What engineers call a learning gradient tells the program how to change weights to reduce error. These gradients do different jobs. At a Google data center, Dan Fuenffinger found a use for both. A model trained on plant records suggested a way to use the winter cold to reduce the electricity spent on cooling.[4][5][12]

The decision had to be tried on the equipment. The plant’s meters could tell Fuenffinger’s team whether colder water actually saved electricity.[12]

## Chapter notes

1. Lovelace’s Notes A and G explain operation and variable cards, the Engine’s capacities and the possible reciprocal influence on mathematical thought. The example with input four follows the first three rows of the Bernoulli diagram. [Lovelace’s notes to Menabrea, 1843](https://www.fourmilab.ch/babbage/sketch.html) · [Facsimile of the diagram](https://www.cs.ox.ac.uk/RIMC-Y9-2021/LovelaceProgramme/FirstComputerProgram.pdf) · [Moulin and the portrait](../research/sources.md#s147)
2. Babbage recalls the error and Lovelace’s intervention in chapter VIII of his 1864 memoir. He does not identify the step. [*Passages from the Life of a Philosopher*](https://www.fourmilab.ch/babbage/lpae.html)
3. Turing discusses surprise and gives the voltage illustration under “Lady Lovelace’s Objection” in section 6. [A. M. Turing, “Computing Machinery and Intelligence,” *Mind*, 1950](https://doi.org/10.1093/mind/LIX.236.433) · [Paper facsimile](https://www.cs.unibo.it/~nuzzoles/courses/intelligenza-artificiale/papers/Turing1950.pdf)
4. Brown and colleagues describe autoregressive language modeling and the use of examples in context. Section 3.9.1 and figure G.44 document the arithmetic tests and example. Vaswani and colleagues describe an architecture and its sequential generation. [“Language Models are Few-Shot Learners,” §§2–2.2](https://arxiv.org/abs/2005.14165) · [“Attention Is All You Need,” §3](https://arxiv.org/abs/1706.03762)
5. The energetic cost depends on the physical implementation of a computation. [David H. Wolpert, “Stochastic thermodynamics of computation”](https://arxiv.org/abs/1905.05669)
6. Shunyu Yao and colleagues describe using Wikipedia queries and retrieved observations on HotpotQA and FEVER. [“ReAct”](https://arxiv.org/abs/2210.03629)
7. Figure 3 in the January 2025 version gives the two counts in the raspberry example. Sections 2–4 report the training data, the cost of fine-tuning and the intervention when generation tries to stop. [Muennighoff and colleagues, *s1: Simple test-time scaling*, especially figure 3](https://arxiv.org/pdf/2501.19393v1#page=4)
8. The three papers distinguish worked examples in a prompt, a short reasoning instruction and training with reinforcement. [Wei and colleagues](https://arxiv.org/abs/2201.11903) · [Kojima and colleagues](https://arxiv.org/abs/2205.11916) · [DeepSeek-AI and colleagues](https://arxiv.org/abs/2501.12948)
9. These comparisons concern the particular models, problems and feedback conditions studied. [Snell and colleagues on allocating computation at inference](https://arxiv.org/abs/2408.03314) · [Huang and colleagues on self-correction](https://arxiv.org/abs/2310.01798)
10. The mishap board identifies the ground-software unit mismatch, the factor of 4.45 and weaknesses in verification and communication. See the review of the loss and the board’s contributing causes. [NASA, Mars Climate Orbiter mishap report](https://discovery.larc.nasa.gov/pdf_files/MCO_report_2.pdf) · [NASA’s record of the loss of contact](https://nssdc.gsfc.nasa.gov/planetary/news/mco_19990923.html)
11. The definition and the distinction between monitoring and recursive self-modeling are developed in [chapter 10](10-the-system-that-models-itself.md). For a learned system whose proposed mathematical steps can be checked independently, see [Hubert and colleagues on AlphaProof](https://www.nature.com/articles/s41586-025-09833-y).
12. The industrial extension of autopoiesis and the energetic preference are the book’s hypotheses. [Varela, Maturana and Uribe](../research/sources.md#s33) · [Chapter 2 on physical gradients and useful work](02-the-gradient-and-the-barrier.md) · [Fuenffinger and the winter cooling change](https://deepmind.google/blog/safety-first-ai-for-autonomous-data-centre-cooling-and-industrial-control/)

---

[← The System That Models Itself](10-the-system-that-models-itself.md) · [Contents](../README.md) · [The Machines That Build the Next Machines →](12-the-machines-that-build-the-next-machines.md)
