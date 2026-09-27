# -*- coding: utf-8 -*-
"""下挖一层：为什么发现规律本身也不可约——直到地板"""
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

fig, ax = plt.subplots(figsize=(14, 14), dpi=165)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

ax.text(50, 97.0, "再下挖一层：为什么「发现」本身也不可约",
        ha="center", va="center", fontsize=19, fontweight="bold", color="#111")
ax.text(50, 93.5, "一层一层问下去，直到地板",
        ha="center", va="center", fontsize=11.5, color="#888")

# 渐深的配色
shades = ["#eef4fb", "#e3edf8", "#d5e5f5", "#c2daf0", "#adcfe8"]
edges  = ["#1f4e79", "#1f4e79", "#1f4e79", "#1f4e79", "#1f4e79"]

layers = [
    ("① 为什么发展是递进的？", "因为三道鸿沟：认识 · 计算 · 实现"),
    ("② 为什么「发现」不可约？", "因为发现是在假设空间里搜索，且验证必须「问世界」"),
    ("③ 为什么搜索空间这么大？", "因为问题空间本身在【展开】——你只能问你已能问的问题"),
    ("④ 为什么规律是分层的？", "因为可压缩性在每个尺度上都成立（细节被平均掉）"),
    ("⑤ 为什么「可压缩」？", "—— 这是地板 ——"),
]

y = 86.0
H = 12.0
for i, (q, a) in enumerate(layers):
    bg = shades[i] if i < 4 else "#111827"
    ec = edges[i] if i < 4 else "#111827"
    tc = "#111" if i < 4 else "#ffffff"
    ac = "#555" if i < 4 else "#cbd5e1"
    ax.add_patch(FancyBboxPatch((8, y-H), 84, H,
        boxstyle="round,pad=0.5,rounding_size=1.3", fc=bg, ec=ec, lw=1.9))
    ax.text(50, y-4.0, q, ha="center", va="center", fontsize=13.5,
            fontweight="bold", color=tc)
    ax.text(50, y-8.6, a, ha="center", va="center", fontsize=10.8,
            color=ac, linespacing=1.4)
    if i < len(layers)-1:
        ax.add_patch(FancyArrowPatch((50, y-H-0.3), (50, y-H-4.7),
            arrowstyle="-|>", mutation_scale=17, color="#8a9aab", lw=2.0))
    y -= (H + 3.6)

# 结论条
ax.add_patch(FancyBboxPatch((6, 3.0), 88, 8.0,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#f0f0f0", ec="#aaa", lw=1.5))
ax.text(50, 7.0, "整条链的每一环，都是同一个东西的不同表现：可压缩性",
        ha="center", va="center", fontsize=11.5, fontweight="bold", color="#333")

plt.tight_layout()
out = "/tmp/dig_deeper.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
