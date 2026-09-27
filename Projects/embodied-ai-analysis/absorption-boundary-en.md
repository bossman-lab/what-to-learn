# The Absorption Boundary

### From AI industry signals, to the structure of the universe, and back to your next pair of glasses

> Whatever is *law* will be swallowed. Whatever is *history* will remain.

---

## Introduction: A strange pattern

In September 2026, two products went viral for reasons that had nothing to do with being smart.

**Jev** — a model that cannot chat, cannot write essays, cannot generate code. It only makes *judgments*. Yet it ran **193× faster** and **444× cheaper** than frontier models, and within days developers had built **600+ open-source projects** around it.

**Muse** — Meta's consumer AI agent. Ten days after launch, it hit **2.5 million downloads** and knocked ChatGPT off the top of the US App Store. Its three selling points were *low barrier*, *money saved*, and *feeling safe*. Not once did Meta advertise intelligence.

Meanwhile, one number tells the other half of the story: **nearly 65% of enterprise AI projects failed in 2025** — and the dominant cause was *context drift and memory loss*, not insufficient model capability.

These facts point at a single structure:

> **Models swallow whatever is reusable. Harnesses do the interface work of connecting to reality.**

This essay traces that structure from an industry observation down to computation, intelligence, and physics — and then back up to the most concrete question of all: which device to bet on.

---

## Part I: The moat that moved

### Models have no moat

In March 2023, the industry believed that model capability *was* the moat: training costs were astronomical, data was irreproducible, algorithms were secret.

Two months later, an internal Google memo leaked: **"We Have No Moat, And Neither Does OpenAI."** It was mocked as sour grapes. Three years later, it was right — just right about the wrong layer.

The evidence is overwhelming:

- GPT-4-class capability → reproduced by many labs
- GPT-3-class capability → reproduced widely
- GPT-2-class capability → trainable by almost anyone
- **August 2026: three Chinese labs shipped frontier-class models within three days** (DeepSeek V4-Pro, Zhipu GLM-5.3, Alibaba Qwen3.8-27B under Apache 2.0)
- Open weights turned frontier capability into a free commodity

**The half-life of model capability is shrinking. Today's moat is next year's baseline.**

### The real moat is complementary assets

The NBER paper *Old Moats for New Models* supplies the framework via two concepts:

- **Appropriability** — can a firm control the knowledge its innovations produce? In AI: **extremely low**.
- **Complementary assets** — does entry require specialized resources incumbents can ration? In AI: **extremely high**.

The complementary assets in question:

| Asset | Barrier |
|---|---|
| Training compute | 100k+ GPUs; $1B+ per training run |
| Inference scale economics | Unit cost must be lowest |
| Distribution | Billion-user entry points |
| Data flywheel | Feedback improves the model |
| Capital endurance | Annual capex in the hundreds of billions |

So: **AI's moat is not in the model. It is around the model.**

### The counterintuitive evidence

Revenue is radically concentrated:

- **Anthropic: ~$65B ARR (July 2026)**, up from ~$9B in 2025
- **OpenAI: ~$40B ARR**

If models truly had no moat, why is the money concentrated in two or three players?

**Because the money is not paid for the *model*. It is paid for the *product system, distribution, and reliability*.**

### The scissors structure

| Layer | Moat status |
|---|---|
| **Model capability** | ❌ None — permanently commoditizing |
| **Complementary assets** | ✅ Very deep — consolidating |
| **Product system** | ⚠️ Real but fragile |

```
Model capability:    ↘ commoditizing (price falls yearly)
Complementary assets: ↗ consolidating (capex arms race)
                       └─ the gap = structural tension
```

**The practical conclusion: stand on the complementary-assets side — data, verification, supply chain, distribution — not on the model side.**

---

## Part II: The harness era

### The formula

By 2026 the industry's vocabulary had shifted from "our model is stronger" to "our system gets work done." A formula spread:

> **Agent = Model (brain) + Harness (reins)**
> The deciding factor in deployment is the *latter*, not the model itself.

**The harness** is everything wrapped around the model that lets it *act* rather than merely *answer*: tool orchestration, context engineering, memory, retry and routing, cost and latency control, safety, and the judgment layer.

### Why now

Two conditions matured simultaneously:

**1. Models crossed the "good enough" threshold.** Value's marginal return is:

$$\frac{dV}{dC} = \underbrace{\frac{dV}{dM}}_{\text{demand saturates}} \times \underbrace{\frac{dM}{dC}}_{\text{supply gets pricier}}$$

Two decreasing functions multiplied → **accelerating decline**. This is not a "bottleneck" (which implies stasis) and not merely a "plateau." It is a **zone of diminishing marginal value** — the value *migrates*.

