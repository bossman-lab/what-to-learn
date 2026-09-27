---
title: "AI Brief: Text Agents Beat VLMs, New Model, Agent APIs"
published: true
description: "Weekly AI digest: text-first agents vs VLM, Ox model debut, Tonghuashun MCP API, ChatGPT award-flight plugin."
tags: [ai, llm, agents, devtools]
canonical_url: https://dev.to/lanternproton/ai-brief-text-agents-beat-vlms-new-model-agent-apis-4h2i
devto_id: 4454250
cover_image:
---

A quick digest of AI-relevant signals from Chinese tech channels — one opinion worth arguing with, one new model worth testing, and two tool updates for agent workflows.

▸ **Text-first agents beat VLM agents — by a quadratic margin** (@openclaw1024): A widely-shared take argues VLM is a dead end: 100k tokens of text carries far more information density than images, let alone video. The argument runs like this — if a 1T–10T-parameter VLM agent can solve a problem of difficulty X, an equivalent text-only LLM agent given full context, memory, wiki, and tool access (text/bash/cli/api/mcp) solves 1000X. And the gap keeps widening: by the time VLMs reach 1000X, text agents are already at (1000²)·X. Provocative, but a useful counterweight to multimodal hype.

▸ **"Ox 牛来" is being called August's surprise model** (@aigc1024): The channel rates it the most impressive model release this month and claims DeepSeek V4-flash-vision-exp can't compete. It's free for 7 days and already live on Cola, OpenRouter, Hermes, and Opencode — worth a spin if you're comparing vision-capable models.

▸ **Tonghuashun ships an official A-share data API with MCP support** (@https1024): The new Financial-API covers market snapshots, daily K-lines, financials, sector data, limit-up, and dragon-tiger lists. One key works across REST, Python, CLI, and MCP, with local DuckDB for storage — aimed squarely at Cursor/Claude-style agents for quant scripts, financial analysis, and automated pipelines, and a way to retire your self-maintained scrapers. An English version of the announcement was cross-posted, signaling an overseas push.

▸ **ChatGPT + Flightpoints plugin for award-mile searches** (@knowledge1024): A quick tip — the Flightpoints plugin lets ChatGPT search mileage award tickets directly in chat, saving a trip to airline portals.

**Bottom line:** multimodal agents are being talked down in favor of text-plus-tools, model churn keeps accelerating, and Chinese data vendors are now shipping MCP-native APIs for the agent ecosystem.
