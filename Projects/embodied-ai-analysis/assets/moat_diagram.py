# -*- coding: utf-8 -*-
"""可约 vs 不可约：一条贯穿物理、计算与智能的定律 —— 框架图"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ---- 中文字体 ----
FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
font_manager.fontManager.addfont(FONT)
font_manager.fontManager.addfont(FONT_B)
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Sans CJK JP"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(15, 10.5), dpi=170)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fafafa")

C_LEFT  = "#1f4e79"; C_LEFT_BG = "#e8f0fa"
C_RIGHT = "#8a3b12"; C_RIGHT_BG = "#fbeee6"
C_DIV   = "#888888"

# ---- 标题 ----
ax.text(50, 96.5, "可约与不可约", ha="center", va="center",
        fontsize=30, fontweight="bold", color="#111111")
ax.text(50, 91.5, "—— 一条贯穿物理、计算与智能的定律 ——",
        ha="center", va="center", fontsize=15, color="#555555")

# ---- 列标题 ----
ax.text(27, 86.5, "可 约 （规律）", ha="center", va="center",
        fontsize=17, fontweight="bold", color=C_LEFT)
ax.text(27, 83.3, "可压缩 · 可泛化 → 会被吞噬", ha="center", va="center",
        fontsize=10.5, color=C_LEFT)
ax.text(73, 86.5, "不 可 约 （历史）", ha="center", va="center",
        fontsize=17, fontweight="bold", color=C_RIGHT)
ax.text(73, 83.3, "不可压缩 · 必须对接 → 永远留下", ha="center", va="center",
        fontsize=10.5, color=C_RIGHT)

# ---- 中央分界线 ----
ax.plot([50, 50], [11, 81.5], color=C_DIV, lw=1.6, ls=(0, (6, 5)), alpha=0.7)

# ---- 行数据 ----
L1 = "有规律的宇宙\n（数学【不合理地有效】）"
R1 = "具体初始条件\n与演化轨迹"
L2 = "压缩 = 泛化\n（Solomonoff 归纳）"
R2 = "计算不可约（Wolfram）\n→ 必须【跑一遍】才知道"
L3 = "通用吞噬特殊\n（图灵通用性）"
R3 = "外部目的不可内化\n（specification 来自外部）"
L4 = "模型吞掉可复用的"
R4 = "harness 对接现实\n（私有 · 异质 · 问责）"
L5 = "编排 / 提示 / RAG\n→ 会被吃掉"
R5 = "私有数据 / 组织流程 / 责任链\n→ 永远留下"

rows = [
    (76.0, "物  理",   L1, R1),
    (62.5, "智  能",   L2, R2),
    (49.0, "计  算",   L3, R3),
    (35.5, "软件工程", L4, R4),
    (22.0, "实  践",   L5, R5),
]

BOX_W, BOX_H = 34, 11.0
for y, layer, left, right in rows:
    ax.text(50, y, layer, ha="center", va="center", fontsize=11.5,
            fontweight="bold", color="#444444",
            bbox=dict(boxstyle="round,pad=0.45", fc="white", ec="#cccccc", lw=1.2))
    ax.add_patch(FancyBboxPatch((10, y-BOX_H/2), BOX_W, BOX_H,
        boxstyle="round,pad=0.6,rounding_size=1.2", fc=C_LEFT_BG, ec=C_LEFT, lw=1.6))
    ax.text(10+BOX_W/2, y, left, ha="center", va="center", fontsize=11.5, color=C_LEFT)
    ax.add_patch(FancyBboxPatch((56, y-BOX_H/2), BOX_W, BOX_H,
        boxstyle="round,pad=0.6,rounding_size=1.2", fc=C_RIGHT_BG, ec=C_RIGHT, lw=1.6))
    ax.text(56+BOX_W/2, y, right, ha="center", va="center", fontsize=11.5, color=C_RIGHT)

# ---- 纵向流程箭头 ----
for y0, y1 in [(76,62.5),(62.5,49),(49,35.5),(35.5,22)]:
    for x in (27, 73):
        ax.add_patch(FancyArrowPatch((x, y0-BOX_H/2-1.4), (x, y1+BOX_H/2+1.2),
            arrowstyle="-|>", mutation_scale=15, color="#999999", lw=1.3))

# ---- 结论条 ----
ax.text(27, 14.6, "会被吃掉", ha="center", va="center", fontsize=14.5,
        fontweight="bold", color=C_LEFT)
ax.text(73, 14.6, "永远留下", ha="center", va="center", fontsize=14.5,
        fontweight="bold", color=C_RIGHT)

# ---- 地板 ----
ax.add_patch(FancyBboxPatch((14, 3.0), 72, 7.8,
    boxstyle="round,pad=0.6,rounding_size=1.2", fc="#f0f0f0", ec="#aaaaaa", lw=1.6))
ax.text(50, 7.0, "地  板：为什么宇宙是有规律的？", ha="center", va="center",
        fontsize=13.5, fontweight="bold", color="#333333")
ax.text(50, 4.2, "（Wigner：数学的不合理有效性 · 至今无解 · 再往下是形而上学）",
        ha="center", va="center", fontsize=9.8, color="#777777")

# ---- 实用判据 ----
ax.text(97, 95.5, "判断会不会被 AI 吞掉：\n问它是【规律】还是【历史】",
        ha="right", va="center", fontsize=10.5, color="#7a6a1a",
        bbox=dict(boxstyle="round,pad=0.6", fc="#fffbe6", ec="#e0c86a", lw=1.2))

plt.tight_layout()
out = "/tmp/moat_diagram.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
