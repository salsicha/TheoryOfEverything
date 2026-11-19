# Chapter 1 — The Square with One Answer

**Part I · How Possibility Becomes Actual**

*The possible is larger than the reachable.*

The top left was an obvious place for a program to begin a Sudoku puzzle. It had one advantage. I knew where to tell the computer to look. The puzzle itself gave that square no special standing.

When I wrote a program to solve these puzzles, the computer would cheerfully start anywhere I told it to. A blank with six legal digits could send it a long way down five wrong paths. The square I came to value was the one with the least freedom. It suggested a question that seemed worth asking outside the puzzle. Can a bottleneck help us create something?

Two rows show what the program could establish before it had to guess. Each row, column and three-by-three box must contain the digits one through nine. The dots mark blanks. In the seventh row the third square already contains a five.

```text
Row 1     8 2 ·  |  9 · 4  |  7 1 6
Row 4     7 1 6  |  8 · 3  |  9 · 4
```

Either three or five fits between the nine and the four in the first row. The same two digits are missing from the gap after the two, with one important difference. The five downstairs rules it out there. That gap takes three, leaving five between the nine and the four. The new five settles the gap in the fourth row directly beneath it, which must take two. Its last gap gets five. Four entries follow from a single exclusion.

The last five was implied before the first entry went in. What changed was the cost of finding it. Choosing the square with the least freedom let one small piece of work pay for the next.

In my program this amounted to counting the candidates for each blank and choosing the square with the fewest left. Computer scientists call it the *minimum-remaining-values* rule. Sometimes the narrowest square still offers two possibilities. A guess there can expose a mistake while there is little to erase. Sometimes the count comes to zero, splendid news if the alternative is to spend the afternoon filling in the rest of a board on which a mistake has already been made. Hard puzzles survive this treatment. The advantage comes from the way the squares bear on one another.[1][2]

A person who writes a Sudoku solver enjoys a privilege that Carlisle Spedding did not. The puzzle comes with a solution. In the coalfield at Whitehaven, the obstruction was plain enough. Water collected in the workings. The solution would have to be built, and once built it was going to need fuel, attention and repairs.

Spedding sank Saltom Pit for Sir James Lowther on a strip of rock between the Cumberland cliffs and the Irish Sea. The shaft had an oval section and a division down the middle. Water came up one side. Coal came up the other. At the surface the remains of a circular horse walk lie beside the shaft. Two horses turned a drum to wind the coal. An engine house built in 1731 held an atmospheric engine that pumped the water. An owner ready to spend money on steam had retained horses within a few yards of his new machinery.[3]

That division in a single shaft tells us where the bottleneck lay. The horses could raise coal once people had cut and loaded it. Water arriving underground could keep them from ever getting to that point. Faster winding at the surface would have made little difference to a flooded working. Adding pumping capacity at the right place changed what all the other hands and horses could accomplish. An engine house for a second pump followed in 1739.[3]

The first working pump overturned none of the geography above ground. Saltom had little room for a road. The way out by land climbed the cliff in a zigzag. The proprietors built a small harbour in 1731–32 so that the coal could leave directly by sea. Storms repeatedly damaged it. By the middle of the decade it was little used. Pumping had put coal on a shelf of rock from which it was still remarkably difficult to sell.[3]

The coal went back underground. A passage behind the pithead took it to the foot of another shaft, at Ravenhill. There a horse gin wound it up the cliff. A wagonway could then carry it to Whitehaven Harbour. The archaeologists who documented the site traced a journey with two ascents separated by a stretch where the coal went into the hillside again. Each part of that otherwise peculiar route answers to a different obstruction.[3]

A pump had changed the value of a horse at the top of a cliff. Once the drainage worked, an investment in transport could deliver coal the older workings had left beyond reach. In turn, drainage at Saltom served the wider Howgill colliery. Its usefulness as a pumping station outlasted its main period of coal production. Spedding had helped build an installation whose neighbors could use it for purposes the first shaft alone could never have supported.[3]

This is my answer to the question about bottlenecks. Flooding concentrated effort on an operation that held up many others. Cheap fuel and an owner prepared to pay supplied the means to act on that knowledge. The harbour at Saltom gives the explanation some teeth. A serious obstacle drew capital there too, and the sea repeatedly undid the work. A constraint helps creation when the arrangement that meets it also opens a practicable route to the next operation.

The five in the Sudoku column made four entries cheaper to find. It had been there the whole time. The path through Ravenhill had to be made, and once it existed it changed the prospects of people working elsewhere on the coast. How did burning coal on the shore begin to do the work of lifting water from below the sea?[3]

## Chapter notes

1. The original notes record the author’s Sudoku programming problem. The two rows are an illustration. [Author’s notes](../editorial/notes.md) · [UC Berkeley on choosing a variable by its remaining values](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html) · [S01](../research/sources.md#s01)
2. Phokion G. Kolaitis discusses how the structure of a constraint problem affects its computational difficulty. [“Constraint Satisfaction, Databases, and Logic”](https://ijcai.org/proceedings/2003/277) · [S120](../research/sources.md#s120)
3. Historic England records the shaft partition, horse gin and two pumping houses. The archaeological watching brief traces the damaged harbour, the Ravenhill route and Saltom’s later drainage service. [Saltom site record](https://historicengland.org.uk/listing/the-list/list-entry/1017558) · [North Pennines Archaeology, §§3.2.1–3.2.3](https://archaeologydataservice.ac.uk/catalogue/adsdata/arch-704-1/dissemination/pdf/northpen3-52104_1.pdf) · [S157](../research/sources.md#s157). Chapter 5 follows the historical machines and the people who measured their work. [Robert C. Allen, “Why the industrial revolution was British”](https://doi.org/10.1111/j.1468-0289.2010.00532.x) · [How Disequilibrium Builds a New Pathway](05-how-disequilibrium-builds-a-new-pathway.md)

---

[← The Portrait Behind Glass](prologue.md) · [Contents](../README.md) · [The Gradient and the Barrier →](02-the-gradient-and-the-barrier.md)
