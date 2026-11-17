# Chapter 1 — The Square with One Answer

*The possible is larger than the reachable.*

Do bottlenecks help in creation?

I came to the question through a Sudoku programming challenge. The task was to make a computer fill the empty squares. Each row had to contain the digits one through nine. So did each column and each of the nine smaller boxes. The rules were easy to state. The difficulty was deciding what to do next.

An empty square seemed to invite a guess. Put a number there, move to another square, and continue until the choices either completed the puzzle or collided. A computer could make these attempts much faster than I could. It was tempting to think of the task as a race through possibilities.

What caught my attention was the choice of where to begin. The next square on the page might have six legal candidates. Somewhere else, a square might have only one.

That square required no guess. Filling it could remove a candidate from another square, which could determine another. A small decision could release a succession of further decisions. Much of the work had already been done by the relations among the numbers on the board.

Consider an illustrative square. The digits in its row leave one, four, and seven available. Its column rules out one. Its box rules out seven. Four is the only remaining candidate. Looking at the square alone would tell us almost nothing. Looking at how it belongs to the rest of the puzzle gives us its answer.

The restriction has made a step possible.

Computer scientists call the policy of choosing the unassigned variable with the fewest legal values the minimum-remaining-values heuristic. It can also expose mistakes early: a square with no legal candidate tells the solver that its current branch cannot succeed.[1]

Suppose the solver has reached a point where every remaining square requires a choice. One has two candidates; another has six. Trying the narrow choice first can reveal a conflict before the solver invests in a long chain of assignments elsewhere. Failure becomes useful when it arrives soon enough to redirect the work.

This does not guarantee that the square with two candidates will lead quickly to an answer. A puzzle can have very few solutions and still be difficult. What matters is how its dependencies allow deductions to travel, and how soon a mistaken assignment becomes visible.[2] The useful restriction is one the solver can act on.

The experience changed the question I was asking. Instead of wondering how many attempts a machine could make, I began to wonder how the arrangement could tell it where an attempt would matter.

A completed Sudoku looks improbable if we imagine filling every empty square independently. But independence is precisely what the puzzle denies. A digit placed here changes the choices there. The solver can use those connections to avoid considering arrangements that are already excluded.

There is still work to do. The candidates have to be checked, consequences followed, and mistaken choices reversed. The restriction helps organize that work. It gives the next operation a reason to occur in one place rather than another.

Could something like this happen outside a puzzle? Could a limit help direct activity toward the creation of a new capability?

A mine gives the question a physical setting.

Imagine a coal mine in which water is preventing further work. There is a deposit worth reaching, people able to extract it, and equipment for moving the coal. Yet adding more effort to those operations will accomplish little while the working area remains flooded. Further extraction depends on drainage.

That dependence makes drainage a bottleneck. Here the word names an operation that limits what the rest of an arrangement can accomplish. In Sudoku, the narrow choice can help the solver decide where to work. In the mine, the blocked operation gives the work a target. The mechanisms differ, but both direct attention to a point where a change can have consequences elsewhere.

The mining scene is illustrative, not a reconstruction of one inventor's experience. Its advantage is that it makes the problem specific. The task is to lift water far enough, at a sufficient rate, for long enough to keep the working area usable. A device that moves a little water once will not meet it. A device that needs more fuel or repair than the mine can supply may fail for a different reason.

The obstruction begins to define what a successful machine would have to do.

This is already a considerable narrowing. The people attempting the task do not need to invent every possible machine. They need an arrangement that can sustain a particular movement against a particular load. Existing pumps, ways of transmitting motion, available materials, and workshop skills give them a starting inventory. The water gives those resources a common problem.

A steam-powered pump brings several operations together. Fuel must be supplied, water heated, motion produced and transmitted, and the mine water lifted. Each part can work by itself and still fail to form a useful whole. The machine has to connect them at rates and loads they can sustain together.

The problem therefore gets divided into questions that can be tried. Can the workshop make a component that holds up under use? Can a connection transmit the required motion? Can a leak be reduced enough for the arrangement to operate? Each improvement matters through its effect on the pumping task. A beautiful component that does not help keep the mine clear has missed the target.

