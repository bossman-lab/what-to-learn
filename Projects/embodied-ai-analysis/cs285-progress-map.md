# CS 285 对照表：你已会 vs 需要补（2026-08-02）

> 依据：你已完成的动手实验（GRPO 训练 6/22、CartPole PPO 7/12）
> 课程：UC Berkeley CS 285 Deep Reinforcement Learning (Levine)

| 讲 | 标题 | 你的现状 | 行动 |
|----|------|---------|------|
| L01 | 课程概览 | 🟢 行业认知已具备 | 跳过 |
| L02 | Supervised Learning of Behaviors（行为克隆） | 🟡 概念接触过（LLM SFT 背景） | 快进看 BC 的局限部分 |
| L03 | Supervised Learning of Behaviors 续 | 🟡 同上 | 快进 |
| L04 | **Reinforcement Learning Basics（MDP/奖励）** | 🟡 GRPO 实验里用过 reward 函数，但 MDP 形式化没系统学过 | **精读** ⭐ |
| L05 | **Policy Gradients（策略梯度）** | 🟡 GRPO 本质就是策略梯度变体，你实现过但可能没意识到理论框架 | **精读** ⭐（GRPO 论文的直接前置） |
| L06 | **Actor-Critic** | 🔴 没系统学过 | **精读** ⭐ |
| L07 | **Value-Based RL（Q-learning）** | 🔴 没学过 | **精读** ⭐ |
| L08 | Q-Learning in Practice | 🟡 用过 DQN 类工具但没看理论 | 精读 |
| L09 | Off-Policy Policy Gradient | 🟡 与 PPO 相关（你跑过 PPO） | 精读 |
| L10 | **Advanced Policy Gradient（PPO/TRPO）** | 🟢 亲手实现过 PPO（CartPole 493.6/500） | **巩固**：对照理论查漏 |
| L11 | Variational Inference | 🔴 没接触 | 略读（数学重，先了解动机） |
| L12 | Variational Inference in RL | 🔴 | 略读 |
| L13 | Control as Variational Inference | 🔴 | 略读 |
| L14 | **RL with Sequences & LMs（RLHF 相关）** | 🟢 GRPO 就是干这个的 | **精读** ⭐（你的主场） |
| L15 | Model-Based RL | 🟡 了解概念 | 精读 |
| L16 | Model-Based RL Algorithms | 🟡 | 精读 |
| L17 | **Offline Reinforcement Learning** | 🔴 没学过 | **精读** ⭐（具身智能数据稀缺场景核心） |
| L18 | Offline RL Algorithms | 🔴 | 精读 |
| L19 | Exploration | 🟡 有直觉 | 精读 |
| L20 | RL Theory | 🔴 数学重 | 按需略读 |

## 推荐学习路径（约 4-6 周）

### 第一优先级（你已经"会做"，补"为什么"）—— 2 周
```
L04 → L05 → L06 → L10 → L14
```
这 5 讲覆盖你实验用到的全部核心：reward 设计、策略梯度、AC 框架、PPO、LLM RL。
**产出**：1 篇 dev.to 文章《我从 GRPO 实验反推 CS 285 理论框架》——用你的实验讲理论，比纯笔记更有辨识度。

### 第二优先级（具身智能必备，完全没接触）—— 2-3 周
```
L07 → L08 → L09 → L17 → L18
```
Value-based 是 DQN 家族（机器人感知-控制常用）；Offline RL 是具身智能数据稀缺时的核心方法。
**产出**：R1 到手后的 sim-to-real 实验会用到 Offline RL，先打理论底。

### 第三优先级（可选）—— 按需
```
L11-L13（变分推断，数学重）→ L15-L16（Model-Based，机器人领域价值高）
```

## 每周节奏
- 精读讲：1-2 讲/周（看视频 1.5x + 过 slides + 记 1 页笔记）
- 笔记沉淀：每 5 讲 → 1 篇 dev.to 英文 + 公众号中文
- 对照实验：每学完一讲，回看你 GRPO/PPO 代码里对应的地方（代码注释里标 lecture 引用）

## 里程碑
- 8 月中：完成第一优先级 5 讲 + 第 1 篇文章
- 8 月底：完成 L07-L09 + 第 2 篇文章
- 9 月：Offline RL 2 讲 + 开始 CS 287（机器人学）
