---
title: "AI Brief: Claude's Riemann Leap, Jev, Vercel's deepsec"
published: true
description: "A research Claude raised a Riemann Hypothesis bound from 41.6% to 67.2%, TypeSafe's Jev outputs decisions instead of text, and Vercel open-sourced an agent-based security scanner."
tags: [ai, machinelearning, opensource, devtools]
canonical_url: https://dev.to/lanternproton/ai-brief-claudes-riemann-leap-jev-vercels-deepsec-2nlm
devto_id: 4685743
---

Three signals from the Chinese AI channels today: agents doing original math research, a model that decides instead of generating, and agent-based security scanning.

▸ **A research build of Claude pushed a Riemann Hypothesis bound from 41.6% to 67.2%** *(source: @aigc1024)*. Since a full proof is out of reach, mathematicians track how many of the Riemann zeta function's non-trivial zeros provably lie on its critical line — progress that crawled from 33% (1974) to 41.7% (2020), roughly 50 years of work. Claude jumped the lower bound to 67.2% in a single step, the largest advance in the problem's history. Anthropic's mathematicians and outside experts (Brian Conrey, Dan Goldston) reviewed the result, and Claude also emitted a machine-checkable Lean formalization. The run was roughly 60 subagents executing 2,400 commands and hundreds of Python scripts; the human operator mostly sent encouragement. Anthropic cautions this does not directly lead to proving the conjecture itself.

▸ **TypeSafe's Jev outputs decisions, not text** *(source: @aigc1024, @https1024)*. The model does only three things: boolean judgments ("search or not"), enum choices ("fast vs plan, which model, which bot"), and candidate scoring. It is pitched as a fast, cheap "System One" for routing. Concrete uses: millisecond search-intent classification, model-gateway routing (flash vs SOTA), and multi-agent task dispatch. Browser Use and TypeSafe shipped `jev-ultrafast`: one request per step picks both the action type and the target element, so the agent skips per-step screenshot analysis by a vision model. Jev is live on OpenRouter but is not OpenAI Chat Completions compatible — you assemble `state` and `questions` against its Decisions API. A practitioner's caveats: 255 options per choice, classification accuracy limits, and System-2 tasks that still need an LLM.

▸ **Vercel Labs open-sourced `deepsec`** *(source: @https1024)*. An agent-based security scanner for large codebases, aimed at the hidden bugs traditional scanners miss. It runs on your own infrastructure, scans in parallel across up to thousands of sandboxes, and resumes from where it stopped. Kick it off with `npx deepsec init`.

▸ **ModelScope's "Purple Book" cookbook** *(source: @aigc1024, @https1024)*. An open-source tutorial (8 parts, 34 chapters, 33 readable) for building your own model end to end: model selection and download, data prep, inference deployment (Ollama, cloud notebooks, quantization), fine-tuning with ms-swift, evaluation with EvalScope, RAG and agent apps, and DiffSynth image LoRA.

▸ **Corporate moves: energy, pharma, servers** *(source: @NewlearnerChannel)*. NVIDIA, Google, and Emerald AI launched an AI energy-management alliance for flexible data centers; Novo Nordisk is partnering with Anthropic to apply Claude to drug discovery; Sharp is entering the AI server market with Foxconn.

**Bottom line:** the day's signal splits between frontier labs using agents to produce original mathematical research, and a new class of cheap decision models that route work instead of generating it.
