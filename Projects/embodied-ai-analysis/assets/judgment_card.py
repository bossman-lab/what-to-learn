# -*- coding: utf-8 -*-
"""速判卡：这东西会被 AI 吞掉吗？"""
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

fig, ax = plt.subplots(figsize=(11, 13.5), dpi=170)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

BLUE = "#1f4e79"; BLUE_BG = "#e8f0fa"
ORANGE = "#8a3b12"; ORANGE_BG = "#fbeee6"

# ---- 卡头 ----
ax.add_patch(FancyBboxPatch((4, 88), 92, 9.5,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc="#111827", ec="none"))
ax.text(50, 93.6, "速判卡", ha="center", va="center", fontsize=21,
        fontweight="bold", color="white")
ax.text(50, 89.9, "这东西会被 AI 吞掉吗？", ha="center", va="center",
        fontsize=13, color="#cbd5e1")

# ---- 核心问题 ----
ax.text(50, 82.5, "只问一个问题", ha="center", va="center",
        fontsize=12, color="#888888")
ax.add_patch(FancyBboxPatch((14, 72.5), 72, 8.2,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc="#fffbe6", ec="#e0c86a", lw=1.8))
ax.text(50, 76.6, "它是【规律】还是【历史】？", ha="center", va="center",
        fontsize=17.5, fontweight="bold", color="#7a5a00")

# ---- 分叉箭头 ----
ax.add_patch(FancyArrowPatch((36, 72.2), (27, 66.5), arrowstyle="-|>",
    mutation_scale=20, color=BLUE, lw=2.2))
ax.add_patch(FancyArrowPatch((64, 72.2), (73, 66.5), arrowstyle="-|>",
    mutation_scale=20, color=ORANGE, lw=2.2))

# ---- 左卡：规律 ----
ax.add_patch(FancyBboxPatch((4, 21), 44, 44,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc=BLUE_BG, ec=BLUE, lw=2.2))
ax.text(26, 61.5, "规  律", ha="center", va="center", fontsize=18,
        fontweight="bold", color=BLUE)
ax.text(26, 56.8, "会被吞掉", ha="center", va="center", fontsize=13,
        fontweight="bold", color="#c0392b")
ax.plot([10, 42], [54.2, 54.2], color=BLUE, lw=1.0, alpha=0.4)
ax.text(26, 50.0, "· 可泛化\n· 有模式\n· 可标准化\n· 可复用",
        ha="center", va="center", fontsize=12.5, color=BLUE, linespacing=1.7)
ax.plot([10, 42], [37.5, 37.5], color=BLUE, lw=1.0, alpha=0.4)
ax.text(26, 32.5, "例：\n提示词工程\nRAG 编排\n通用工具编排\n通用框架",
        ha="center", va="center", fontsize=11.5, color="#5a7fa0", linespacing=1.6)

# ---- 右卡：历史 ----
ax.add_patch(FancyBboxPatch((52, 21), 44, 44,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc=ORANGE_BG, ec=ORANGE, lw=2.2))
ax.text(74, 61.5, "历  史", ha="center", va="center", fontsize=18,
        fontweight="bold", color=ORANGE)
ax.text(74, 56.8, "会留下", ha="center", va="center", fontsize=13,
        fontweight="bold", color="#1e7a34")
ax.plot([58, 90], [54.2, 54.2], color=ORANGE, lw=1.0, alpha=0.4)
ax.text(74, 50.0, "· 具体\n· 私有\n· 不可约\n· 要问责",
        ha="center", va="center", fontsize=12.5, color=ORANGE, linespacing=1.7)
ax.plot([58, 90], [37.5, 37.5], color=ORANGE, lw=1.0, alpha=0.4)
ax.text(74, 32.5, "例：\n私有数据\n组织流程\n责任链\n领域直觉",
        ha="center", va="center", fontsize=11.5, color="#a8765a", linespacing=1.6)

# ---- 底层原因 ----
ax.add_patch(FancyBboxPatch((11, 9.5), 78, 8.5,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc="#f0f0f0", ec="#aaaaaa", lw=1.5))
ax.text(50, 15.5, "底层原因", ha="center", va="center",
        fontsize=11, color="#888888")
ax.text(50, 11.8, "可压缩性（数学）   ·   计算不可约性（物理）",
        ha="center", va="center", fontsize=13.5, fontweight="bold", color="#333333")

# ---- 页脚 ----
ax.text(50, 4.5, "凡「规律」，终将被吞；凡「历史」，永远留下。",
        ha="center", va="center", fontsize=12, style="italic", color="#666666")

plt.tight_layout()
out = "/tmp/judgment_card.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