Drainage has given invention both a direction and a test. Water removed and a working area kept usable are consequences against which a proposed solution can be judged.

But the mine must support the attempt before the machine delivers those consequences. Materials and labor are consumed during construction. A trial can reveal another defect. Repairs take time. The resources needed to continue have to come from somewhere already accessible. The coal still under water cannot feed the boiler needed to reach it.

The amount of support available can change which designs are worth attempting. A fuel-hungry pump may be usable where fuel is cheap enough and the work it replaces is costly enough. Robert Allen's account of early British industrialization gives a prominent role to this relation between expensive labor and cheap energy.[3] For the present question, the important point is conditional: a machine's shortcomings can be bearable in one setting and prohibitive in another.

An imperfect first version may therefore have a place to operate. It can do enough useful pumping to justify continued use while further changes are tried. That gives development something to work with: a running arrangement, particular defects, and a reason to improve it.

The bottleneck helps explain why effort is directed toward drainage. The surrounding resources help explain how that effort can continue. A working pump requires both a problem that gives the attempt a purpose and conditions under which the attempt can be carried through.

Suppose the pump runs through a shift. Water keeps entering the mine. For the first time the crew sees the waterline drop below the seam and stay there long enough to work. Yesterday the test was whether the engine could lift water. Today someone can ask what to do with the first load of coal.

Set aside some coal for the next firing. The rest can go to market. As the engine works, a second kind of return accumulates beside the shaft. Someone learns which seal starts to leak, how long the pump can stand idle, and which repair is worth making before the next shift.

If that knowledge is retained, the next machine begins from a different position. Its builders can use dimensions that have been tried, connections that have worked, and records of failures they need not repeat. A workshop capable of repairing the pump has acquired capabilities that did not exist merely because the original problem was urgent.

The return can also help keep the machine in existence. If the coal newly reached supports fuel, repairs, and the work of building another pump, the successful arrangement has gained a means of continuing. The proposal we will follow is that assemblies opening greater access to usable energy tend to gain this advantage: they can support more of the work needed to maintain and reproduce their capabilities. More coal reached does not ensure that the return is used that way. The connection must actually be made.

This is the creation at issue here: an arrangement gains something it can now do. The pump turns existing materials, skills, and fuel into a capacity for sustained drainage. The capacity changes access to resources. Its operation can also leave behind knowledge and equipment that make further construction easier.

The completed assembly becomes part of the starting conditions for another assembly.

In Sudoku, filling a square changes the candidates elsewhere. In the mine, successful pumping changes which work can be attempted at all. A deeper working area may become accessible. Another mine may become a plausible site for a similar machine. A proposed improvement can be judged against an operating example instead of being an entirely unsupported conjecture.

These are possibilities, not an automatic sequence. The new workings may be disappointing. The pump may be too difficult to maintain. Knowledge may remain with one person and disappear when that person leaves. To carry a capability forward, something of the achievement has to remain usable.

A practical question follows each apparent success: what does it leave available for the next attempt?

More coal is one answer. A reliable component is another. So is a method of repair that a second worker can learn. These gains differ, but each can change the cost or feasibility of what comes next. The importance of the first machine lies partly in that altered starting point.

This also shows why we should be careful about calling the bottleneck creative. Water in a mine can stop work permanently. A tighter restriction can exhaust the resources that might have supported a solution. The presence of a valuable deposit does not guarantee the knowledge needed to reach it.

Consider three versions of the same illustrative mine. In the first, existing drainage is adequate. There may be little reason to incur the cost of developing a different pump. In the second, drainage limits extraction, but enough accessible resources remain to sustain trials. A new pump has a useful function and support for its development. In the third, flooding has left no means to pay for construction or keep the workforce together. The need is most urgent where the ability to respond is weakest.

This comparison suggests a condition under which a bottleneck might help: it concentrates effort on an important dependency while leaving enough capacity to attempt a change. It also suggests a way the claim could fail. A restriction may reduce investment, scatter skills, or eliminate workable options faster than it directs invention.

