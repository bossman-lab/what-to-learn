# -*- coding: utf-8 -*-
"""受精卵体外培育：三段难度与那堵「输运墙」"""
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

fig, ax = plt.subplots(figsize=(16, 10), dpi=165)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

GREEN="#1e7a34"; RED="#c0392b"; GOLD="#c08a00"; BLUE="#1f4e79"

ax.text(50, 95.5, "受精卵体外培育：三段难度，一堵墙",
        ha="center", va="center", fontsize=21, fontweight="bold", color="#111")
ax.text(50, 91.5, "程序早就在基因组里了 —— 难点不是「造程序」，是「维持供给」",
        ha="center", va="center", fontsize=12, color="#666")

# 时间轴
ax.add_patch(FancyArrowPatch((5, 76), (95, 76), arrowstyle="-|>",
    mutation_scale=20, color="#999", lw=2.2))
for x, lab in [(14, "受精卵"), (34, "囊胚"), (56, "原肠胚"), (78, "器官发生")]:
    ax.plot([x, x], [74.4, 77.6], color="#999", lw=1.6)
    ax.text(x, 72.2, lab, ha="center", va="center", fontsize=10, color="#666")

# 三段
zones = [
    (6, 30, "早 期", "受精 → 14 天", GREEN, "#e8f5ea",
     "● 技术可行（限制在伦理）\nAI 已深度介入（见下）"),
    (38, 30, "中 期", "14 天 → 8 周", RED, "#fbeae8",
     "× 卡在这里\n器官发生需要【母体血液循环】"),
    (70, 24, "晚 期", "8 周 → 出生", GOLD, "#fdf6e3",
     "△ Biobag 有进展\n但那是【早产儿】，不是受精卵"),
]
for x, w, name, span, c, bg, note in zones:
    ax.add_patch(FancyBboxPatch((x, 46.0), w, 22.0,
        boxstyle="round,pad=0.5,rounding_size=1.2", fc=bg, ec=c, lw=2.0))
    ax.text(x+w/2, 64.0, name, ha="center", va="center", fontsize=15,
            fontweight="bold", color=c)
    ax.text(x+w/2, 60.3, span, ha="center", va="center", fontsize=9.6,
            color="#666", style="italic")
    ax.text(x+w/2, 52.5, note, ha="center", va="center", fontsize=9.6,
            color=c, linespacing=1.75)

# 输运墙
ax.plot([37.2, 37.2], [38.5, 70], color=RED, lw=3.4, ls=(0, (6, 4)), zorder=5)
ax.add_patch(FancyBboxPatch((21, 30.5), 32, 8.0,
    boxstyle="round,pad=0.4,rounding_size=1.0", fc=RED, ec="none", zorder=6))
ax.text(37, 34.5, "输 运 墙 ： 表面 / 体积比 → 扩散供不上", ha="center", va="center",
        fontsize=11.5, fontweight="bold", color="white", zorder=7)

# AI 发力点
ax.text(4, 25.0, "AI 的发力点（按成熟度）", ha="left", va="center",
        fontsize=12, fontweight="bold", color="#333")
tools = [
    ("★★★ 胚胎评估与选择", "已部署（如 Chloe EQ）——最能落地", GREEN),
    ("★★ 时差成像形态动力学", "从发育时序提取潜能特征", BLUE),
    ("★★ 微环境条件优化", "3D 仿生微环境 · 贝叶斯优化", GOLD),
    ("★★ 无创染色体筛查", "免活检，从培养液/图像预测倍性", "#6a3d9a"),
]
x = 4
for title, desc, c in tools:
    ax.add_patch(FancyBboxPatch((x, 10.0), 22.6, 11.5,
        boxstyle="round,pad=0.4,rounding_size=1.0", fc="#ffffff", ec=c, lw=1.7))
    ax.text(x+11.3, 18.2, title, ha="center", va="center", fontsize=10.2,
            fontweight="bold", color=c)
    ax.text(x+11.3, 13.6, desc, ha="center", va="center", fontsize=8.6,
            color="#555", linespacing=1.5)
    x += 23.4

# 底部
ax.add_patch(FancyBboxPatch((4, 2.0), 92, 6.2,
    boxstyle="round,pad=0.4,rounding_size=1.1", fc="#111827", ec="none"))
ax.text(50, 5.1, "AI 能优化「供给参数」和「选择判断」，但改不了「输运极限」",
        ha="center", va="center", fontsize=11.8, fontweight="bold", color="white")

plt.tight_layout()
out = "/tmp/ivf_limits.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
