# -*- coding: utf-8 -*-
"""「吞噬边界」系列全貌总图"""
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

fig, ax = plt.subplots(figsize=(15, 17), dpi=155)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

ax.text(50, 97.6, "吞 噬 边 界 · 系列全貌",
        ha="center", va="center", fontsize=23, fontweight="bold", color="#111")
ax.text(50, 94.3, "从 AI 产业现象，到宇宙结构，再到设备终局",
        ha="center", va="center", fontsize=12.5, color="#666")
ax.text(50, 91.2, "6 篇正文 + 1 篇姊妹篇 + 2 篇技术附篇 + 16 张图",
        ha="center", va="center", fontsize=10.2, color="#999")

descend = [
    ("篇一", "护城河的迁徙",     "现象",     "#93c5fd", "#1f4e79"),
    ("篇二", "缰绳时代",         "系统",     "#7eb3ea", "#1f4e79"),
    ("附一", "Jev 技术拆解",     "案例",     "#6AA0DC", "#123a5c"),
    ("篇三", "可约与不可约",     "法则·空间", "#8b7bc4", "#4c3d7a"),
    ("姊妹", "为什么发展是递进的","法则·时间", "#7a68b8", "#4c3d7a"),
]
ascent = [
    ("附二", "规律如何被高效抽象","案例·工程", "#d9b45c", "#8a6d00"),
    ("篇四", "个人云计算机",     "推演",     "#8fbf9c", "#1e7a34"),
    ("篇五", "形态的宿命",       "收官",     "#77b487", "#1e7a34"),
    ("篇六", "王座在眼镜",       "终章",     "#5fa871", "#14562a"),
]

H = 6.0
y = 85.0
ax.text(6, y+3.4, "往深处挖", ha="left", va="center", fontsize=11.5,
        fontweight="bold", color="#4c3d7a")
for tag, title, layer, bg, tc in descend:
    ax.add_patch(FancyBboxPatch((14, y-H), 62, H,
        boxstyle="round,pad=0.4,rounding_size=1.0", fc=bg, ec="none"))
    ax.text(17.5, y-H/2, tag, ha="left", va="center", fontsize=10.5,
            fontweight="bold", color="#ffffff")
    ax.text(25, y-H/2, "《" + title + "》", ha="left", va="center",
            fontsize=12.5, fontweight="bold", color=tc)
    ax.text(89, y-H/2, layer, ha="center", va="center", fontsize=9.6,
            color=tc, style="italic")
    y -= (H + 1.0)

# 地板
ax.add_patch(FancyBboxPatch((6, y-H+0.4), 88, H-0.5,
    boxstyle="round,pad=0.4,rounding_size=1.0", fc="#111827", ec="none"))
ax.text(50, y-H/2+0.2, "地  板   ｜   为什么宇宙可压缩？—— 至今无公认答案",
        ha="center", va="center", fontsize=11.5, fontweight="bold", color="white")
y -= (H + 0.4)

ax.text(6, y-3.6, "带回地面", ha="left", va="center", fontsize=11.5,
        fontweight="bold", color="#1e7a34")
for tag, title, layer, bg, tc in ascent:
    ax.add_patch(FancyBboxPatch((14, y-H), 62, H,
        boxstyle="round,pad=0.4,rounding_size=1.0", fc=bg, ec="none"))
    ax.text(17.5, y-H/2, tag, ha="left", va="center", fontsize=10.5,
            fontweight="bold", color="#ffffff")
    ax.text(25, y-H/2, "《" + title + "》", ha="left", va="center",
            fontsize=12.5, fontweight="bold", color=tc)
    ax.text(89, y-H/2, layer, ha="center", va="center", fontsize=9.6,
            color=tc, style="italic")
    y -= (H + 1.0)

# 三句话
ax.add_patch(FancyBboxPatch((6, 1.6), 88, 11.0,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#f0f0f0", ec="#aaa", lw=1.5))
ax.text(50, 10.7, "三句话收束全系列", ha="center", va="center",
        fontsize=10.5, color="#888")
ax.text(50, 7.7, "凡「规律」，终将被吞；凡「历史」，永远留下。",
        ha="center", va="center", fontsize=11.8, fontweight="bold", color="#333")
ax.text(50, 5.0, "规律明确，但路径必须一层一层地走出来。",
        ha="center", va="center", fontsize=11.8, fontweight="bold", color="#333")
ax.text(50, 2.5, "工具先于理论，结构先于算力。",
        ha="center", va="center", fontsize=11.8, fontweight="bold", color="#333")

plt.tight_layout()
out = "/tmp/series_overview.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
