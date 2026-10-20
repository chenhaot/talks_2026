# Talk plan (15 minutes, 24 slides)

| Part | Slides | Time |
|---|---|---|
| I. Interactive Age of Information | 1–4 | 3 min |
| II. Ballot measures: interaction by chat | 5–17 | 6 min |
| III. Papers are not the final destination: interaction by creation | 18–23 | 4.5 min |
| Closing | 24 | 0.5 min |

Through-line: since writing, a text has been fixed. You can read it, but it does not answer back and it does not change. AI enables two kinds of interaction with a text: **interaction by chat** (the reader talks with the document, e.g., a ballot measure) and **interaction by creation** (the document itself is redone and extended, e.g., a paper).

Slides: `talk.html`, built on the `../mit/talk.html` template. Images are in `resources/`. The longer version is in `talk.long.md`; the original AI Scientists talk is in `talk.backup.md`.

Style: slide titles are 60px and in title case. No color emphasis on text; emphasis is bold only.

# Part I: Interactive Age of Information

## Slide 1 — Title

**Information in the Interactive Age**

Chenhao Tan
Chicago Human+AI Lab & SAI
[chenhaot.com](https://chenhaot.com)
chenhao@uchicago.edu, @ChenhaoTan

Logos: `resources/chai.jpg`, `resources/sai.png`

## Slide 2 — "Fixity"

Left:

The printing press (~1450) made identical copies of a text at scale.

On click: Science adopted the same form: *Philosophical Transactions* (1665) made the paper the fixed record of a finding.

Right:

- `resources/gutenberg_bible.jpg`, caption "Gutenberg Bible, ~1455"
- On click (with the second paragraph): `resources/philosophical_transactions_1665.jpg`, caption "*Philosophical Transactions*, Vol. I, 1665"

Footer: E. Eisenstein, *The Printing Press as an Agent of Change* (1979). Images: Wikimedia Commons.

## Slide 3 — Phaedrus quote (no title)

> "You'd think they were speaking as if they had some understanding, but if you question anything that has been said because you want to learn more, it continues to signify **just that very same thing forever**."
>
> Plato, *Phaedrus*

Speaker notes: Socrates said this about writing around 370 BCE. Print made it true at scale, and web search made fixed documents easy to find but left them fixed. Chat is the first time text can answer back.

## Slide 4 — AI Enables a New Age of Interaction

Two columns; the second appears on click. Images have a drop shadow and no background box.

**Interaction by Chat**
Image: `resources/ballot_text.png`
Caption: Colorado ballot measure on drug-related penalties
Link: [civicchats.org](https://civicchats.org)

**Interaction by Creation**
Image: `resources/minimum_wage_text.png` (abstract)
Caption: Cengiz, Dube, Lindner, and Zipperer (2019), *The Effect of Minimum Wages on Low-Wage Jobs*
Link: [livingscience.ai](https://livingscience.ai)

# Part II: Ballot measures (interaction by chat)

## Slide 5 — Highlight: Interaction by Chat

Same as Slide 4, with Interaction by Creation faded (no transition), to mark the start of Part II.

## Slide 6 — Ballot Measures Are Hard to Read

Full width: `resources/ballot_colorado_fentanyl.png`

Below the image: Ballot measures are proposals put to a public vote. They are written in complex legal language → voter misunderstanding and disengagement (Reilly and Richey 2011; Burnett and Kogan 2015; Ballotpedia 2026).

Footer: Concurrent work: Ash, Galletta, and Opocher, *BallotBot*.

References:
- Ballotpedia News, Oct 16, 2026: https://news.ballotpedia.org/2026/10/16/2026-ballot-titles-required-17-years-of-education-to-read-down-from-a-record-21-in-2025/ (2026 ballot titles take about 17 years of education to read; 164 statewide measures in 40 states)
- Shauna Reilly and Sean Richey, "Ballot Question Readability and Roll-Off: The Impact of Language Complexity," *Political Research Quarterly* 64(1): 59–67, 2011. https://journals.sagepub.com/doi/10.1177/1065912909349629 (harder-to-read measures are skipped by more voters)
- Craig M. Burnett and Vladimir Kogan, "When Does Ballot Language Influence Voter Choices? Evidence from a Survey Experiment," *Political Communication* 32(1): 109–126, 2015. https://doi.org/10.1080/10584609.2014.894160 (wording can shift votes)

Speaker notes: Democracy depends on an informed electorate; technology has sometimes worked against this (filter bubbles, echo chambers).

## Slide 7 — Research Question (no title)

Centered statement, italic: Can AI-based chat help voters make **more informed decisions**?

## Slide 8 — Three Interactive Conditions

Row of three; the second and third appear one per click:

- `resources/bot_qa.png`: Q&A
- `resources/bot_argumentative.png`: Argumentative
- `resources/bot_reflective.png`: Reflective

On click, below: Technical details are omitted for this talk

## Slide 9 — Experiment

Left: Five conditions

- Official ballot text only (control)
- Ballot text + Ballotpedia
- Chat-QA
- Chat-Argumentative
- Chat-Reflective

Right: `resources/ballot_walkthrough.gif`, a looping walkthrough of the six study screens (consent → instructions → chat → vote → explain → questionnaire; Oklahoma SQ 832, $15 minimum wage). Built from the `resources/ballot_walk_*.png` screenshots, about 1 second per screen (1.5 seconds on the chat screen).

Below: Read and chat → Vote → Explain your reasoning

Results slides 10–12 and 14–17 come from `defense_final.pptx`, slides 34–41 (slide 36 dropped).

## Slide 10 — Two Measures from CO and FL

- Penalty for Fentanyl Sales and Possession Initiative, CO (N=200)
  - Increases penalties for fentanyl-related offenses
  - Requires treatment for certain felony possession cases
- Changes to Budget Stabilization Fund Amendment, FL (N=400)
  - Increases the state’s “rainy-day” fund cap
  - Requires regular deposits, with flexibility to pause them in certain situations

Speaker notes: We chose two measures that differ in topic, complexity, and likely ideological valence.

## Slide 11 — Hypothesis I (no title)

Centered statement: Hypothesis I: Argumentative and Reflective AI will lead to **better decision explanations**

## Slide 12 — Treatments Increase Articulation and Resolution of Tradeoffs, Especially Chatbots

Above the image: A tradeoff is a passage where the participant weighs two competing considerations and resolves or accepts the tension.

On click (pause first), image: `resources/ballot_tradeoffs.png` (resolved vs. unresolved tradeoffs by condition, pooled across studies)

## Slide 13 — How People Talk to Each Bot

Three columns of text, shown together, no images. Each column: the bot's label, then an example user message.

- **Q&A**, "Where would the money be coming from if this was approved"
- **Argumentative**, "I am against, because government is already hiding extra money reserves"
- **Reflective**, "I see the state may want to dip into those funds for emergencies. Florida does tend to suffer from hurricanes, for example..."

## Slide 14 — Hypothesis II (no title)

Centered statement: Hypothesis II: AI leads to **different voting behavior**

## Slide 15 — Treatments Shift Vote Distributions across Both Measures

Image: `resources/ballot_votes.png` (yes/no/abstain by condition, CO and FL)

## Slide 16 — Treatments Cut Abstain by 28% in FL, 12% in CO

Image: `resources/ballot_votes_abstain.png` (same chart, abstain highlighted). No transition from Slide 15.

Speaker notes: Treatments shift vote distributions across both measures and reduce abstention.

## Slide 17 — Ballotpedia Drops CO Yes by 30% but Raises FL Yes by 13%

No transition from Slide 16. Images stacked in place:

- `resources/ballot_votes_yes.png` (same chart, yes highlighted)
- On click: `resources/ballot_votes_yes_bpedia.png` (Text and B-pedia only, arrows: CO down, FL up)
- On click: `resources/ballot_votes_yes_chat.png` (QA, Argue, Reflect only)

Speaker notes: When we look at how the yes vote shifts, we see different patterns across the two measures. (Click) The information intervention does not simply raise or lower support in one direction; effects depend on the content of the measure and the reasons participants encounter. (Click) The strength and direction of the chat effects also vary by measure.

# Part III: Papers are not the final destination (interaction by creation)

## Slide 18 — Highlight: Interaction by Creation

Same as Slide 4, with Interaction by Chat faded (no transition), to mark the start of Part III.

## Slide 19 — Papers Are Not the Final Destination

Top: `resources/minimum_wage_paper.png` (title page, NBER Working Paper 25434, January 2019)

On click, below, italics: This is an empirical study about the past. We need updated results to understand the current state of the world and to inform policymaking.

Footer: Cengiz, Dube, Lindner, and Zipperer, *The Effect of Minimum Wages on Low-Wage Jobs*, QJE 2019.

## Slide 20 — Living Science

Revisit influential research as new data become available.

Flow, left to right:

Replication package → Reproduce key findings → Extend to newer data → Author feedback + community comments

Pause, then all three bullets on one click:
- SAI's replication agent does the first three steps.
- Starts with economics, where data are regularly updated.
- The goal is to keep papers in an ongoing discussion, not to judge whether they were right.

## Slide 21 — Living Science: Minimum Wages through 2024

Left: `resources/living_minimum_wages_fig2.png` (1979–2016 vs. 2016–2024)

Right:

- Extended to **236 increases**, 1979–2024
- **+4.6%** affected wages
- **−1.1%** affected employment, statistically indistinguishable from zero

## Slide 22 — A Quick Overview of the Current Results

- Minimum wages (Cengiz et al. 2019), to 2024: no clear job loss through the $15 era.
- Unemployment (Shimer 2012), to 2026: unemployment still rises mainly because people take longer to find new jobs, not because more people lose jobs. The exception is 2020, when COVID layoffs drove the spike.
- Regional economies (Blanchard and Katz 1992), to 2025: migration now absorbs less of a local job loss.
- China Syndrome (Autor, Dorn, and Hanson 2013), to 2023: most of the manufacturing job loss had not recovered by 2023.
- Allocation of talent (Hsieh et al. 2019), to 2024: falling barriers now add 4–8% of growth, down from about 40% in 1960–2010.

Speaker notes: Code is public on GitHub; anyone can flag issues and add analyses.

## Slide 23 — An Ongoing Effort

Top: `resources/livingscience_home.png` (livingscience.ai home page)

Below, centered:

The project is a living project on its own. We would love to work together!

Please nominate papers at [livingscience.ai/nominate](https://livingscience.ai/nominate)

# Closing

## Slide 24 — Closing (no title)

Two columns of website screenshots, drop shadow, no background box:

- **Interaction by Chat**: `resources/civicchats_home.png`, link [CivicChats](https://civicchats.org)
- **Interaction by Creation**: `resources/livingscience_home.png`, link [Living Science](https://livingscience.ai)

On click, centered, both lines the same size, not bold:

The Interactive Age of Information is already here.
What can we do to shape it?
