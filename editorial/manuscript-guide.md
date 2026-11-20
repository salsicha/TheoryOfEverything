# Manuscript guide

| File | Purpose |
| --- | --- |
| [notes](notes.md) | Original source notes with a dated author clarification appended |
| [ideas](ideas.md) | Expanded ideas I01–I77 and current coverage map |
| [outline](outline.md) | Current twelve-chapter sequence, section plans, and causal argument |
| [sources.md](../research/sources.md) | Source keys S01–S160, evidence limits, and outstanding research |
| [Natural-experiment scripts](../scripts/README.md) | Twelve evidence records, with estimators, data contracts, and explicit identification limits |
| [Experiment results](../scripts/results/summary.md) | Completed comparisons, diagnostic checks, and explicit missing-data statuses |
| [Dataset search audit](../scripts/dataset-search.md) | Located primary data, access limits, and the observations still needed |
| [Parked material](archive/parked-material.md) | Earlier displaced philosophical, historical, and policy discussions |
| [Earlier case studies](archive/earlier-case-studies.md) | Full grid, housing, and Montreal chapters replaced or condensed in this revision |
| [Institutional background](archive/institutional-background.md) | Former chapter 10, preserved before the autopoiesis revision |
| [Historical drafts](archive/historical-drafts/README.md) | Complete former grain, steam, ammonia, and factory chapters, with their original numbering |
| [Human-development revision](archive/human-development-revision.md) | Complete constraint-transformation and self-domestication drafts before their merger into then-chapter 7 (now chapter 7) |
| [Cognition chapter plans](archive/cognition-chapter-plans.md) | Former chapter 10 and 11 outlines preserved before full prose drafting |

## Mathematical support in the prose

The chapters use constraint satisfaction, nonlinear dynamics, autocatalytic and production networks, predictive complexity, control theory, thermodynamics of computation, and technological combination to sharpen their mechanisms. The prose explains these through existing scenes and short examples. Technical assumptions and attribution sit in chapter notes, [sources S120–S127](../research/sources.md#s120), and the afterword. The additions distinguish accessibility, stability, maintenance, prediction, and regulation; they do not turn every form of complexity into the same quantity or change the status of the empirical results.

## Draft extent

The prologue, twelve drafted chapters, and epilogue contain **23,603 words** before notes. The methodological afterword adds **2,878**, for **26,481 words** of drafted prose in the reading sequence. Counts use whitespace-separated words and include titles, part headings and epigraphs. Plates, navigation, source notes and research appendices are excluded.

The original 65,000–80,000-word ambition remains a possible longer revision. Expansion should add explanatory mechanisms, historical depth, and discriminating comparisons.

| Section | Words before notes |
| --- | ---: |
| [prologue](../manuscript/prologue.md) | 637 |
| [chapter1](../manuscript/01-the-square-with-one-answer.md) | 665 |
| [chapter2](../manuscript/02-the-gradient-and-the-barrier.md) | 1,304 |
| [chapter3](../manuscript/03-life-makes-its-conditions.md) | 1,963 |
| [chapter4](../manuscript/04-the-discovery-that-became-possible.md) | 1,825 |
| [chapter5](../manuscript/05-how-disequilibrium-builds-a-new-pathway.md) | 2,221 |
| [chapter6](../manuscript/06-from-uncertainty-to-an-assembled-universe.md) | 2,642 |
| [chapter7](../manuscript/07-the-species-that-changed-its-own-conditions.md) | 1,955 |
| [chapter8](../manuscript/08-the-world-that-learned-to-think.md) | 1,583 |
| [chapter9](../manuscript/09-the-system-that-produces-its-tomorrow.md) | 2,332 |
| [chapter10](../manuscript/10-the-system-that-models-itself.md) | 1,937 |
| [chapter11](../manuscript/11-why-the-world-builds-artificial-intelligence.md) | 1,625 |
| [chapter12](../manuscript/12-the-machines-that-build-the-next-machines.md) | 1,763 |
| [epilogue](../manuscript/epilogue.md) | 1,151 |
| [afterword](../manuscript/afterword.md) | 2,878 |

## Writing conventions

Begin with a person confronting a particular problem in an identifiable place, or with an observation, object or document whose maker can be identified. Use plain language for what each person saw, decided and did. Let the physical detail or the decision raise the question the chapter answers. Why were horses still winding at Saltom with steam engines beside them? Why did a weaver who already had the cards for one portrait need a painter for the next? Follow the decisions and their consequences before giving the relation a name.

Where a case permits more than one explanation, identify what each would lead us to expect, then return to a feature of the record that can help decide between them. Graeber and Wengrow introduce schismogenesis through the institutions of neighboring peoples and the historical possibility of deliberate differentiation. Take that argumentative move as a craft reference. Attribute a historical investigator’s thought experiment to its author. Keep prospective tests in the afterword and the manuscript’s own natural experiments in the research companion. [Wengrow on the comparison](https://discovery.ucl.ac.uk/id/eprint/10192232/2/Wengrow_Historical_Materialism_DoE.pdf) · [Companion methods](../research/causal-inference.md) · [Evidence by chapter](../research/evidence.md)

Separate established observations, disputed interpretations, the book's causal hypothesis, and proposed tests. Energy, power, entropy production, useful work, reproduction, profit, and welfare require distinct accounting. State the system boundary, alternatives, and timescale. Do not invent dialogue, measurements, quotations, or empirical validation.

Preserve the distinction between conceptual contradiction and physical disequilibrium. Einstein's dialectical interpretation belongs to the book; relativity and wave–particle duality have distinct histories. State the proposed natural emergence of AI and data centers directly, then specify the mechanisms, prerequisites, and comparisons through which it can be tested. Their particular date, architecture, ownership, and uses require separate explanations. State that the universe and fundamental constants are probably assembled as the book's working conjecture; neither a numerical probability nor a derivation has been established.

Distinguish hierarchy, recurrence, recursive procedures, and self-modeling. A functional self-model does not by itself establish subjective experience. Trace the shift from explicit logical programs to learned representations without erasing the uses of formal methods. Keep learning-loss gradients separate from physical disequilibrium, and connect task improvements to actual physical consequences before drawing energetic conclusions.

Distinguish a model from its executing service, agent loop, and productive supports. Frozen model parameters do not imply fixed total inference compute. Separate prompting, reasoning-oriented training, and additional inference work; none guarantees unlimited cognitive improvement.

Give formation and further creation the most space. Establish the gradient, the limiting relation, the new capacity and the possibility it opens for someone or something else. Use autopoiesis where the question is how an established form is produced again. Historical claims about institutional failure need evidence of the particular operation that failed, the attempted repairs, and the arrangement that replaced it.

Preserve the historical text of the [source notes](notes.md); append dated author clarifications when requested, as on November 17, 2026. Use the [expanded ideas](ideas.md) for research commitments, the [outline](outline.md) for the current sequence and the [source ledger](../research/sources.md) for evidence. Prior work on assembly, technology, biology, and social systems must be acknowledged.

## Review before committing

Read changed prose, check titles and transitions against the outline, verify local links and source keys, distinguish proposed designs from demonstrated effects, check identification assumptions and evidence limits, recalculate counts, and run `git diff --check`.

The manuscript remains readable without a runtime. The research code in [scripts](../scripts/README.md) uses a separate Python environment and has estimator/data-validation tests. Run `.venv/bin/python -m unittest discover -s scripts/tests -v` when changing that code. Passing software tests and reproducing a component comparison do not validate the universal hypothesis.
