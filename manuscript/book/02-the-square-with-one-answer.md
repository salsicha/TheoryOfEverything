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

The citrate had been available to all twelve populations. The amount of energy available *to a cell* depended on its inherited machinery. One change let a transport function operate under conditions in which it had previously been of little use. It reused something the cell’s ancestors already possessed. Subsequent changes could improve access now that there was some access to improve. A history of that kind has different odds from assembling the finished machinery in one draw.[2]

There is a sharp limit to the Sudoku comparison. A setter has decided what belongs in the bottom corner before the solver buys the newspaper. The bacteria had ancestors and neighbors. Once some of them used the citrate, compounds they released gave other lineages a new source of food. A move in one lineage changed the board on which its neighbors lived. A researcher hoping to anticipate the next change would need to measure what was in the flask again.[2]

The difference is decisive for the thesis. Some constraints hold wherever the arrangement recurs. A cell cannot spend energy from a nutrient to which it has no metabolic access. Which nutrient is out of reach, and which change can put it within reach, depend on the equipment and surroundings that exist at that time. Evolution need never know what a possible space of organisms looks like. In each generation it encounters the costs and benefits of a few reachable changes. The freezer can reveal how those possibilities themselves have a history.

In a supplied flask, a change that lets a cell use more food can help it leave more descendants with the same ability. It can also cost more than it earns when the food changes. That is a claim about a return a lineage can spend on reproduction. The energy does not choose a mutation in advance. If descendants of every frozen ancestor had acquired the trait at the same rate, the case for a changing constraint would be weaker. If all twelve flasks had gone cloudy on the same morning, we would want a different account of the role of chance.[2]

The mark in row seven still explains why a three belongs in the first row. It cannot explain why a physical system should move from one admissible state to another. For that we need something a sheet of paper does not supply. In a laboratory in the Netherlands it came from a motor bolted beneath a tube.

## Notes

1. The puzzle comes from the author’s notes and the earlier manuscript. [Constraint propagation and variable ordering](../../research/sources.md#s01) · [Limits of search heuristics](../../research/sources.md#s120)

2. Blount, Borland and Lenski report the replay comparisons. Related work traced the mechanistic changes and the resources released to neighbors. [Long-term experiment and replay](../../research/sources.md#s03) · [Primary replay paper](https://doi.org/10.1073/pnas.0803151105) · [Growth and cross-feeding sources](../03-life-makes-its-conditions.md#chapter-notes)

---

[← What Moves at Absolute Zero?](01-what-moves-at-absolute-zero.md) · [Contents](../../README.md#contents) · [Why the Beads Choose a Side →](03-why-the-beads-choose-a-side.md)
