# -*- coding: utf-8 -*-
"""「吞噬边界」系列总封面"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
font_manager.fontManager.addfont(FONT)
font_manager.fontManager.addfont(FONT_B)
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Sans CJK JP"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(16, 9), dpi=180)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

BLUE = "#1f4e79"; ORANGE = "#8a3b12"

# 背景分区
ax.axvspan(0, 50, color="#eef4fb", zorder=0)
ax.axvspan(50, 100, color="#fbf1ea", zorder=0)

# 标题
ax.text(50, 81, "吞  噬  边  界", ha="center", va="center",
        fontsize=56, fontweight="bold", color="#111111")
ax.text(50, 69.5, "T H E   A B S O R P T I O N   B O U N D A R Y",
        ha="center", va="center", fontsize=13, color="#888888")
ax.text(50, 61.0, "从 AI 产业现象  →  宇宙结构  →  设备终局",
        ha="center", va="center", fontsize=14.5, color="#555555")

# 中央分界线
ax.plot([50, 50], [12, 52], color="#999999", lw=2.0, ls=(0, (7, 6)), zorder=3)

# 左：可约
ax.text(27, 45.5, "可 约", ha="center", va="center", fontsize=20,
        fontweight="bold", color=BLUE)
ax.text(27, 39.0, "规律 · 可压缩 · 可泛化", ha="center", va="center",
        fontsize=12, color="#4a7aa0")
ax.text(27, 34.0, "会被吞噬", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color="#c0392b")
ax.text(27, 27.0, "编排 · 提示词 · 通用框架\n模型能力 · 平板 · 折叠屏",
        ha="center", va="center", fontsize=10, color="#6a8aa8", linespacing=1.7)

# 右：不可约
ax.text(73, 45.5, "不 可 约", ha="center", va="center", fontsize=20,
        fontweight="bold", color=ORANGE)
ax.text(73, 39.0, "历史 · 不可压缩 · 必须对接", ha="center", va="center",
        fontsize=12, color="#a8765a")
ax.text(73, 34.0, "永远留下", ha="center", va="center", fontsize=13.5,
        fontweight="bold", color="#1e7a34")
ax.text(73, 27.0, "私有数据 · 组织流程 · 责任链\n高带宽创作 · 数据主权 · 眼镜",
        ha="center", va="center", fontsize=10, color="#a8765a", linespacing=1.7)

# 底部主旨
ax.add_patch(FancyBboxPatch((8, 4.5), 84, 9.5,
    boxstyle="round,pad=0.5,rounding_size=1.5", fc="#111827", ec="none", zorder=4))
ax.text(50, 9.2, "凡「规律」，终将被吞；凡「历史」，永远留下。",
        ha="center", va="center", fontsize=15, fontweight="bold",
        color="white", zorder=5)

plt.tight_layout()
out = "/tmp/series_cover.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
