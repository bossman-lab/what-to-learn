# -*- coding: utf-8 -*-
"""谁能活下来：以「形态」定义 vs 以「功能」定义"""
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

fig, ax = plt.subplots(figsize=(15.5, 10), dpi=170)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

RED = "#c0392b"; RED_BG = "#fbeae8"
GREEN = "#1e7a34"; GREEN_BG = "#e8f5ea"

ax.text(50, 96.5, "谁能活下来？——以「形态」定义 vs 以「功能」定义",
        ha="center", va="center", fontsize=20, fontweight="bold", color="#111")
ax.text(50, 92.0, "以形态定义的设备，会被下一代形态创新吃掉；以功能定义的设备能存活",
        ha="center", va="center", fontsize=11.5, color="#666")

# 左：形态定义（脆弱）
ax.add_patch(FancyBboxPatch((4, 20), 44, 66,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc="#fff5f4", ec=RED, lw=2))
ax.text(26, 82.0, "以「形态」定义 —— 脆弱", ha="center", va="center",
        fontsize=14, fontweight="bold", color=RED)
ax.text(26, 78.0, "定义 = 某个体积 / 形状的屏幕", ha="center", va="center",
        fontsize=9.5, color="#a06058", style="italic")

left_items = [
    (73.0, "平板", "“更大的屏幕”", "被折叠屏从下吃\n被二合一从上吃", "danger"),
    (50.0, "折叠屏", "“能折叠的屏幕”", "吃掉平板——但自己\n也可能被 AR 吃掉", "warn"),
]
for y, name, define, fate, kind in left_items:
    c = RED
    ax.add_patch(FancyBboxPatch((7, y-8.5), 38, 17,
        boxstyle="round,pad=0.5,rounding_size=1.2", fc=RED_BG, ec=c, lw=1.7))
    ax.text(10, y+5.0, name, ha="left", va="center", fontsize=14,
            fontweight="bold", color=c)
    ax.text(10, y+1.4, define, ha="left", va="center", fontsize=9.5, color="#666")
    ax.text(10, y-3.2, fate, ha="left", va="center", fontsize=9.2,
            color=c, linespacing=1.5)

# 右：功能定义（稳固）
ax.add_patch(FancyBboxPatch((52, 20), 44, 66,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc="#f4fbf5", ec=GREEN, lw=2))
ax.text(74, 82.0, "以「功能」定义 —— 稳固", ha="center", va="center",
        fontsize=14, fontweight="bold", color=GREEN)
ax.text(74, 78.0, "定义 = 不可替代的用途", ha="center", va="center",
        fontsize=9.5, color="#4a8a5c", style="italic")

right_items = [
    (68.0, "手机",  "随身个人终端"),
    (58.0, "PC",   "高带宽创作 + 数据主权"),
    (48.0, "眼镜",  "第一视角感知"),
    (38.0, "耳机",  "语音交互"),
    (28.0, "手表",  "身体信号采集"),
]
for y, name, define in right_items:
    ax.add_patch(FancyBboxPatch((55, y-3.7), 38, 7.6,
        boxstyle="round,pad=0.4,rounding_size=1.0", fc=GREEN_BG, ec=GREEN, lw=1.5))
    ax.text(58, y, name, ha="left", va="center", fontsize=12,
            fontweight="bold", color=GREEN)
    ax.text(96, y, define, ha="right", va="center", fontsize=9.8, color="#444")

# 吃掉箭头
ax.add_patch(FancyArrowPatch((26, 58.7), (26, 64.3),
    arrowstyle="-|>", mutation_scale=17, color="#c0392b", lw=2.2))

# 底部结论
ax.add_patch(FancyBboxPatch((6, 5.0), 88, 11,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#111827", ec="none"))
ax.text(50, 12.6, "规律：形态 = 可约（会被替代）　·　功能 = 不可约（物理 / 社会锚定）",
        ha="center", va="center", fontsize=12, fontweight="bold", color="white")
ax.text(50, 8.2, "平板只是“某个体积的屏幕”——所以它注定被下一个形态吃掉",
        ha="center", va="center", fontsize=10.2, color="#cbd5e1")

plt.tight_layout()
out = "/tmp/form_vs_function.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
