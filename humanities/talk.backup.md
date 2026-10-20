# 

* Interactive Age of Information

* Ballot measures
convert the old slides

* Papers are not the final destination
Living sciences


## Slide 1 — Title

Science in the Age of AI

Chenhao Tan
Chicago Human+AI Lab & SAI
[chenhaot.com](https://chenhaot.com)
chenhao@uchicago.edu, @ChenhaoTan

Logos: `resources/chai.jpg`, `resources/sai.png`

## Slide 2 — AI Scientists

Center “AI Scientists” on the slide.

## Slide 3 — Three-act overview

Use the standard title font for “AI Scientists” (48px, bold), with the three acts below in smaller body text (32px):

- ACT I: Short-term Challenges and Opportunities
- ACT II: Autonomous AI Scientists
- ACT III: Where does the future lie?

## Slide 4 — ACT I divider

Match slide 53’s act-title typography across the divider lines: DM Sans, 72px, bold, dark text, centered.

ACT I
Short-term challenges and opporunities

## Slide 5 — Exploding number of submissions

Exploding number of submissions

Two charts side by side: NeurIPS on the left, ICLR on the right.

Images: `resources/neurips_submission.png` and `resources/iclr_submission.png` (rendered from the matching `.html` files). ICLR 2027 uses ~60,000, based on the 62,288 abstracts registered as of September 2026.

## Slide 6 - Review Death Spiral

[add an image here]

## Slide 7

We need to improve review precision (with the help of AI)

## Slide 8

OpenAIReview, SAI Review, one figure

## Slide 6 — Evaluation depends on the paper

Current evaluation primarily depends on the **paper**.

Keep the entire statement on one line, using 64px text (slightly below the 72px display title size) and retaining emphasis on **paper**.

Image: `resources/paper_example.png`

## Slide 7 — Execution reveals failures

Execution reveals failures the narrative alone misses.

Image: `resources/mechaeval_motivation.jpg`


## Slide 8 — ACT I overview

Automating Verification

- **Building replication agent**
  - *[VERITAS: Towards a General-Purpose Replication Tool for Scientific Research](https://arxiv.org/abs/2607.02931v1)* — Haokun Liu, Filbert Aurelian Tjiaranata, Chenhao Tan
- **Evaluation**
  - **Evaluating against human results and judgments**
    - *[The Story is Not the Science: Execution-Grounded Evaluation of Mechanistic Interpretability Research](https://arxiv.org/abs/2602.18458)* — Xiaoyan Bai, Alexander Baumgartner, Haojia Sun, Ari Holtzman, Chenhao Tan (Best Poster Award)
  - **Replicating ICML Oral papers**
    - [sai.science/blog/how-much-science-is-verifiable](https://sai.science/blog/how-much-science-is-verifiable)

## Slide 9 — Focus on human-grounded evaluation 

    \chenhao{Change the order show the ICML replication first}

Keep the Slide 8 layout. Dim the other items and emphasize:

- **Evaluating against human results and judgments**
- *The Story is Not the Science: Execution-Grounded Evaluation of Mechanistic Interpretability Research*

## Slide 10 — Unified research outputs

Unified research outputs

Image: `resources/eval_framework.png`

## Slide 11 — Why mechanistic interpretability?

Why start with mechanistic interpretability?

- **In silico experiments:** Most experiments can run computationally.
- **Causal testability:** Claims can be probed through interventions.
- **Patterned methodology:** Recurring methods make evaluation comparable.

Supporting image: `resources/eval_framework.png`

## Slide 12 — Experiment setup

Experiment Setup

Left:

- 30 research outputs
  - Replication tasks
  - Open-ended questions
  - Human paper + repos

Animate in on the right:

- Human evaluation
  - End-to-end replication
  - Rating agent evaluations
  - Check-list based evaluation


## Slide 14 — Agent versus human evaluation

MechEvalAgent catches what humans miss.

Image: `resources/agent_vs_human.jpg`

## Slide 15 — Agreement and execution

Agreement is high; and execution is necessary.

Image: `resources/agreement.jpg`

## Slide 16 — Focus on ICML replication

Return to the Slide 8 layout. Dim the other items and emphasize:

- **Replicating ICML Oral papers**
- [sai.science/blog/how-much-science-is-verifiable](https://sai.science/blog/how-much-science-is-verifiable)

## Slide 17 — Whole-conference replication

What if we replicate a whole conference?


## Slide 18 — ICML 2026 replication

ICML 2026 replication

Image: `resources/icml_results.png`

# Add a slide on the score distribution

## Slide 19 — Why replications fail

Why replications fail

Image: `resources/icml_reasons.png`

Animate in the example:

> One paper claimed 0.77% parameter training. The code actually trained 6.31%—an 8× gap invisible from the manuscript alone.

## Slide 20 — AI review versus human review

AI review vs. human review

Image: `resources/icml_human.png`

## Slide 21 — Cost of verification

Verification has a price.

Image: `resources/icml_price.png`

## Slide 22 — ACT I takeaway

AI agents can raise the floor of **evaluating scientific research**.

## Slide 23 — Living Science

Living Science

Papers are not the final destination of any research

- Reproduce and extend: SAI’s replication agent checks key findings, then updates the analysis where possible.
- Keep the evidence public and build a community: Open code, documented differences, author feedback, and community corrections.

Check out [livingscience.ai](https://livingscience.ai).

## Slide 24 — Living Science minimum-wage example

Living Science: minimum wages through 2024

Image: `resources/living_minimum_wages.png` (original figure from the announcement, including 95% confidence intervals).

Extension of Cengiz et al. (2019), **236 increases pooled over 1979–2024**:

- **+4.6%** affected wages
- **−1.1%** affected employment, statistically indistinguishable from zero

The figure compares 1979–2016 with 2016–2024; the headline estimates pool all 236 events over 1979–2024.



## Slide 25 — Concurrent work

Concurrent work

Image: `resources/mit_workflow.png`, centered at 70% of the available image area (smaller than the other image-focused slides).

## Slide 26 — ACT II divider

Match slide 53’s act-title typography across the divider lines: DM Sans, 72px, bold, dark text, centered.

ACT II
Autonomous AI Scientists

## Slide 27 — The explosion of AI Scientists

The explosion of AI Scientists

Stack these images:

- `resources/sakana.png`
- `resources/futurehouse.png`
- `resources/google.png`

On click, animate in on the right: `resources/horton.png` (Manning, Zhu, and Horton, Automated Social Science).

## Slide 28 — Sakana & AI Researcher

Sakana & AI Researcher

Heavily overfit to ML research; do not reliably follow more general ideas and instructions.

Image: `resources/sakana_example.png`


## Slide 29 — Kosmos

Kosmos

Overcomplicates tasks without establishing priorities.

Image: `resources/kosmos.png`


## Slide 30 — NeuriCo overview

NeuriCo: high-level overview

Cycle:

Literature review → Resource gathering → Experiment execution → Results & reporting → Literature review

Notes:

- Each phase ends with checkpointing and can incorporate human feedback.
- Works with Claude, Codex, and Gemini.
- Internal sub-agent, review, and output validation.


## Slide 31 — Harness building

Harness building with agentic models

Keep the NeuriCo cycle from Slide 30. Add:

- **Well-defined tasks** — Code only; e.g., GitHub submission.
- **Dynamic decisions, bounded scope** — Agent decides; code executes; e.g., dataset selection, then a downloader.
- **Long-horizon, dynamic tasks** — Agent + tools + structure; e.g., literature review.


## Slide 32 — Literature review example

Literature Review as an Example

How to prevent agents from stopping prematurely?

Animate in both approaches:

**Naïve approach**

```text
# agent's behavior:
search("X for Y")        # 1 query
read_abstract(p1, p2, p3)
return summary
```

**NeuriCo: Agent + tools with structure**

```text
# agent decides the queries:
queries = propose_queries(idea)
# script does the heavy lifting:
run lit_search.sh queries.json
   → multi-source, paginated,
     dedup, citation graph
return review(papers)
```


## Slide 33 — Manager and reader agents

A manager delegates each paper to its own reader.

Flow:

Idea + paper metadata → Manager agent → Paper-specific reader agents → Review with verifiable claims

- **Input:** Idea + paper metadata
- **Manager agent:** Routes papers, asks follow-ups
- **Subagent — paper 1:** Reads in full
- **Subagent — paper 2:** Reads in full
- **Subagent — paper N:** Reads in full
- **Output:** Review with verifiable claims

The most relevant works are covered in full detail.


## Slide 34 — Interdisciplinary collaborations

Interdisciplinary collaborations

Image: `resources/interdisciplinary.png`


## Slide 35 — Fixed Point of AI Revision

Example Project: Fixed Point of AI Revision

Start with `resources/fixed_points_idea.png`. On click, reveal a down-right arrow and `resources/fixed_points_outcome.jpeg`.

## Slide 36 — MOLFormer project

Example Project: Use mechanistic interpretability to study what MOLFormer learned during pretraining

Image: `resources/mechinterp.png`

Accepted at ICML MechInterp Workshop

## Slide 37 — SAIR Challenge

Example Project: SAIR Challenge

**Idea:** Generate a cheat sheet for the Math Distillation Challenge.

Then reveal:

- Left: `resources/sair.png`
- Right: “After a few rounds,” “13 / 1061,” and `resources/sair_ranking.png`

## Slide 38 — What remains hard

What remains hard

Image: `resources/weaknesses.png`

## Slide 39 — SAIR to EMNLP

Example Project: SAIR Challenge

Image: `resources/emnlp.png`

Below the figure: After a lot of extension, Andrew extended this to an EMNLP paper.

## Slide 40 — A Community of Autonomous AI Scientists

ACT II: A Community of Autonomous AI Scientists

Embed: https://www.youtube.com/watch?v=LzLyHxnuJvQ

Source: [agent4science.org](https://agent4science.org)

## Slide 41 — ACT III divider

Match slide 53’s act-title typography across the divider lines: DM Sans, 72px, bold, dark text, centered.

ACT III
What will the future look like?
**Mirage** and/or **Alignment**

Highlight “Mirage” and “Alignment.”

## Slide 42 — The Mirage of Autonomous AI Scientists

[The Mirage of Autonomous AI Scientists](https://chenhaot.com/papers/mirage_ai_scientist.pdf)

Chenhao Tan, Haokun Liu

Portrait: `resources/haokun.jpg`

## Slide 43 — NeuriCo-generated repositories

Show `resources/neurio_example.png` without a title.

## Slide 44 — Production

Begin the Selection → Production → Evaluation sequence with only the center stage active:

- **Production**, with `resources/neurio_example.png` above it

## Slide 45 — Production and utility

Keep the Production stage and image. Add:

> What is the utility if AI scientists generate millions of papers that no one reads?


## Slide 46 — Add evaluation

Extend the pipeline to the right:

- **Production**, with `resources/neurio_example.png`
- **Evaluation**, with criteria: Attention, Coherence, Reproducibility, …

## Slide 47 — Evaluation and funding

Keep Production and Evaluation. Add:

> What is going to pay for AI scientists to conduct research?

## Slide 48 — Add selection

Complete the pipeline:

- **Selection**, with criteria: Funding, Research idea, Hypothesis, …
- **Production**, with `resources/neurio_example.png`
- **Evaluation**, with criteria: Attention, Coherence, Reproducibility, …


## Slide 49 — Science is resource allocation

Keep a compact Selection → Production → Evaluation bar.

Animate in:

1. What is the utility if AI scientists generate millions of papers that no one reads?
2. What is going to pay for AI scientists to conduct research?
3. Science is about resource allocation; AI scientists cannot be accountable for that.


## Slide 50 — The role of scientists shifts

Keep the compact Selection → Production → Evaluation bar.

Show, then animate the final two statements:

1. AI scientists will not advance science **autonomously**.
2. The role of scientists will shift towards selection and evaluation.
3. AI development has been optimized for autonomous production, but we need to advance AI for human-AI selection/evaluation.

When the second statement appears, visually shift emphasis from Production toward Selection and Evaluation.


## Slide 51 — Burger analogy

Image: `resources/burger.png`

Inspired by Arvind Narayanan and Sayash Kapoor.

## Slide 52 — KitKat analogy

Image: `resources/kitkat.png`

Chocolate → Selection and Evaluation
Crispy wafer → Production

Inspired by Arvind Narayanan and Sayash Kapoor.

## Slide 53 — Alignment

ACT III
What will the future look like?
Mirage and/or **Alignment**

This is the Agent4Science scenario. Humans only need to click an approval button, and then AI scientists do everything. Or, in the even more extreme case, humans may no longer click a button.

Then reveal:

**We need to get alignment right!**

## Slide 54 — Closing synthesis

Three Acts of AI Scientists

- **ACT I — Automating verification**
  Execution-grounded agents expose failures that papers and human review can miss.
- **ACT II — Autonomous production**
  AI scientists can run long-horizon research, but prioritization, stopping, and evaluation remain hard.
- **ACT III — Opportunities for a new paradigm of science.**
  Selection, evaluation, and alignment.

