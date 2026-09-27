---
title: "Claude Code Job Search: 69 Applications, 20 Interviews, 1 Offer"
published: true
description: "A laid-off geophysicist used Claude Code to automate his job hunt (69 apps -> offer, 29k+ GitHub stars). Full breakdown of the ai-job-search pipeline + a markdown editor shipped with AI coding."
tags: [ai, claude, career, devtools]
canonical_url: https://dev.to/lanternproton/claude-code-job-search-69-applications-20-interviews-1-offer-487f
devto_id: 4537511
---

A laid-off geophysicist turned his job hunt into an agentic workflow and open-sourced it. The project, **ai-job-search**, has blown past 29,000 stars on GitHub — and it's a blueprint for how AI turns a messy, subjective process into an executable pipeline.

▸ **From 69 applications to an offer** *(source: @aigc1024)*. Mads Lorentzen, a geophysicist who was laid off, used Claude Code to build a job-search framework that automated his entire funnel: 69 applications → 20 first-round interviews → a job offer, and he landed an AI engineering role. The full funnel data is shared publicly on LinkedIn.

▸ **The whole job-search supply chain, automated** *(source: @aigc1024)*. Where most people use ChatGPT as a copy-paste resume polisher, ai-job-search rebuilds the pipeline end to end: job discovery, match scoring (skills, experience, culture, location, career growth), tailored resume and cover letter drafting, interview prep, and application tracking.

▸ **Dual-agent review is the core design** *(source: @aigc1024)*. A Drafter agent generates a tailored resume and cover letter from your profile; a Reviewer agent — a second Claude agent started with fresh context — independently researches the target company and critiques the draft from a third-party angle. That directly attacks the quality instability of single-pass generation.

▸ **Four commands cover the full loop** *(source: @aigc1024)*. `/setup` builds your career profile (from a documents folder, a single resume, or a guided interview); `/scrape` searches and ranks jobs (built-in Danish portals, plus `/add-portal` to extend to any region); `/apply` generates materials — LaTeX-compiled to an exactly-2-page resume and 1-page cover letter, with ATS verification on the PDF text layer; `/interview` produces staged interview prep with company research, interviewer background, STAR case mapping, and mock interviews.

▸ **Local-first, privacy-safe, fork-and-own** *(source: @aigc1024)*. All data stays on your machine — no SaaS, no privacy leaks. Fork it and change anything.

▸ **Bonus: ColaMD 2.0.0, a markdown editor shipped by a self-taught non-programmer** *(source: @aigc1024)*. The author credits AI coding tools — specifically the ox and terra models — for pushing each version forward, including a notoriously harder iOS build. Now at 1,000+ stars and 1,500+ installs, with Mermaid support, multi-window, custom fonts, and auto-save.

The pattern is the point: complex, subjective workflows become repeatable agent pipelines — and the people shipping those pipelines are the ones getting hired.
