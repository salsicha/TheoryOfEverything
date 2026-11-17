# Chapter 1 — The Square with One Answer

**Part I · How Possibility Becomes Actual**

*The possible is larger than the reachable.*

Do bottlenecks help in creation?

When I was writing a Sudoku solver, two blank squares could look alike and ask very different things of the machine. One offered half a dozen ways to get into trouble. The other had so little room left that it could give away half a row.

Try a few squares. In Sudoku, each row, each column, and each three-by-three box must contain the digits one through nine. Here are two rows from a possible board. The dots are empty squares. One other clue will be enough. Farther down the third column, someone has already entered a five.

```text
Row 1     8 2 ·  |  9 · 4  |  7 1 6
Row 3     7 1 6  |  8 · 3  |  9 · 4
```

Start with the first gap in row one. The row is missing three and five. The five downstairs settles which one goes here. Write three. That leaves five for the gap between nine and four. Now look straight down from the five you have just written. The gap between eight and three in row three could have held a two or a five. It has to be two. The last gap in that row takes five. Four squares have filled in, and you haven’t made a guess.

What changed while you were doing that? Every digit you needed was implied by marks already on the board. Yet the last five was easier to see after the first three went in. Writing the three did some work for you. It brought a consequence within reach of the next small operation.

The useful change in my program was to let the puzzle choose the square. Count the legal candidates for each empty square and go first to the one with the fewest. A single candidate gives a move. An empty list tells the program to back up. Even if the narrowest square still has two candidates, an unfortunate guess there may reveal its consequences while there is comparatively little to undo. Computer scientists call this the minimum-remaining-values heuristic.[1] Its usefulness depends on how the squares constrain one another. A puzzle with a unique answer can still be very hard.[2]

I had been given the rules, the board, and enough electricity to run the program. The question I took away concerned the first of those gifts. Could a restriction help people find something they could build, in a situation where nobody had prepared an answer for them to find?

Imagine a coal mine. An upper working still produces enough to keep the crew employed. Below it lies another seam. Water has risen across the passage to it. There are people who can cut coal here, carts that can carry it, and a buyer. Another cart would join the others standing empty.

The water gives the crew a specification. Enough must come out to lower the level past the passage. Since more keeps coming in, a working shift has to be won against the inflow. A pump could raise a magnificent jet at the shaft mouth and leave the passage every bit as wet at the end of the day. Mark the water level on the shaft wall before the first stroke. Come back at the end of the shift and see how much of the wall below the mark has come into view.

With that mark, a great many imaginable improvements lose their appeal. A faster stroke is worth trying if the pump can fill again between strokes. A modest repair to a valve may matter more if half the water lifted on each stroke runs back down. The crew can compare both ideas against the same wet wall. The flooding has done something quite precise for invention. Before anyone has built a working pump, the crew knows how to judge a design.

Now comes the bill. Suppose the crew can put together a steam engine to drive the pump. Even the first unsuccessful firing will burn coal. Somebody has to bring fuel from the upper working, and somebody has to be paid to fit the valve again tomorrow. A mine with cheap coal to hand can afford to learn something from a wasteful engine. At a mine paying dearly for every load, exactly the same performance might end the trial. This difference in what a first machine costs its users features in Robert Allen’s account of early British steam power.[3]

Give the imagined crew a little time. The valve holds. A hand’s breadth of wet stone shows below the mark. Toward the end of a shift the water drops below the passage and someone walks in where no one could work the day before. Until that moment, each firing had used fuel won by the old means. The first cart out can carry some of the fuel for the next firing. It can also go to a buyer who will pay for a spare rod. Yesterday the lower seam could pay for neither.

The spare rod is easy to overlook. It does nothing on the day it arrives. Later a rod breaks while water is still coming in. A fitter who has the spare to hand can start work at once. If someone has kept the dimensions and shown a second fitter how to make the joint, the workshop now has something to offer the next mine as well. One mine set out to clear a passage. Among the possible results is a workshop that knows how to keep two passages clear. There was no square on the original board for that workshop.

Change the timing slightly. Suppose the water cuts off the upper working a week before the valve holds. The fuel for the next trial was going to come from there. The problem is now even more narrowly defined. The crew knows where to work and has lost the means of working there. Left to flood, this shaft would deserve a place in any history of what bottlenecks do, alongside the one with the pump on display.

In the puzzle, the first three was there to be found, and finding it made the next choice easier. At the mine, people had to make a pump that ran long enough to give them a choice they had never had. The bottleneck helped while it gave their effort a direction and left enough room for a failure, a repair, and another try. What it cost to take those steps depended, from the first stroke to the last, on something the waterline could tell them very little about. Where would the work to lift the water come from?

## Chapter notes

1. The author’s Sudoku programming challenge and the decision to prioritize the most constrained squares are recorded in the [source notes](../editorial/notes.md). The two rows here are a fresh illustration. For the heuristic see [UC Berkeley CS188 on variable ordering](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html) and [S01](../research/sources.md#s01).

2. Phokion G. Kolaitis discusses the relation between the structure of a constraint problem and its computational difficulty. [“Constraint Satisfaction, Databases, and Logic”](https://ijcai.org/proceedings/2003/277) · [S120](../research/sources.md#s120)

3. The flooded seam, waterline mark, trials, and spare rod belong to the imagined mine. For the historical argument about the relative prices of energy and labor, see [Robert C. Allen, “Why the industrial revolution was British”](https://doi.org/10.1111/j.1468-0289.2010.00532.x). [Chapter 5](05-how-disequilibrium-builds-a-new-pathway.md) follows the historical engines and measurements.

---

[← The Machine Waiting for Electricity](prologue.md) · [Contents](../README.md) · [The Gradient and the Barrier →](02-the-gradient-and-the-barrier.md)