**2. Models keep commoditizing.** Open weights turn frontier capability into a free input. When the model is a commodity, differentiation can only live outside the model.

### The brutal corollary

Harness is *not* a permanent moat. Its history is a history of being swallowed:

| Former harness | Status |
|---|---|
| Chain-of-thought prompting | ✅ Eaten by native reasoning models |
| Prompt engineering | ✅ Eaten by instruction tuning |
| RAG orchestration | ⏳ Being eaten by long context |
| Generic tool orchestration | ⏳ Being eaten by native function calling |

**Rule: any harness technique that is *standardizable and generalizable* will be eaten by the next model. Only the part that interfaces with concrete reality survives.**

A counterintuitive corollary: **protocol standardization (MCP, A2A) actually accelerates absorption**, because it makes interfaces generically learnable. What resists absorption is what *cannot* be standardized: private, heterogeneous, accountability-bound.

---

## Part III: The Jev case — a revolution in the objective function

Jev's author is **Diogo Almeida**, a co-inventor of ChatGPT (he worked on RLHF and InstructGPT). His question:

> "After co-inventing ChatGPT, I kept asking: **why didn't a superhuman chat model bring AGI?**"

His answer:

> "Today's AI is very good at *assisting*, but not yet at *automating*."
> "Why do LLMs always need a human in the loop? Because when we trained them, we **literally put a human in that loop**."

### Three technical cores

**1. No generation — only judgment.** Jev outputs typed probabilistic decisions: *Noul* (boolean, 0–1), *Choice* (up to 255 options), *Score* (a scale). No free text. Output *is* structure — no JSON prompting, no parser, no parse failures.

**2. Parallel sampling.** Because output is a fixed-structure decision rather than a variable-length sequence, there is no sequential dependency → all outputs in one forward pass. Result: **70–500 ms** end-to-end vs 3–329 s for frontier models; input at **$0.042/M tokens**, output free.

**3. RLCD — calibrated decisions.** This is the real core:

> "If a model can do a task 95% of the time but won't tell you when it's in that 5%, **you cannot automate the task**."

RLCD (Reinforcement Learning for Calibrated Decisions) enforces: *if the model says 80%, roughly 80% of its 80% judgments should actually be true.*

That turns directly into engineering:

```
confidence > 90%  → auto-execute
70–90%            → escalate to a stronger model
< 70%             → hand to a human
```

**This is the first time "lights-out automation" became engineering-feasible.**

### The deeper point

RLHF taught models *what answers humans prefer*. That is a feature for chat and a **fatal flaw for automation**, because it optimizes for *agreeableness*, not *accuracy*. Jev is a revolution in the objective function: from "make people like it" to "make judgments calibratable."

**Jev's lesson is not "small models beat big models." It is "the objective function beats the parameter count."**

⚠️ Caveat: "Zero hallucinations" means *no type errors* — the output never leaves the defined format. TypeSafe's own FAQ admits Jev "can still be wrong." Calibration's value is precisely that it lets you *know when it might be wrong*.

---

## Part IV: Reducible and irreducible — the law

### Layer 1: Compressibility is the precondition of intelligence

**Kolmogorov complexity** K(x) = length of the shortest program outputting x. A basic theorem: **the vast majority of strings are incompressible** (K(x) ≈ |x|). Randomness dominates; "having regularity" is a mathematically rare event.

Therefore: **intelligence (= optimal prediction = compression) can only exist in a *compressible* world.** Compressibility is not a bonus — it is the precondition.

### Layer 2: Why is the universe compressible? — this is the floor

We observe a highly compressible universe (a few equations cover everything). That is *not* obvious. Three candidates, none confirmed:

| Answer | Problem |
|---|---|
| **Anthropic** — no observers could exist in an incompressible world | Explains why *we* see regularity, not *why* regularity exists |
| **Mathematical necessity** (Tegmark) — the universe *is* a mathematical structure | Unfalsifiable; defers the question |
| **Brute fact** | An honest surrender |

Wigner (1960) named this **"the unreasonable effectiveness of mathematics."** **This is the floor. Below it lies metaphysics.**

### Layer 3: Intelligence is *thermodynamically* favored

```
The universe has laws (compressible)
  → prediction = compression (mathematical necessity)
  → better predictors dissipate less (Landauer) and minimize surprise (Friston)
  → selection pressure pushes compression capacity up
  → a universal compressor = general intelligence, inevitably
```

Compression is not "cleverness" — it is **energy economy**. **In a compressible universe, compression is a thermodynamic advantage, so selection will inevitably push it into general intelligence.**

### Layer 4: Why the residue never disappears — computational irreducibility

