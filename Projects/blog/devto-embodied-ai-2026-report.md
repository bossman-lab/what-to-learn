---

title: China Ships 84.7% of the World's Humanoid Robots — What the 3 Biggest 2026 Reports Actually Say
published: false
description: Three 2026 industry reports on embodied AI and humanoid robots land the same number: 84.7%. Unitree shipped 5,500 units. Funding hit $46B. I read all three so you don't have to.
tags: robotics, ai, china, embodiedai, industryanalysis
canonical_url: https://dev.to/lanternproton/china-ships-847-of-the-worlds-humanoid-robots-what-the-3-biggest-2026-reports-actually-say
cover_image: 

---

## 84.7%

That's the number that jumps out of every 2026 report on embodied AI and humanoid robots.

**China shipped 84.7% of the world's humanoid robots in 2025.** For every 10 humanoid robots built last year, more than 8 came from Chinese factories.

This isn't a PowerPoint story. **Unitree shipped 5,500 units in 2025.** Zhiyuan (智元) shipped over 5,000. The combined output of these two companies exceeds every other player in the world *combined*.

2026 is being called "the mass production inflection year" for humanoid robots. I read three major reports — from **Robot Lecture Hall (机器人大讲堂)**, **36Kr Research Institute**, and **HCR (慧辰股份)** — and pulled out the signal.

---

## 1. The Market Reality: RMB 1 Trillion

36Kr's headline number: China's embodied AI market grew from RMB 213.3B in 2018 to RMB 915B in 2025. **It's expected to cross RMB 1 trillion in 2026.**

Zooming into humanoid robots specifically, HCR gives a more granular trajectory:

| Year | Market Size | Driver |
|------|------------|--------|
| 2023 | ~RMB 0.1B | Nascent |
| 2025 | **RMB 3.5B** | R&D procurement, government demos, industrial pilots |
| 2027E | **RMB 15.6B** | Transitioning from small-batch to scaled replication |
| 2030E | **RMB 106.8B** | Crossing the hundred-billion mark |

**Critical caveat from HCR: growth decelerates after 2028.** The competition shifts from "can we build it" to "can we deliver reliably and prove ROI."

---

## 2. Capital Inflow: 4x in One Year

The funding numbers are staggering:

- **RMB 33.47B ($4.6B) in the first 11 months of 2025** — 4x the same period in 2024
- Over **305 funding rounds** totaling **RMB 38B+** for the full year
- Over **600 investing institutions** participated

Humanoid robotics alone captured **35%** of all robotics funding in 2025, overtaking industrial robots, service robots, and core components. Capital has voted: this is the inflection.

---

## 3. The Tech Stack: World Models > Hardware

All three reports converge on the same technical thesis: **world models are the critical path to AGI in robotics.**

> "Stanford's team demonstrated algorithms that can predict object motion trajectories. Carnegie Mellon released a 100,000-hour dataset of robot manipulation videos covering home and factory environments."

The end-to-end embodied large model has graduated from labs. In a pilot factory in Shenzhen, robots follow voice commands like "put the red part in bin #3" with **>95% accuracy**.

Robot Lecture Hall's tech stack summary is the cleanest I've seen:

| Layer | What's Happening |
|-------|-----------------|
| **Brain** | End-to-end embodied LLM; multimodal perception + autonomous decision-making deeply integrated |
| **Hardware** | Servo motor/reducer precision improvements; full-terrain adaptation; Optimus Gen 2 walking on gravel |
| **Mass Production** | Shifting from single-function to general-purpose; "general intelligence + general body" paradigm |

---

## 4. The Two Leaders: Unitree vs. Zhiyuan

HCR's report has the hardest quantitative data:

