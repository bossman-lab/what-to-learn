---
title: "Stop Asking 'Is GAI Here' — Ask 'At What Layer'"
published: false
description: "The GAI debate keeps moving the goalpost. I built a 5-layer framework that defines what 'general' actually means, then evaluated 6 frontier models against it. The results explain why we're all talking past each other."
tags: ["ai", "gai", "framework", "evaluation"]
canonical_url: https://dev.to/lanternproton/stop-asking-is-gai-here-ask-at-what-layer-3970
published: true
devto_id: 3936075
---

## Stop Asking 'Is GAI Here' — Ask 'At What Layer'

The GAI debate has a structural problem.

Someone says "passing this benchmark means GAI." A model passes it. Then they say "that benchmark wasn't hard enough." The goalpost moves.

Someone says "passing the Turing test means GAI." Models pass it. Then they say "the Turing test is too easy." The goalpost moves again.

Someone says "inventing new mathematics means GAI." Models do it. Then they say "that's just pattern matching in disguise." Goalpost moves.

**This isn't bad faith. It's a missing layer definition.**

We never agreed on what "general" means. Without that, every achievement gets reclassified as "not really general."

I've been working on a framework that might fix this. It started as a way to map AI capability layers. Then I realized: this isn't just a capability map. **It's a GAI maturity model.**

---

## The Five Layers

| Layer | Name | Definition |
|---|---|---|
| L0 | Embodied | Perceive and operate in the physical world |
| L1 | Application | Complete single-domain tasks using tools |
| L2 | Engineering | Build and maintain systems; understand architecture and constraints |
| L3 | Meta-Domain | Abstract, map, and transfer between unrelated domains |
| L4 | Meta-Cognition | Perceive, understand, and control your own thinking process |

**The rule: layers cannot be skipped.** You can't reach L3 without having L1 and L2 solid. It's a maturity sequence, not a checklist.

This immediately explains the goalpost problem: some people define GAI as reaching L1. Others define it as L4. They're using different layers for the same word and wondering why they can't agree.

---

## What About Models Without Bodies?

The framework originally defined L0 as "perceive and operate in the physical world." But text-only models don't have bodies. So what does L0 mean for an LLM?

Three possibilities:

A. **Training data = body.** A model perceives what its training data covers. Problem: this makes every LLM's L0 stronger than a human's, which defeats the point.

B. **Tool calling = body.** APIs act as sensors and effectors. Problem: tools can be turned off. Bodies can't.

C. **LLMs have no L0.** They start at L1 — cognition without embodiment. This isn't a defect. It's an architectural difference.

Humans build up from L0 (a baby senses the world before understanding it). LLMs start at L1 (they understand the world directly, skipping physical experience). The result: humans can "feel" when something is wrong — that's L0 feeding signals up to L4. LLMs don't have this channel.

**The framework forced me to face something uncomfortable: human intelligence cannot exist without a body.**

---

## Six Models, Five Layers

I evaluated six frontier models against the five layers. The data comes from public benchmarks (SWE-bench, AIME, GPQA, Terminal-Bench, FrontierCode) and published capability reports.

### L0 — Embodied

| Model | Multimodal | Computer Use | Verdict |
|---|---|---|---|
| Gemini 3.1 Pro | Native (text, image, video, audio) | ✅ | **Pass** |
| GPT-5.5 | Vision + audio | ✅ | **Pass** |
| Claude Fable 5 / Mythos 5 | Vision (rebuilds web apps from screenshots) | ✅ | **Pass** |
| Claude Opus 4.8 | Vision | ✅ | **Pass** |
| DeepSeek V4 Pro | Limited multimodal | ❌ | **Fail** |
| GLM-5.2 | Text-only | ❌ | **Fail** |

### L1 — Application (Reasoning, Math, Knowledge)

| Model | AIME 2026 | GPQA-Diamond | HLE | Verdict |
|---|---|---|---|---|
| GLM-5.2 | **99.2** | 91.2 | 40.5 | **Strong** |
| GPT-5.5 | 98.3 | 93.6 | 41.4 | **Strong** |
| Gemini 3.1 Pro | 98.2 | **94.3** | 45 | **Strong** |
| Claude Opus 4.8 | 95.7 | 93.6 | **49.8** | **Strong** |
| DeepSeek V4 Pro | 94.6 | 90.1 | 37.7 | **Good** |