Here is the key turn. Even with all the laws, some things cannot be shortcut:

| | Compressibility | Example |
|---|---|---|
| **Law** | Highly compressible | F=ma summarizes everything |
| **History** | Possibly irreducible | this universe's initial conditions and trajectory |

Bennett's **logical depth**: a string can be compressible yet still require long computation to produce from its compressed form. So there are two kinds of "incompressible":

1. **Information-theoretically incompressible** (truly random) → unpredictable
2. **Computationally irreducible** (lawful but must be *run*) → understandable but unpredictable

**This is the eternal source of the harness:**

| | Belongs to | Why |
|---|---|---|
| **Law** | the model (compressible → generalizable → swallowed) | mathematically reducible |
| **Concrete history** | the harness (must be interfaced) | computationally irreducible → must be *run* |

### Layer 5: The unification

> **"Models swallow the reusable, harnesses interface with reality" is not a software-engineering accident, nor an industry-cycle artifact. It is the necessary tension between two physical facts: *law is compressible*, and *history is computationally irreducible*.**

### Layer 6: One line through everything

| Layer | Reducible side | Irreducible side |
|---|---|---|
| Software engineering | model eats the reusable | harness interfaces with reality |
| Computation | generality eats specificity | external purpose |
| Intelligence | compression = generalization | computational irreducibility |
| Physics | a lawful universe | concrete initial conditions |
| Meta | **reducible** | **irreducible** |

**Both ends are irreducible: one anchors in mathematics, the other in reality. So the line never disappears — it only moves.**

### The practical criterion

> **To judge whether something will be eaten by AI, ask one question: is it *law* or *history*?**
> - **Law** (generalizable, patterned, standardizable) → **will be eaten**
> - **History** (concrete, private, irreducible, accountability-bound) → **will remain**

---

## Part V: The personal cloud computer

### The line everyone missed

Most coverage of Muse discussed saving money and low friction. The real signal was a technical detail:

> **Meta allocates every Muse user an independent, continuously running virtual machine in the cloud.**

Specs: **2 vCPU / 8GB RAM / 100GB SSD**, its own browser, saved credentials, **keeps running after you close the app**, with an internal review system called *Sentinel* and a planned *Confidential VM* (user-held keys).

### The inversion of the device–cloud relationship

| Dimension | Traditional | Muse model |
|---|---|---|
| Execution | device executes, cloud assists | **cloud executes, device interacts** |
| State | device-primary | **cloud-primary, device stateless** |
| Always-on | only when the device is on | **cloud 24/7, device may be offline** |
| Device role | computing terminal | **pure interface (sensorium + actuator)** |
| Devices per state | one each | **one cloud VM serves N devices** |

> **Yesterday: the device was the computer and the cloud was a peripheral. Today: the cloud is the computer and the device is a peripheral.**

This is a **spiral return** to centralization — but *per-user private*, with super-capable terminals and low-latency networks. (Oracle's 1996 Network Computer failed because the conditions weren't ready. In 2026, they are.)

### Different devices, different collaboration modes

```
Collaboration mode = f(device capability, scenario constraint, task owner)
```

| Mode | Devices | Focus |
|---|---|---|
| **Sync** | phone | state coherence + routing (the only dual-primary device) |
| **Uplink** | glasses, watch | perception in, understanding in the cloud |
| **Downlink** | Charm | pure entry; cloud does everything |
| **Local** | earbuds, car, home | autonomy + offline |

**Mismatching the mode = product failure.** A car that sends braking decisions to the cloud is a catastrophe. A keychain that expects local compute is impossible. Glasses that upload all vision collapse on privacy, bandwidth, and battery.

---

## Part VI: The fate of forms

### PC's layered retreat

| Phase | PC covers | Taken by |
|---|---|---|
| 1995–2010 | everything | — |
| 2010–2025 | work + professional creation | **consumption/social — taken by the smartphone** |
| 2025–2035 | high-bandwidth creation + sovereignty | **knowledge work — taken by AI** |

**Each retreat leaves a more irreducible layer.**

A reversal in the data: in 2026 overall PC shipments fell 11–14%, yet **"AI PCs" were the only growth engine** (>50% penetration, 140M+ units). **PC's compute role is not vanishing — it is *transfusing*: from running apps to running local AI inference plus guarding data sovereignty.**

### Foldables are eating tablets

- **Foldables 2026: +21% YoY**; panel shipments +24%, 27.5M units
- **Apple's first foldable iPhone: September 2026**, projected to take **25% share** in year one
- **Tablets 2026: −10% to −11%**

The mechanism: a foldable is **not "a bigger phone" — it is "a foldable tablet."** It grows out of the phone form factor and eats the tablet's function. Huawei's strategy is explicit: make foldables the *only* choice, **replacing "phone + tablet."**

