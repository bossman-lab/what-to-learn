---
title: "Agents Learn to Work Overnight: Prime Agent, Buzz, Lightpanda"
published: true
description: "Five open-source releases from the Chinese dev channels: persistent overnight agents, Block's multi-agent workspace Buzz, an 11x faster headless browser, API provenance testing, and self-registering agents."
tags: [ai, opensource, agents, devtools]
canonical_url: https://dev.to/lanternproton/agents-learn-to-work-overnight-prime-agent-buzz-lightpanda-208n
devto_id: 4668558
---

Five open-source releases surfaced in the Chinese dev channels today, and they point in one direction: agents are getting persistence, shared workspaces, cheaper eyes, and provenance checks.

▸ **"Overnight work" becomes real with Prime Agent** *(source: @openclaw1024)*. PrimeIntellect's RLM agent was today's top GitHub star gainer (2,300+). It treats context as a variable and subagents as function calls inside a persistent IPython environment, and runs as a background daemon — kill your terminal, reconnect later, the task is still alive. Subagents talk to each other directly instead of routing every message through the user. Its "continual harness" keeps prompts, memory, and skill descriptions as persistent state, then makes small evidence-driven refinements from execution traces, with rollback. Skills are importable Python packages.

▸ **Block open-sourced Buzz, a human + agent workspace** *(source: @openclaw1024)*. At 26,000+ stars, Buzz puts people and AI agents into the same workspace: messages, commits, reviews, and merges all land in one signed log, so nobody has to ask "what did the agent do?" Agents get their own keys, roles, and audit trail; they can open repos, submit patches, review code, and run automation. macOS, Linux, Windows, plus an agent-specific CLI.

▸ **Lightpanda: scraping agents don't need a full browser** *(source: @https1024)*. Most agents burn resources rendering pixels nobody ever sees. Lightpanda is a headless browser rewritten from scratch in Zig — not a Chromium fork — reported at 11x faster and 9x lighter on memory than headless Chrome. One-line Docker install, compatible with CDP, Playwright, Puppeteer, and Chromedp.

▸ **ModelTrace checks what your API relay is actually serving** *(source: @aigc1024)*. Challenge-response probing plus attribution scoring to answer a question every dev buying relay/proxy API access has: is this really the model on the label? It targets the worst case — paying flagship prices while silently getting something cheaper.

▸ **Google's Workspace CLI closes the agent self-registration loop** *(source: @yunying23)*. A developer rigged Claude Code to register and log in to platforms autonomously; the last broken link was email verification codes. Polling Gmail through the new `gws` CLI fixed it: the agent registers, pulls the code, verifies, and returns with an API key. Caveat: Google OAuth still rejects automated browsers, so not every platform is reachable.

The skill layer kept expanding too — AntV's Infographic engine renders SVG infographics from a one-line description with ~200 built-in templates and Claude Code / Codex skill integration *(source: @aigc1024)*.

The pattern: agents are being handed the missing infrastructure — persistence, shared logs, cheap perception, and proof of identity — rather than just better prompts.
