---
title: "WorkBuddy Turns Kindle Into a Dashboard; CoLa Launches Skills Store"
published: true
description: "AI/automation news from Chinese tech channels: an open-source Kindle dashboard hack and CoLa's curated skills store."
tags: [ai, automation, devtools, productivity]
canonical_url: https://dev.to/lanternproton/workbuddy-turns-kindle-into-a-dashboard-cola-launches-skills-store-51n5
devto_id: 4322904
---

Two updates from the Chinese AI community this week — one hardware hack, one ecosystem play.

▸ **Turn any jailbroken Kindle into an always-on dashboard** *(source: @aigc1024 — AI探索指南)*. A developer open-sourced **kindle2workbuddy**, a project that repurposes a Kindle e-reader into a low-power status display for WorkBuddy automation tasks. The flow: Pillow renders a 600×800 grayscale dashboard image on the computer, SCP pushes it to the Kindle, and the `eips` command refreshes the e-ink screen. Result: a constantly-on, battery-friendly screen showing automations, meetings, system metrics, and calendar. It cycles four pages every 30 seconds (a 2-minute loop): ① main dashboard — time, weather, automation tasks, meeting overview, system load; ② system details — disk donut chart, Kindle status, next-run countdown; ③ calendar view — oversized clock, weather, lunar calendar, and the current month with today highlighted; ④ live meeting info — ongoing meetings plus recently ended ones. Caveat: the Kindle must be jailbroken first, and the README carries a brick-your-device warning. Repo: [github.com/MWang-TS/kindle2workbuddy](https://github.com/MWang-TS/kindle2workbuddy).

▸ **CoLa opens a curated AI skills store** *(source: @aigc1024 — AI探索指南)*. "guizang PPT Skills" now has a gold sponsor — CoLa — and is available through CoLa's skills store, where users can install and invoke it (plus future skills) with one click. The store was built by Zang Shifu (藏师傅) and CoLa's collaborators over a long optimization process: every skill is manually vetted and security-tested, and the catalog features top Chinese creators including guizang, baoyu, and Kazik. Overseas skills receive deep Chinese localization, and each listing shows its original source and details. Rather than dumping the entire library into your agent, CoLa says it matches skills intelligently based on your profile and needs. Web version: [colaskill.com](https://colaskill.com).

**Bottom line**: repurposing cheap hardware and curating skill distribution are quietly becoming real channels for AI tooling adoption.
