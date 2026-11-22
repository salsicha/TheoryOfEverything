# Chapter 2 — The Square with One Answer

*Part I · Physics*

When I wrote a Sudoku solver, the first empty square gave me a bad place to start. Six digits might fit there. The program could fill half the board before a contradiction sent it back to try the second one. Elsewhere on the same board a square might already have its answer. The cost of solving the puzzle depended on whether the program could find that square first.[1]

Here are two rows. Farther down, in the third square of row seven, the puzzle setter has printed a five.

~~~text
Row 1     8 2 ·  |  9 · 4  |  7 1 6
Row 4     7 1 6  |  8 · 3  |  9 · 4
~~~

The first row lacks a three and a five. The five down below rules one of them out of the third column. Write three beside the two. That leaves five for the square between nine and four. Now look straight down from the new five to the gap in the middle of row four. Row four needs a two and a five. Its middle square must take two. The five goes over on the right.

A mark in the seventh row settled four entries without ever touching the fourth row. Ink did nothing at a distance. The change passed through a set of relations that hold for the solver who copies the puzzle onto another sheet or puts it into a machine. This is what I mean by a constraint in *Platonic space*. Specify the rows, columns, boxes and entries and some continuations cease to exist as solutions. A second solver can exploit the same constraint without knowing that I wrote a program.[1]

The program can keep a list beside each vacant square, cross off a digit after a move and start its next search where the fewest possibilities remain. An empty list reveals an earlier mistake. This rule will sometimes save an enormous amount of work. Other boards still require branching and a return to a previous choice. There is no promise that constraints always make a problem easy. The claim is that counting every string of digits gives a poor estimate of the work required to solve this particular board.[1]

## The flask that went cloudy

In January 2003 Tim Cooper came across a flask that was too cloudy. Richard Lenski’s group had been following twelve populations of bacteria since 1988. They descended from the same stock and received the same small allowance of glucose. The density of growth had become familiar enough for a surprising flask to suggest contamination. Someone checked whose bacteria they were.[2]

They belonged to the population that was supposed to be there. Its ancestors had grown with oxygen on glucose. The flasks also contained citrate, added to keep iron available. The ancestral cells had no effective way to grow aerobically on that supply of carbon. Descendants in one flask had acquired one. What looked like an intruder was evidence that an old inhabitant had gained admission to a second food supply.[2]

The great advantage of this particular accident was a freezer. Lenski’s group had preserved samples from earlier generations. Zachary Blount and his colleagues could bring those ancestors back, give their descendants another run at the opportunity, and ask whether the odds had always been the same. Descendants of certain later ancestors acquired the trait more readily than descendants of earlier ones. A weak ability had appeared by around generation 31,500 in the historical population. Further changes helped produce the dense growth Cooper saw.[2]

What could the cells in Cooper’s flask do that morning? Two ways of making a living were open in the same oxygenated broth. Some cells could consume the day’s glucose and grow until it ran short. Cells with the new inherited capacity could also draw on the citrate left in the flask. They could use it during hours in which an exclusively glucose-fed population had little left to process. A third possibility actually arose. The citrate users released compounds that neighbors could consume. Different lineages could work on successive portions of the same chemical supply.[2]

Follow one day’s ration from the time it enters the flask until the next transfer. A population that leaves citrate in tomorrow’s discarded liquid passes up some of the work this food could supply. A mixed population can recover more if one cell takes up what another releases before the day is out. Whether that arrangement spreads depends on the return to the lineages that must build and maintain the machinery. Once the usable food is exhausted, adding more cells cannot raise the daily supply.[2]

The cloudy flask recorded more growth. Where did the rest of the energy go? Carbon carried out in new cells or discarded products still has chemical value. For the book’s claim the decisive comparison is the free energy lost across the whole flask per day at the same temperature, including what leaves at transfer. A community that left more descendants while sending more usable energy out in that bottle could win the competition and lose the thermodynamic comparison. The dense growth establishes that a new route worked. Its advantage in entropy production depends on what went down the drain.[2]

The frozen ancestors let us date the change in what was feasible. Early cells confronted the same citrate with different equipment. The interval of roughly 31,500 generations before the weak trait appeared belongs in the history of building that equipment. Comparisons after it appeared can ask which combinations made the most of the next ration. Counting all the imaginable bacterial genomes would answer neither question.[2]

The mark in row seven still explains why a three belongs in the first row. It cannot explain why a physical system should move from one admissible state to another. For that we need something a sheet of paper does not supply. In a laboratory in the Netherlands it came from a motor bolted beneath a tube.

## Notes

1. The puzzle comes from the author’s notes and the earlier manuscript. [Constraint propagation and variable ordering](../../research/sources.md#s01) · [Limits of search heuristics](../../research/sources.md#s120)

2. Blount, Borland and Lenski report the timing, daily transfers and replay comparisons. Later work documents resource exchange between lineages. The daily free-energy balance is the book’s proposed comparison. Culture density and reproductive fitness are separate observations. [Primary replay paper](https://doi.org/10.1073/pnas.0803151105) · [Resource use and cross-feeding](../03-life-makes-its-conditions.md#chapter-notes) · [Working sources](../../research/sources.md#s03)

---

[← What Moves at Absolute Zero?](01-what-moves-at-absolute-zero.md) · [Contents](../../README.md#contents) · [Why the Beads Choose a Side →](03-why-the-beads-choose-a-side.md)