**Tablets are squeezed from both ends** — foldables from below, 2-in-1s from above — because they were always a middle state.

### The deep law: form is reducible, function is irreducible

| Definition | Fate |
|---|---|
| By **form** ("a size/shape") | ❌ eaten by the next form |
| By **function** ("an irreplaceable use") | ✅ survives |

- **By form**: tablet ("a bigger screen"), foldable ("a foldable screen"), laptop screen
- **By function**: phone (personal terminal), PC (high-bandwidth creation + sovereignty), glasses (first-person perception), earbuds (voice), watch (body signals)

**Form eats form — until "screen" itself ceases to be the core of a device.** If AR matures, glasses can virtualize any screen size, and both tablets and foldables lose their reason.

---

## Part VII: The throne is in glasses

### The three-criteria test

| Criterion | Why it matters | Glasses |
|---|---|---|
| **Function-defined** | survives being eaten | ✅ first-person perception |
| **No incumbent OS** | an Agent OS can be born natively | ✅ neither Android nor iOS owns it |
| **High bandwidth + rich context** | can be the primary entry | ✅ vision + audio + first-person situation |

**Glasses score 3/3. Every other device has a fatal flaw:** phones and PCs have incumbent OSes; watches have too little bandwidth; earbuds are audio-only; Charm is form-defined and will be eaten.

**Glasses are the only device that is both a *survivor* and an *eater* — the form that will itself consume every screen.**

### But breakthrough ≠ entry point

- **The biggest prize**: ✅ yes — it can eat every screen
- **The easiest entry**: ❌ no — it has the highest adoption friction

**Four risks: social acceptance (hardest), weight/power/thermals, privacy backlash, and form risk.**

### The social-acceptance moat

**Google Glass (2013) did not die of technology.** Its defects were real but not fatal. It died of *social rejection*: the epithet **"Glasshole,"** bans from restaurants and bars, and a simple social fact — *you might be recording the person talking to you.*

**That is a sociological problem, not an engineering one. No firmware update fixes it.**

It gets worse: glasses' camera + face recognition + AI can identify a stranger and pull their name, address, and family details **in seconds**. The backlash is structural: **the stronger the technology, the stronger the rejection.**

**Meta's demonstrated path:**

1. **Disguise as an ordinary object** — Ray-Ban Meta is indistinguishable from normal Ray-Bans in thickness and weight
2. ⭐ **Ship a camera-less version on purpose** — CTO Bosworth: the camera-less version was road-mapped two years earlier because *"audio is consistently the most popular feature in glasses."* Dropping the camera delivered **three wins at once: lower price, less weight, longer battery**
3. **Visible recording indicator** — make the invisible visible
4. **Standards and regulation** — China has brought AI glasses into standards oversight; building rules rebuilds the social contract
5. **Lead with low-friction forms** — audio glasses and the Charm to bypass the Glasshole effect

**Historical pattern**: phone cameras, Bluetooth earbuds (single-ear used to look *crazy* — until AirPods), smartwatches. **Social acceptance is not a function of technology, but it changes with a signature product.**

**Smart glasses are waiting for their AirPods moment.**

### The ecosystem after glasses break through

| Category | Members |
|---|---|
| **Eaten** | tablets, foldables, TVs/monitors, cameras, some phone scenarios |
| **Attached** | earbuds (audio), watch (body data), keyboard (high bandwidth), ring/wristband (gesture), cloud VM |
| **Born** | optics/waveguides, microdisplays (MicroLED/LCoS), low-power SoC, a glasses-native OS |
| **Unchanged** | sovereignty, accountability, physical contact |

**Note: the PC may become "keyboard + glasses"** — the keyboard stays, the screen moves to the glasses, compute goes to the cloud.

---

## Conclusion

The line runs from an industry observation to the structure of the universe and back to a pair of glasses:

```
Industry signal (Jev, Muse, 65% failure)
  → system explanation (diminishing marginal value; value shifts to the harness)
  → fundamental law (compressibility vs computational irreducibility)
  → architecture extrapolation (device–cloud inversion)
  → device endgame (the fate of forms)
  → strategic target (the throne is in glasses)
  → the floor (why is the universe lawful?)
```

**One sentence holds it together:**

> **Whatever is law will be swallowed. Whatever is history will remain.**

**And the throne is in glasses — but the key is not in compute. It is in social acceptance.**

---

*Six essays and a technical appendix, ten figures, written September 2026. Data from TypeSafe, Counterpoint, Omdia, NBER Working Paper w32474, and public reporting. Figures such as 193.6×/444.6× are vendor self-reported and should be discounted.*