To find out what happened historically, we would need more than a successful engine beside a once-flooded mine. We would need to examine unsuccessful attempts, places where drainage posed less of a problem, and differences in the resources available to respond. Otherwise we would be crediting the obstacle for a result that might have occurred without it. The book's proposed historical comparisons are intended to investigate that distinction.[4]

There is another possibility: the obstruction can be removed using a capability that already exists. Hiring an available pumping service might restore production without creating a new kind of machine. That can be an excellent response. But it answers a different question from the one with which we began. To explain creation, we need to identify what was developed, how the restriction contributed to its development, and what the resulting arrangement could do that it could not do before.

The Sudoku solver makes this distinction easier to see. The puzzle's rules and permitted solutions are already fixed. The solver constructs an answer within them. At the mine, the useful response may require building equipment that changes the practical range of future activity. The first example shows how a restriction can guide work; the second asks how guided work can produce a capacity that outlasts the original problem.

The connection is strongest when we can follow the intervening steps. A limit makes a dependency visible, or additional resources make an attempt feasible. An assembly forms. Its useful return can support maintenance and repeated construction. The retained capability then changes the conditions of the next attempt. A successful pump does more than answer the flooded mine: it can help supply the work from which another answer will be built.

Each step adds something the previous one could not supply. A target does not provide materials. Materials do not provide a working connection. A working connection does not ensure that anyone can repair or reproduce it. Creation depends on getting the steps to hold together.

When I looked at the Sudoku square with one candidate, the answer became easier to find because the rest of the puzzle was already there. The square gathered the consequences of an existing arrangement into a place where the next move was clear.

The flooded mine presents a more demanding version of that situation. The next move is not written anywhere. The obstruction identifies work worth attempting, while the equipment and skills around it make some attempts feasible. If a pump can be assembled and sustained, the result becomes part of what is available thereafter.

Do bottlenecks help in creation? They can help give work a direction, concentrate the alternatives worth trying, and make a useful result recognizable. Their contribution depends on the means to act and on what the action leaves behind. The creative event is the successful passage from a limiting dependency to a new capacity.

The water still has to be lifted. A clear target cannot supply the work needed to reach it. To follow the story further, we must ask what can drive the machine, and how that driving difference becomes useful motion.

We begin with a hot object, a cold object, and the difference between them.

## Chapter notes

1. [Russell and Norvig, constraint satisfaction](https://aima.cs.berkeley.edu/4th-ed/pdfs/newchap05.pdf), and [UC Berkeley CS188, variable ordering](https://inst.eecs.berkeley.edu/~cs188/textbook/csp/ordering.html). The opening experience is drawn from the author's notes. The candidate-set example illustrates the heuristic; it is not a reconstruction of that particular puzzle or a performance benchmark.

2. **Constraints and search structure.** Phokion G. Kolaitis, [“Constraint Satisfaction, Databases, and Logic”](https://ijcai.org/proceedings/2003/277) (2003), discusses how the structure of dependencies affects tractability. This supports the distinction between counting solutions and organizing a search. The comparison with physical invention belongs to the book. See [S120](../research/sources.md#s120).

3. [Robert C. Allen, “Why the industrial revolution was British”](https://doi.org/10.1111/j.1468-0289.2010.00532.x). Supports the conditional argument about labor costs, energy prices, and the viability of early machinery. The mine and its three variants are illustrative; no specific sequence of trials, quoted testimony, or measured effect is claimed. Chapter 5 develops the historical explanation and its alternatives.

4. **Empirical research design (S108).** The proposed comparison concerns the Napoleonic blockade and French mechanized cotton spinning: whether a trade restriction helped make a previously uncompetitive local capability viable. The [specification](../scripts/experiments.json) and [research guide](../scripts/README.md) state the assumptions; the [run report](../scripts/results/chapter01.json) still records missing inputs. This is a proposed test of a component mechanism, not evidence that the mine illustration establishes a causal effect.

---

[← The Machine Waiting for Electricity](prologue.md) · [Contents](../README.md) · [The Gradient and the Barrier →](02-the-gradient-and-the-barrier.md)
