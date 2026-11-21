# Chapter 1 — The Square with One Answer

**Part I · How Possibility Becomes Actual**

When I wrote a Sudoku solver, I had to decide which empty square it should fill first. Start at the top left and the first square might allow six digits. The program could fill half the board before it discovered it had guessed wrong. Elsewhere on the board a square might already have only one possible answer.[1]

I wanted the program to find that square. Could a bottleneck also help people make something new? I think it can when it tells them which change would make a difference. There is an easy way to see what that means in a puzzle and a harder one in a mine.

Each row, column and three-by-three box must contain the digits one through nine. Here are two rows of a puzzle. The dots mark blanks. There is one other clue we need, a five in the third square of row seven.

```text
Row 1     8 2 ·  |  9 · 4  |  7 1 6
Row 4     7 1 6  |  8 · 3  |  9 · 4
```

The top row is missing a three and a five. The five lower down in the third column rules out a five beside the two. I can write three there. The square between nine and four must take five.

Look directly below that five, in the middle of the fourth row. This row is missing a two and a five. Until a moment ago it could hold a five in the middle. Now the column already has one. In goes the two, and the five belongs over on the right. One digit printed in the seventh row has helped settle four entries, including two in a row it never touches.

A solver can keep a list of possible digits for each square. Enter a digit and cross it off the lists in the same row, column and box. If a list shrinks to one, fill the square. If it empties, undo a guess. Computer scientists call the rule of choosing the shortest list first *minimum remaining values*.[1][2]

The program has gained something without making any of the other guesses. It can rule them out from what is already on the board. A mine owner faces a less obliging problem. Water in a shaft says nothing about the shape of the machine that might drain it. What it rules out is the value of certain other improvements while the water stays high.

Beside the shaft at Saltom Pit on the Cumberland coast, a low stone wall marks the edge of a circle. Two horses once walked round it, turning a pole seven and a half metres long. The footings of their stable survive. Carlisle Spedding put one of the district’s early steam engines beside that horse walk. Why keep both?[3]

In 1729 Spedding began sinking the pit for Sir James Lowther on a rock platform between the cliffs and the Irish Sea, six metres above sea level. The shaft ran some 480 feet down to reach coal that extended under the sea. Spedding divided the oval shaft down the middle. Coal came up one side on a rope wound round a drum. On the other, the pump rods kept moving even when there was no load ready to raise.[3]

An atmospheric engine was well suited to those rods. Its beam rocked up and down, which was just the motion a pump required. Getting a winding drum to turn smoothly from that motion was harder. Two horses walking round a pole could turn a drum directly. When another pump house went up in 1739, there was still useful work for the horses to do. The better the engine kept the mine dry, the more coal the horses could wind.[3]

An extra winding horse could raise more loads from a dry seam. However fast it turned the drum, it could raise no coal from a seam the men could not enter. Drainage mattered because an improvement there made the effort already spent on horses, shafts and miners worth more. This is one way a constraint can direct invention. It tells people which part of a job it would pay to change first.[3]

Every load came out at the foot of a cliff. A steep track zigzagged up it. In 1731–32 the owners built a small harbour beside the shaft so ships could take the coal directly. Storms damaged it. After 1734 little coal went out that way.[3]

The coal went back underground. A horizontal passage led from the pithead into the cliff to a shaft sunk from the high ground at Ravenhill. A second horse gin wound the coal up. From there a wagonway took it to Whitehaven Harbour. The owners had sunk a shaft just to lift coal the miners had already brought to the surface once.[3]

Saltom’s pumps went on draining the neighboring Howgill workings after the pit’s main years of production. The little harbour, built for an equally urgent need, proved of little use once storms had damaged it. A bottleneck gives people a reason to attempt a particular job. A storm can still defeat their best attempt.[3]

The puzzle and the mine part company at the second shaft. Each digit my solver entered had been implied by the clues before I wrote a line of code. At Ravenhill the reason to dig arose because the men at Saltom had already reached the coal. Their first solution helped create a second problem worth solving. That is the sense in which a bottleneck can contribute to creation.[3]

## Chapter notes

1. The original notes record the author’s Sudoku programming problem. The two rows are an illustration. [Author’s notes](../editorial/notes.md) · [UC Berkeley on choosing a variable by its remaining values](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html) · [S01](../research/sources.md#s01)
2. Phokion G. Kolaitis discusses how the structure of a constraint problem affects its computational difficulty. [“Constraint Satisfaction, Databases, and Logic”](https://ijcai.org/proceedings/2003/277) · [S120](../research/sources.md#s120)
3. Historic England records the shaft partition, horse gin and two pumping houses. The archaeological watching brief traces the damaged harbour, the Ravenhill route and Saltom’s later drainage service. [Saltom site record](https://historicengland.org.uk/listing/the-list/list-entry/1017558) · [North Pennines Archaeology, §§3.2.1–3.2.3](https://archaeologydataservice.ac.uk/catalogue/adsdata/arch-704-1/dissemination/pdf/northpen3-52104_1.pdf) · [S157](../research/sources.md#s157). Chapter 5 follows the historical machines and the people who measured their work. [Robert C. Allen, “Why the industrial revolution was British”](https://doi.org/10.1111/j.1468-0289.2010.00532.x) · [How Disequilibrium Builds a New Pathway](05-how-disequilibrium-builds-a-new-pathway.md)

---

[← The Portrait Behind Glass](prologue.md) · [Contents](../README.md) · [The Gradient and the Barrier →](02-the-gradient-and-the-barrier.md)
