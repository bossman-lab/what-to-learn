# The Missing Piece in Jason Wei's Framework: When to Go On-Policy

> Jason Wei — the "Chain-of-Thought father" — just left OpenAI for Meta. The rumored package starts at $100M.
>
> Before the news broke, he published two blog posts. One on life lessons from reinforcement learning. One on the asymmetry of verification.
>
> Both are insightful. But neither answers the question that ties them together: **when do you switch from imitation to on-policy exploration?**
>
> Here's a framework.

---

## The two ideas

**Idea #1: Life is on-policy RL**

Jason Wei discovered RL this year and became obsessed. One concept stuck: stay on-policy whenever possible.

Off-policy: learning from someone else's trajectory. On-policy: generating your own data by interacting with the environment, then learning from it.

Imitation learning gets you started. School is imitation. Studying successful people and copying their moves — sometimes it works. But over time you realize: imitation can never surpass the original, because everyone has unique strengths and circumstances you cannot replicate.

He gives two personal habits:

- Reading raw data (not summaries). Spending days going through every data point, writing personalized feedback to each annotator. Data quality soared, and he developed insights nobody else had.

- Running ablation studies on his own past decisions. Spending a month isolating every "hacky" choice he'd made in previous research — figuring out what actually worked.

Common structure: **bypass the middleman. Touch the signal directly.**

**Idea #2: The asymmetry of verification**

Some tasks are much harder to solve than to verify.

Sudoku: solving takes forever, verifying takes seconds.
Building a website: teams spend years, a user verifies in minutes.
BrowseComp: browse hundreds of sites to find an answer, verifying takes moments.

The corollary — **Verifier's Law**: anything measurable can be optimized. Under RL, the ability to verify equals the ability to build a training environment. Every solvable, easily-verifiable task will eventually fall to AI.

This doesn't mean "easy tasks get solved first." It means tasks with low verification cost get solved first — regardless of their human-perceived difficulty. The boundary of AI capability follows verification cost, not task importance.

> Intelligence will advance unevenly. In verifiable domains, AI will dominate — not because those domains are easier, but because they are more *tameable*.

---

## The hidden tension

Put these two ideas together. A contradiction emerges.

Verifier's Law is a **convergent** logic. Good verification → good optimization → solved. Deterministic, downward-compatible, path-clear.

On-policy life is a **divergent** logic. Walk your own path → embrace uncertainty → chase unknown rewards. Open, exploratory, anti-imitation.

One says "everything verifiable can be conquered." The other says "don't just walk roads others have verified."

Are they contradictory? No. They're two sides of the same cycle.

Verifier's Law describes **optimization in known space** — you already have a verifiable standard, now optimize to the limit.

On-policy describes **exploration in unknown space** — no standard exists yet. You need to generate your own trajectory and define what counts as "good."

The only real question: **when do you switch?**

---

## The answer he didn't give

Jason Wei says: "switch once you've found your footing."

This statement has one honest part — imitation genuinely works at the start. And one dishonest part — **"found your footing" has no operational definition.**

He didn't provide one. Not because he doesn't know, but because the ability to judge when imitation is no longer serving you is itself an on-policy skill. You cannot learn it from someone else's trajectory.

Here's the missing framework.

---

## Two switch signals

**Signal #1: You ask a question your imitation source cannot answer.**

Imitation learning follows an S-curve. Early: steep gains. Mid: diminishing returns. Late: near-zero — you realize your source is also struggling with this problem, or no established answer exists.

The switch signal is NOT "I don't know how." That's the starting line.

The switch signal is: **"I know how others do it — but I suspect their approach is wrong, incomplete, or blind to something I see. And I want to test my hypothesis."**

Jason Wei read raw data not because he hadn't read the papers. He read it because he suspected the compression ratio of academic writing was losing signal. He ran ablation studies not because he didn't know the conclusions — he wanted to verify those conclusions held in his environment.

Common structure: you formed a hypothesis, and the only way to verify it is to **execute yourself.**

**Signal #2: The 60% rule.**

There is always a reason to "study more before acting." Theory can always be deeper. Knowledge can always be broader. "I'll act once I truly understand" is an infinite loop.

The rule: when you are 60% confident your hypothesis is not stupid — **execute.**

Why 60%? Because the remaining 40% can only come from on-policy feedback. You will never reach 100% certainty inside the imitation phase. Jason Wei spent a month on ablation studies with uncertain expected value. He admitted afterward: "it took considerable time, but I gained things nobody could teach me."

> Starting doesn't need perfection. Starting needs real feedback.

---

## Reference card

| Phase | Your question | Action |
|-------|-------------|--------|
| Still imitating | "How do they do it?" | Keep learning, no rush |
| Ready to switch | "Is their approach *right*?" | Test your hypothesis |
| Must execute | 60% confident it's not stupid | Go. The last 40% lives in feedback. |

---

## The deeper structure

These two frameworks, taken together, reveal a meta-cycle:

> Explore (on-policy) → Verify (Verifier's Law locks in gains) → Free cognitive bandwidth → Explore again

This is not a linear A-then-B progression. It is a dynamical loop.

Every cycle of "ship → validate → fix P0s → write paratext → format → finalize" follows the same pattern: on-policy execution, followed by verification-based convergence, followed by freed bandwidth for the next exploration.

Jason Wei's most valuable — and unstated — insight might be this:

**The judgment of when to explore and when to converge is itself the moat.**

And that judgment can only be acquired on-policy.

So your first step: write down one hypothesis nobody else has written, but you believe is worth testing.

Don't wait for 100%.

60% is enough.

---

*Originally published on [dev.to](https://dev.to/lanternproton).*

*Follow for more AI-era cognitive frameworks — frameworks at the intersection of systems thinking, epistemology, and machine learning.*
