# -*- coding: utf-8 -*-
"""规律从未知到被计算机高效抽象：七阶段流程"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
font_manager.fontManager.addfont(FONT)
font_manager.fontManager.addfont(FONT_B)
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Sans CJK JP"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(15.5, 15.5), dpi=160)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

BLUE="#1f4e79"; PURPLE="#6a3d9a"; GOLD="#c08a00"; GREEN="#1e7a34"; RED="#c0392b"
TEAL="#0e7490"

ax.text(50, 97.2, "规律：从未知到被计算机高效抽象",
        ha="center", va="center", fontsize=20, fontweight="bold", color="#111")
ax.text(50, 94.0, "七个阶段 —— 每一步都是一次「表示的变换」",
        ha="center", va="center", fontsize=11.5, color="#888")

# 左侧阶段竖标
stages = [
    ("① 观测",   "世界 → 数据",   "仪器扩展可观测范围",           BLUE,   "瓶颈：只能问你已能问的问题"),
    ("② 发现",   "数据 → 规律",   "压缩：在假设空间里找最短描述",  PURPLE, "瓶颈：搜索不可约"),
    ("③ 形式化", "规律 → 符号",   "用精确语言重写（数学 / 逻辑）", GOLD,   "无鸿沟 —— 这一步是加速器"),
    ("④ 算法化", "符号 → 过程",   "求解 / 离散化 / 数值方法",      TEAL,   "瓶颈：计算不可约，必须跑"),
    ("⑤ 高效化", "过程 → 快过程", "发现结构：FFT · 并行 · 硬件匹配", GREEN,  "数量级收益的真正来源"),
    ("⑥ 学习",   "数据 → 表示",   "参数化 + 梯度下降（自动压缩）",  RED,    "代价：隐式，写不出规律"),
    ("⑦ 泛化",   "表示 → 能力",   "压缩 → 抓住共同结构",           "#475569", "仍脆弱：外推不可靠"),
]

y = 89.5
H = 8.8
for i, (name, flow, mech, c, caveat) in enumerate(stages):
    ax.add_patch(FancyBboxPatch((5, y-H), 90, H,
        boxstyle="round,pad=0.45,rounding_size=1.2", fc="#ffffff", ec=c, lw=1.9))
    # 阶段名
    ax.add_patch(FancyBboxPatch((5, y-H), 15, H,
        boxstyle="round,pad=0.45,rounding_size=1.2", fc=c, ec="none"))
    ax.text(12.5, y-H/2, name, ha="center", va="center", fontsize=12.5,
            fontweight="bold", color="white")
    # 变换
    ax.text(22.5, y-3.1, flow, ha="left", va="center", fontsize=11.5,
            fontweight="bold", color=c)
    # 机制
    ax.text(22.5, y-6.6, mech, ha="left", va="center", fontsize=9.6, color="#555")
    # 瓶颈/代价
    ax.text(93.5, y-H/2, caveat, ha="right", va="center", fontsize=9.2,
            color=c, style="italic")
    if i < len(stages)-1:
        ax.add_patch(FancyArrowPatch((50, y-H-0.25), (50, y-H-1.75),
            arrowstyle="-|>", mutation_scale=15, color="#9aa8b6", lw=1.9))
    y -= (H + 1.6)

# 底部
ax.add_patch(FancyBboxPatch((5, 1.0), 90, 6.2,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#111827", ec="none"))
ax.text(50, 5.5, "「高效」不来自算力，来自【发现结构】",
        ha="center", va="center", fontsize=13, fontweight="bold", color="white")
ax.text(50, 2.8, "同一个规律，换一种表示，速度差几个数量级 —— FFT 之于朴素求和即为例证",
        ha="center", va="center", fontsize=9.8, color="#cbd5e1")

plt.tight_layout()
out = "/tmp/law_pipeline.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