Every frontier model is solid at L1. Gaps are within 5%. This is not where differentiation lives anymore.

### L2 — Engineering (Code, Agentic Tasks)

| Model | SWE-bench Pro | Terminal Bench 2.1 | Verdict |
|---|---|---|---|
| **Claude Fable 5 / Mythos 5** | **80.3** | — | **Dominant** |
| Claude Opus 4.8 | 69.2 | **85** | **Leading** |
| GLM-5.2 | 62.1 | 81 | **Strong** |
| GPT-5.5 | 58.6 | 84 | **Strong** |
| DeepSeek V4 Pro | 55.4 | 64 | **Good** |
| Gemini 3.1 Pro | 54.2 | 74 | **Good** |

L2 shows real separation. Fable 5's 80.3% on SWE-bench Pro is 11 points ahead of Opus 4.8. That's not an optimization gap — it's a generation gap.

### L3 — Meta-Domain (Cross-Domain Transfer)

There is no benchmark for L3. The evidence is indirect:

| Model | Evidence | Verdict |
|---|---|---|
| **Claude Fable 5 / Mythos 5** | Protein design, genomics, and cybersecurity — three unrelated domains — with autonomous work; scientific hypotheses validated independently; rebuilds web apps from screenshots (vision to code) | **Strongest signal** |
| Claude Opus 4.8 | FrontierSWE 74.4, DeepSWE 58 | **Preliminary, code-only** |
| GPT-5.5 | FrontierSWE 72.6, NL2Repo 50.7 | **Preliminary, broad** |
| GLM-5.2 | HLE+Tools 54.7, FrontierSWE 74.4 | **Signals, unverified** |
| Gemini 3.1 Pro | MCP-Atlas 69.2 | **Potential, limited data** |
| DeepSeek V4 Pro | All scores low | **Uncertain** |

Mythos 5's genomics case is the strongest L3 signal I've seen: it ran autonomously for a week, compiled single-cell data from 138 species, designed and trained its own ML model, and outperformed a *Science*-published model despite being 100x smaller.

**The biggest gap isn't model capability — it's that nobody built a benchmark for L3.**

### L4 — Meta-Cognition

| Model | Evidence | Verdict |
|---|---|---|
| **All** | ❌ No model can accurately describe its own reasoning process in real time | **Not reached** |
| | They generate plausible post-hoc explanations, not real-time meta-cognition | |
| | OpenAI's Beneficial RL paper shows "epistemic humility" can be trained, but that's not meta-cognition | |

L4 is completely empty. Not because every model is equally behind — because **the entire industry isn't targeting this capability.**

---

## Summary Table

| Model | L0 | L1 | L2 | L3 | L4 |
|---|---|---|---|---|---|
| **Fable 5 / Mythos 5** | ✅ | ✅✅ | ✅✅✅ | ❓(signal) | ❌ |
| Claude Opus 4.8 | ✅ | ✅✅ | ✅✅ | ❓ | ❌ |
| GPT-5.5 | ✅ | ✅✅ | ✅✅ | ❓ | ❌ |
| Gemini 3.1 Pro | ✅ | ✅✅ | ✅ | ❓ | ❌ |
| GLM-5.2 | ❌ | ✅✅ | ✅✅ | ❓ | ❌ |
| DeepSeek V4 Pro | ⚠️ | ✅ | ✅ | ❓ | ❌ |

---

## What This Means

**If GAI = L1 or L2, we're already there.** Every frontier model can do single-domain tasks and build systems. That's not controversial.

**If GAI = L3, we don't know.** The strongest model (Mythos 5) shows real cross-domain signals, but there's no benchmark to verify it systematically. We need a test for L3 before we can answer.

**If GAI = L4, we're not close.** And more importantly: **nobody in the industry is targeting this.** Not as a research direction, not as a training objective, not as a benchmark.

The GAI debate isn't one debate. It's people arguing at different layers using the same word.

This framework doesn't replace existing benchmarks. It puts them in a coordinate system. Next time someone says "GAI is here" or "GAI is nowhere," the right response is: **"At what layer?"**

---

*Originally published at lanternproton.dev. This framework draws on the Four-Layer Verification Framework (L1 rules → L2 feedback → L3 self-consistency → L4 calibration) and the multi-objective white paper on necessary capabilities for general intelligence. Follow for more at dev.to/lanternproton.*