| Company | 2025 Shipments | Strategy | Price Point |
|---------|---------------|----------|-------------|
| **Unitree** | 5,500 (global #1) | Full-stack in-house components, motion control excellence | Entry-level ~$1,400 (RMB 10K) |
| **Zhiyuan** | 5,000+ | "Body + AI + Data" closed loop, large model driven | Mid-to-high end |

Everyone else — Ubtech, Leju, Galaxy General, Songyan Power — is in the second tier.

**The two strategies are already diverging:**
- **Unitree path**: cost-driven, motion-control-first, primarily education/research revenue
- **Zhiyuan path**: AI-first, deep integration into industrial manufacturing and logistics

Product prices span from **RMB 10K to RMB 700K** ($1,400 to $97,000). No homogeneous competition — the industrial tier has formed.

**2026**: leading factories are scaling from thousands to tens of thousands of units per year.

---

## 5. The BOM: 62% Goes to Brain + Joints

HCR's cost breakdown is worth memorizing:

| Component | % of BOM | Key Parts |
|-----------|---------|-----------|
| Computing & Actuation | **62%** | Joint actuators, AI compute modules, dexterous hands |
| Sensing & Power | 15% | Sensors, batteries |
| Structure & Manufacturing | 23% | Body, chassis |

**The 62% category is where the bottlenecks are** — and where localization gains will compound. It's also the primary reason Chinese humanoids cost **~50% of comparable overseas products**.

---

## 6. Regional Clusters: Three Cities, Three Strategies

| City | Positioning | Key Data |
|------|------------|----------|
| **Beijing Haidian** | Innovation source | 300+ companies; 19,000 R&D personnel; birthed Emu3 (world's first unified multimodal world model) |
| **Beijing Future Science City** | Industry-academia hub | 136+ companies; RMB 14.93B revenue; targeting 100B-level cluster |
| **Shanghai Zhangjiang (Yangtze Delta)** | Full-chain closed loop | 100+ companies; 80+ OEM/supplier ecosystem |

The differentiation is real: Beijing = innovation origin, Shanghai = application showcase, Shenzhen = ecosystem chain.

---

## 7. The Commercialization Path: Three Jumps

All three reports converge on a "ToB-first, multi-scenario gradient" model:

| Phase | Timeline | Primary Scenarios |
|-------|----------|-------------------|
| **Capability building + demo verification** | 2025-2027 | University R&D (**70% of projects**), government pilots (**70% of contract value**) |
| **Controlled B2B scale production** | 2028-2030 | Automotive manufacturing, warehousing & logistics, energy inspection |
| **General physical intelligence** | 2030+ | Robots as deployable general-purpose labor assets |

**The fundamental tension right now:** 70% of projects come from universities; 70% of money comes from state-owned enterprises. True commercialization — enterprises buying because it *pays back* — won't be proven until 2028+.

---

## 8. Reality Check: Three Boundaries

After reading 100+ pages across three reports, here's what the reports *don't* emphasize but I think matters:

### 1. 84.7% ≠ tech dominance
The global humanoid robot base is tiny (~10-20K units in 2025). China's share reflects **supply chain depth and cost advantage**, not a model layer lead. The US still leads on AI models and advanced sensors.

### 2. The real TAM bottleneck isn't production — it's ROI
A humanoid robot with a BOM of RMB 100-300K ($14K-$42K) replacing a worker earning RMB 120K/year ($17K) takes **2-3 years to break even**. The explosion only happens when price hits RMB 50K ($7K) *and* reliability meets factory floor standards. This is why HCR specifically calls out "post-2028 growth deceleration."

### 3. World models are real progress, but nowhere near done
Current end-to-end models perform at 95%+ in controlled settings. In the wild — unfamiliar objects, unseen terrain, unexpected disturbances — they still fail almost every time. The hard problem isn't motion control. **It's understanding the physical world.**

---

## What I'd Watch

Three signals for the next 18 months, in order:

1. **Unitree and Zhiyuan's 2026 delivery numbers** — are we talking 10K or 50K? The gap tells you if robots are real products or glorified demos.

2. **BOM cost trajectory** — the fastest path to market expansion isn't better AI; it's cheaper joints. Watch the actuator supply chain.

3. **The first non-government repeat buyer** — the day a factory chain places its *third* order without subsidy is the day the industry actually arrived.

---

*Sources: Robot Lecture Hall (机器人大讲堂) — 2026 Embodied Intelligence & Humanoid Robot Industry Report; 36Kr Research Institute — 2026 Embodied Intelligence Industry Development Report; HCR (慧辰股份) — 2026 China Embodied Intelligence Industry Series Report: Humanoid Robot Edition*

---

<p><em>Found this useful? Follow me on <a href="https://dev.to/lanternproton">dev.to/lanternproton</a> — I write about the intersection of AI infrastructure, strategy, and the semiconductor supply chain. No hype, just frameworks.</em></p>
