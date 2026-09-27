# -*- coding: utf-8 -*-
"""为什么规律"明确"而发展"递进"：三道鸿沟 + 层叠结构"""
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

fig, ax = plt.subplots(figsize=(16, 10.5), dpi=170)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

DARK = "#111827"; PURPLE = "#6a3d9a"; BLUE = "#1f4e79"
GOLD = "#c08a00"; GREEN = "#1e7a34"

ax.text(50, 96.5, "为什么规律「明确」，发展却「递进」？",
        ha="center", va="center", fontsize=21, fontweight="bold", color="#111")

# ===== 上半：三道鸿沟 =====
ax.text(4, 89.5, "① 三道鸿沟：规律 → 技术之间", ha="left", va="center",
        fontsize=12.5, fontweight="bold", color="#333")

# 起点
ax.add_patch(FancyBboxPatch((4, 74), 20, 11,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc=DARK, ec="none"))
ax.text(14, 81.5, "宇宙规律", ha="center", va="center", fontsize=14,
        fontweight="bold", color="white")
ax.text(14, 77.3, "明确 · 可约 · 极少", ha="center", va="center",
        fontsize=8.6, color="#cbd5e1")

gaps = [
    ("认识鸿沟", "规律要【被发现】\n（本体确定 ≠ 已知）", BLUE),
    ("计算鸿沟", "后果要【被展开】\n（不可约 · 必须跑）", PURPLE),
    ("实现鸿沟", "方案要【被搜索】\n（好设计是找出来的）", GOLD),
]
x = 26
for name, desc, c in gaps:
    ax.add_patch(FancyBboxPatch((x, 72), 18, 15,
        boxstyle="round,pad=0.5,rounding_size=1.2", fc="#f4f4f5", ec=c, lw=1.8))
    ax.text(x+9, 83.0, name, ha="center", va="center", fontsize=12,
            fontweight="bold", color=c)
    ax.text(x+9, 76.8, desc, ha="center", va="center", fontsize=9.0,
            color="#444", linespacing=1.6)
    ax.add_patch(FancyArrowPatch((x-1.8, 79.5), (x-0.2, 79.5),
        arrowstyle="-|>", mutation_scale=13, color="#aaa", lw=1.6))
    x += 20

# 终点
ax.add_patch(FancyBboxPatch((86, 72), 12, 15,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#e8f5ea", ec=GREEN, lw=1.8))
ax.text(92, 79.5, "技术", ha="center", va="center", fontsize=13,
        fontweight="bold", color=GREEN)
ax.add_patch(FancyArrowPatch((84.2, 79.5), (85.8, 79.5),
    arrowstyle="-|>", mutation_scale=13, color="#aaa", lw=1.6))

ax.text(50, 67.0, "规律给你的是「约束」，不是「蓝图」——所以每一步都要自己找",
        ha="center", va="center", fontsize=11.5, style="italic", color="#666")

# ===== 下半：层叠结构 =====
ax.text(4, 61.5, "② 层叠依赖：每层只有下面做完，上面才可达", ha="left", va="center",
        fontsize=12.5, fontweight="bold", color="#333")

layers = [
    ("物理", "#e8f0fa", BLUE), ("材料", "#e8f0fa", BLUE),
    ("器件", "#e8f5ea", GREEN), ("电路", "#e8f5ea", GREEN),
    ("架构", "#fdf6e3", GOLD), ("系统软件", "#fdf6e3", GOLD),
    ("应用", "#f0e8f7", PURPLE), ("智能 / AI", "#fbeae8", "#c0392b"),
]
bw, bh, gap = 10.5, 15, 1.4
total = len(layers)*bw + (len(layers)-1)*gap
x0 = (100-total)/2
for i, (name, bg, c) in enumerate(layers):
    xx = x0 + i*(bw+gap)
    ax.add_patch(FancyBboxPatch((xx, 40), bw, bh,
        boxstyle="round,pad=0.3,rounding_size=1.0", fc=bg, ec=c, lw=1.6))
    ax.text(xx+bw/2, 47.5, name, ha="center", va="center", fontsize=10.5,
            fontweight="bold", color=c, rotation=90)
    if i < len(layers)-1:
        ax.add_patch(FancyArrowPatch((xx+bw+0.1, 47.5), (xx+bw+gap-0.1, 47.5),
            arrowstyle="-|>", mutation_scale=11, color="#bbb", lw=1.4))

ax.text(50, 35.0, "每一层都开启一个全新的「设计空间」——而空间只能逐层进入",
        ha="center", va="center", fontsize=11, color="#666")

# ===== 底部 =====
ax.add_patch(FancyBboxPatch((6, 6.0), 88, 24,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#111827", ec="none"))
ax.text(50, 25.5, "所以：规律「明确」不等于路径「明确」",
        ha="center", va="center", fontsize=14, fontweight="bold", color="white")
ax.text(50, 19.0,
        "图灵 1936 年就证明了「通用计算是可能的」——\n"
        "但要真正实现它，用了 80 多年，而且要一层一层地搭。",
        ha="center", va="center", fontsize=10.8, color="#cbd5e1", linespacing=1.7)
ax.text(50, 10.5,
        "这与「可约 / 不可约」是同一条定律：规律可约，但其展开不可约。",
        ha="center", va="center", fontsize=10.2, color="#94a3b8", style="italic")

plt.tight_layout()
out = "/tmp/why_incremental.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
