# Talk plan

1. Interactive Age of Information
2. Ballot measures (converted from `polsci/polscience.pptx`, slides 39–70)
3. Papers are not the final destination: Living Science

Through-line: ballot text and research papers are both static documents written once and read many times. AI makes information interactive, which changes how citizens engage with a ballot and how a paper keeps living after publication.

All new images are in `resources/`. The previous AI Scientists talk is kept below under **Archive** for reuse.

# Part I: Interactive Age of Information

## Slide 1 — Title

Working title (the polsci deck notes said "I need a new title"): **Information in the Interactive Age**

Chenhao Tan
Chicago Human+AI Lab & SAI
[chenhaot.com](https://chenhaot.com)
chenhao@uchicago.edu, @ChenhaoTan

Logos: `resources/chai.jpg`, `resources/sai.png`

## Slide 2 — From static to interactive

[DRAFT, edit framing]

A timeline across the slide:

Print → Library catalog → Web search → Chat

- Print through search: you **retrieve** a fixed document and read it yourself.
- Chat: the information **responds** to you. You can ask, push back, and reflect.

\chenhao{dig up some history on information, book}

\chenhao{Interaction by chat, interaction by creation, that should be the difference between chat and paper}

## Slide 3 — Same document, different reader

[DRAFT]

Interactive information means the same content can be met differently by each reader: a voter asking where the money comes from, a skeptic arguing against, a scholar asking about a newer data set.

## Slide 4 — Two static documents

[DRAFT]

Two side-by-side cards, which preview Parts II and III:

- **The ballot**: written in legal language, read once at the voting booth. Image: `resources/ballot_colorado_fentanyl.png`
- **The paper**: written once, frozen at publication. Image: `resources/living_minimum_wages_fig1.png`

What happens when both become interactive?

# Part II: Ballot measures (CivicChats)

Source: `/Users/chenhao/work/talks/2026/polsci/polscience.pptx`, slides 39–70. Original slide numbers in parentheses.

## Slide 5 — AI & Democracy (40)

AI & Democracy

- Democracy depends on an informed electorate.
- Technology may have been counterproductive in some cases (e.g., filter bubble, echo chamber).

## Slide 6 — Sycophancy (41)

Keep Slide 5 bullets; animate in a third:

- LLMs by default might be sycophantic.

Image on the right: `resources/science_toxic_praise.png` (Science cover, "Toxic Praise").

## Slide 7 — Question (42)

How can we build AI to strengthen democracy?

## Slide 8 — Ballot measures (43)

Ballot measures are proposals put to a public vote.

Image: `resources/ballot_colorado_fentanyl.png` (Colorado, Penalties for Fentanyl Sale and Possession Initiative, November 3, 2026).

## Slide 9 — Complex legal language (44)

Ballot measures often contain complex legal language

→ voter misunderstanding and disengagement [Riley and Richey 2009]

Speaker notes (from original):
- https://www.nytimes.com/roomfordebate/2016/11/03/why-are-ballot-measures-so-confusing/ballot-measures-need-to-be-written-in-plain-language
- https://civicdesign.org/ballot-questions-are-hard-to-understand-here-are-6-ways-to-fix-them/
- https://journals.sagepub.com/doi/abs/10.1177/1065912909349629
- https://ballotpedia.org/Ballot_measure_readability_scores,_2025#cite_note-RR2011-5

## Slide 10 — Research question (45)

Can AI-based chat interfaces help voters make more informed decisions on ballot measures?

Speaker notes: https://www.science.org/doi/10.1126/science.adq1814, https://osf.io/preprints/psyarxiv/h7n8u_v2

## Slide 11 — Three chatbots (46–47)

Keep the question as the title. Build left to right, one per click, each labeled below:

- `resources/bot_qa.png`: **Q&A**
- `resources/bot_argumentative.png`: **Argumentative** ("That is not right")
- `resources/bot_reflective.png`: **Reflective** ("Have you considered this")

## Slide 12 — Concurrent work (48)

Keep Slide 11. Overlay on the left: `resources/ballotbot_paper.png` (Ash, Galletta, Opocher, *BallotBot: Can AI Chatbots Lower Voter-Information Barriers?*).

## Slide 13 — Evaluation + prompt refinement (49)

Evaluation + Prompt Refinement

Image: `resources/ballot_eval_prompt_refinement.png`

## Slide 14 — Section divider (50)

Ongoing Large-scale Experiments

## Slide 15 — Experiment conditions (51)

Experiment Conditions

- **Official ballot text**: official ballot text only (control)
- **Ballotpedia**: official text + expandable Ballotpedia content
- **Chatbot conditions**
  - Chat-QA
  - Chat-Argumentative
  - Chat-Reflective

## Slide 16 — Experiment walkthrough (52–55)

Experiment Walkthrough

Step through one image per click (example: Oklahoma SQ 832, $15 Minimum Wage Initiative):

1. `resources/ballot_walk_consent.png`: consent
2. `resources/ballot_walk_instructions.png`: study structure
3. `resources/ballot_walk_chat.png`: read and discuss the measure with CivicChat
4. `resources/ballot_walk_vote.png`: voting decision and confidence
5. `resources/ballot_walk_explain.png`: explain reasoning, address opposing views
6. `resources/ballot_walk_questionnaire.png`: background questionnaire

Note: the original "Preliminary Results" slide (56) reused the Colorado ballot image, so it is dropped here.

## Slide 17 — Hypotheses (57)

Hypotheses

1. AI leads to more and deeper engagement
2. AI leads to more informed voting
3. AI leads to different voting decisions

Slides 18–25 reuse this list as a progress bar: highlight the current hypothesis and dim the others (replaces original divider slides 58, 63, 66).

## Slide 18 — Engagement time (59)

H1. Users engage longer in AI conditions

Image: `resources/ballot_active_time.png`

## Slide 19 — Message length (60)

H1. Users write more in Argumentative

Image: `resources/ballot_message_length.png`

## Slide 20 — Example messages (61)

H1. User chat engagement differs across conditions

Three columns:

**Q&A**
- "Where would the money be coming from if this was approved"
- "If the current budget is 10% how much is that"

**Argumentative**
- "They mention budget shortfall, but don't mention all the money that all the government entities (city, county, State, etc.) have as 'rainy day funds' already"
- "I am against, because government is already hiding extra money reserves"

**Reflective**
- "Ok I am confused. If more money is kept in the budget stabilization funds, does this mean there's more money available for emergencies but less for day to day?"
- "I see the state may want to dip into those funds for emergencies. Florida does tend to suffer from hurricanes, for example. Is part of the reasoning here that Florida is wanting to be more independent of federal funding and support that might come e.g. from FEMA?"

## Slide 21 — Question types (62)

H1. A further breakdown of user messages

Image: `resources/ballot_question_types.png`, with legend `resources/ballot_question_types_legend.png` placed at the top right.

## Slide 22 — Arguments (64)

H2. Users write more arguments, especially in Reflective

Image: `resources/ballot_arguments.png`

## Slide 23 — Counter-arguments (65)

H2. Users acknowledge and engage with counter-arguments more in chat conditions

Image: `resources/ballot_counterarguments.png`

## Slide 24 — Vote choice (67)

H3. Participants in the Reflective condition are much more likely to vote No

Image: `resources/ballot_vote_choice.png`

## Slide 25 — In progress and looking ahead (68–70)

In Progress
- Additional states/ballot measures
- Long-term follow-up survey (1 month)

Looking Ahead
- We are actively looking for partners.
- We might expand this to candidate voting.
- Any feedback is welcome!

Animate in: Tell your friends about CivicChats so that they feel ready to vote in future elections!

## Slide 26 — CivicChats team (39)

CivicChats

Row of team photos: `resources/civicchats_team_1.png` … `resources/civicchats_team_5.png`, `resources/civicchats_team_6.jpg`. [TODO: add names under each photo; the original slide had none.]

# Part III: Papers are not the final destination

## Slide 27 — Transition

[DRAFT]

A ballot is read once. So is a paper: published, cited, and frozen.

What if papers kept living?

## Slide 28 — Living Science

Living Science

Revisit influential research as new data, models, and methods become available. The goal is to keep influential papers part of an ongoing discussion, not to judge whether they were correct when published.

Check out [livingscience.ai](https://livingscience.ai).

## Slide 29 — How it works

Flow, left to right:

Find public replication package → Reproduce key findings → Extend to newer data → Sanity checks + author feedback → Community comments

- SAI's replication agent does the first three steps.
- Starts with economics, where data sources are regularly updated.
- At least one new paper per week; nominate at livingscience.ai/nominate.

## Slide 30 — Minimum wages: replication

Living Science: minimum wages (Cengiz, Dube, Lindner, Zipperer 2019)

Image: `resources/living_minimum_wages_fig1.png`

Original: 138 state increases, 1979–2016. Jobs lost below the new minimum are matched by jobs gained just above it. Wages **+6.8%**, employment **+2.8%** (not significant).

Replication: Stata translated to R; Table I matches to reported precision.

## Slide 31 — Minimum wages: extension

Living Science: minimum wages through 2024

Image: `resources/living_minimum_wages_fig2.png` (1979–2016 vs. 2016–2024 increases).

**236 increases pooled over 1979–2024**:
- **+4.6%** affected wages
- **−1.1%** affected employment, statistically indistinguishable from zero

Animate in: the 2016–2019 high-bite ($15-era) window shows employment −4.0% (s.e. 2.4).

## Slide 32 — Unemployment

Living Science: what drives unemployment? (Shimer 2012)

Image: `resources/living_ins_and_outs_fig2.png` (series carried to mid-2026, with a marker where the paper's data stopped).

- Paper: job finding explains ~90% of fluctuations since 1987.
- Extended through June 2026, excluding 2020: **89%**.
- 2010–2026 including 2020: job loss explains **38%**. The pandemic was mainly a layoff shock.

## Slide 33 — Regional economies

Living Science: how regions absorb job losses (Blanchard and Katz 1992)

Image: `resources/living_regional_evolutions_fig2.png` (four adjustment quantities re-estimated by era, 1978–2025).

- Employment shocks are still permanent (year-20 response 1.52 for 2006–2025).
- Year-one out-migration absorbs **24–28%** of a job loss after 2008, down from **38%** in 1978–1990.

## Slide 34 — Supports, qualifies, or changes

[DRAFT] One row per paper:

| Paper | Newer evidence |
|---|---|
| Minimum wages | Supports (with a caveat for $15-era increases) |
| Unemployment | Supports, except the pandemic |
| Regional economies | Qualifies: less migration |

## Slide 35 — A shared public record

Why a shared public record

- **Building on work**: replication repositories are public on GitHub.
- **Common knowledge**: shows when newer evidence supports, qualifies, or changes older results.
- **Community effort**: people catch errors, question interpretations, and add analyses as data arrive.

Each report also has "Ask about this paper": the paper itself becomes interactive (ties back to Part I).

## Slide 36 — Closing

[DRAFT]

Information in the Interactive Age

- **Ballots**: AI chat changes how voters engage, argue, and decide. Design choices (Q&A vs. Argumentative vs. Reflective) matter.
- **Papers**: findings can be reproduced, extended, and discussed as data arrive.
- Open question for the humanities: [TODO]

# Archive: previous AI Scientists talk

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

