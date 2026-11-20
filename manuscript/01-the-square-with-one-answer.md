# Chapter 1 — The Square with One Answer

**Part I · How Possibility Becomes Actual**

When I wrote a Sudoku solver, I had to decide where it should start. The easiest instruction to write was to take the first empty square in the top row. On some boards that square allowed six digits. The program could make five wrong guesses before it tried the right one.

Elsewhere on the same board there might be a square with just one legal digit. Starting there could save work on several other squares. That led me to a broader question. Can a bottleneck help us create something?

Two rows show what the program could establish before it had to guess. Each row, column and three-by-three box must contain the digits one through nine. The dots mark blanks. In the seventh row the third square already contains a five.

```text
Row 1     8 2 ·  |  9 · 4  |  7 1 6
Row 4     7 1 6  |  8 · 3  |  9 · 4
```

The first row lacks a three and a five. The blank after the two is in a column that already contains a five, so it must take three. The other blank takes five. Directly below it, the middle blank in row four can now take only two. The last blank takes five. Knowing where one digit couldn’t go settled four entries.

My program counted the legal digits in each blank and chose the one with the fewest left. Computer scientists call this the *minimum-remaining-values* rule. If the smallest remaining set contains two digits, my program tries one. If that leaves another square with no legal digit, it can go back at once. It saves time because filling one square changes the choices in others.[1][2]

At Whitehaven the difficulty was equally easy to identify. Miners knew there was coal below them. Water was getting into the workings faster than they could remove it. Carlisle Spedding had to build something that would let the men reach the seam.

Spedding sank Saltom Pit for Sir James Lowther on a strip of rock between the Cumberland cliffs and the Irish Sea. He divided its oval shaft down the middle. Water came up one side, coal up the other. On the surface two horses walked in a circle, turning the drum that wound up the coal. Beside them stood an engine house built in 1731. Its steam engine pumped the water.[3]

The horses could raise coal once the miners had cut and loaded it. What held up the work was the water below. A second pumping house followed in 1739. The owners were still using horses for the work the horses could do.[3]

There was little room for a road between the pit and the sea. A track climbed the cliff in a zigzag. In 1731–32 the owners built a small harbour so that ships could take on coal at the pit. Storms damaged it repeatedly. After 1734 it was barely used.[3]

The coal went back underground. From the pithead it traveled along a passage to the foot of Ravenhill shaft. Horses there wound it up to the top of the cliff. A wagonway carried it the rest of the way to Whitehaven Harbour.[3]

Saltom kept draining neighboring workings at Howgill after its main period of coal production ended. An engine installed to open one shaft helped miners work a larger part of the coalfield.[3]

Flooding helped direct invention at Saltom. Everybody knew what an engine had to do, and Lowther could afford to try it. The damaged harbour explains why that matters. Shipping was just as serious a problem. The owners spent money on it too. They gained a dependable route to port only when they found a way through the cliff.

In Sudoku, the four digits were already determined. At Saltom the miners had to build the pump and the passage. When they finished, they could mine coal their predecessors had left under water.[3]

## Chapter notes

1. The original notes record the author’s Sudoku programming problem. The two rows are an illustration. [Author’s notes](../editorial/notes.md) · [UC Berkeley on choosing a variable by its remaining values](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html) · [S01](../research/sources.md#s01)
2. Phokion G. Kolaitis discusses how the structure of a constraint problem affects its computational difficulty. [“Constraint Satisfaction, Databases, and Logic”](https://ijcai.org/proceedings/2003/277) · [S120](../research/sources.md#s120)
3. Historic England records the shaft partition, horse gin and two pumping houses. The archaeological watching brief traces the damaged harbour, the Ravenhill route and Saltom’s later drainage service. [Saltom site record](https://historicengland.org.uk/listing/the-list/list-entry/1017558) · [North Pennines Archaeology, §§3.2.1–3.2.3](https://archaeologydataservice.ac.uk/catalogue/adsdata/arch-704-1/dissemination/pdf/northpen3-52104_1.pdf) · [S157](../research/sources.md#s157). Chapter 5 follows the historical machines and the people who measured their work. [Robert C. Allen, “Why the industrial revolution was British”](https://doi.org/10.1111/j.1468-0289.2010.00532.x) · [How Disequilibrium Builds a New Pathway](05-how-disequilibrium-builds-a-new-pathway.md)

---

[← The Portrait Behind Glass](prologue.md) · [Contents](../README.md) · [The Gradient and the Barrier →](02-the-gradient-and-the-barrier.md)
