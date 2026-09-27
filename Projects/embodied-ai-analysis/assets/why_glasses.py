# -*- coding: utf-8 -*-
"""为什么突破口在眼镜：三判据交叉检验"""
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

fig, ax = plt.subplots(figsize=(15.5, 10), dpi=170)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

GOOD, MID, BAD = "#1e7a34", "#c08a00", "#c0392b"
G = "●"; M = "◐"; X = "○"

ax.text(50, 96.0, "为什么突破口在眼镜？", ha="center", va="center",
        fontsize=22, fontweight="bold", color="#111")
ax.text(50, 91.5, "三个判据的交叉检验：能活 · 可原生 · 能当主入口",
        ha="center", va="center", fontsize=12, color="#666")

# 列定义
cols = [("设备", 12), ("① 功能定义\n（能活）", 40),
        ("② 无在位 OS\n（可原生）", 58), ("③ 高带宽 + 富上下文\n（能当主入口）", 76),
        ("合 计", 92)]

# 表头
for name, x in cols:
    ax.text(x, 84.5, name, ha="center", va="center", fontsize=10.5,
            fontweight="bold", color="#444", linespacing=1.4)

ax.plot([4, 96], [80.5, 80.5], color="#999", lw=1.6)

rows = [
    ("眼镜",  (G, GOOD), (G, GOOD), (G, GOOD), "3 / 3", "#e8f5ea", GOOD),
    ("耳机",  (G, GOOD), (M, MID),  (M, MID),  "2 / 3", "#fdf8e8", "#8a7a1a"),
    ("PC",   (G, GOOD), (X, BAD),  (G, GOOD), "2 / 3", "#fdf8e8", "#8a7a1a"),
    ("手机",  (M, MID),  (X, BAD),  (G, GOOD), "1.5 / 3", "#f8f8f8", "#666"),
    ("手表",  (G, GOOD), (M, MID),  (X, BAD),  "1.5 / 3", "#f8f8f8", "#666"),
    ("Charm", (X, BAD),  (G, GOOD), (X, BAD),  "1 / 3", "#f8f8f8", "#666"),
]

y = 73.5
for name, c1, c2, c3, total, bg, tc in rows:
    ax.add_patch(FancyBboxPatch((4, y-4.4), 92, 8.8,
        boxstyle="round,pad=0.3,rounding_size=1.0", fc=bg, ec="#ddd", lw=1.2))
    ax.text(12, y, name, ha="center", va="center", fontsize=12.5,
            fontweight="bold", color="#222")
    for (sym, c), x in [(c1, 40), (c2, 58), (c3, 76)]:
        ax.text(x, y, sym, ha="center", va="center", fontsize=15, color=c)
    ax.text(92, y, total, ha="center", va="center", fontsize=12.5,
            fontweight="bold", color=tc)
    y -= 10.0

# 底部结论
ax.add_patch(FancyBboxPatch((6, 6.2), 88, 11.0,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#111827", ec="none"))
ax.text(50, 13.9, "眼镜是唯一同时满足三条的设备",
        ha="center", va="center", fontsize=13.5, fontweight="bold", color="white")
ax.text(50, 10.1, "它在【能活的一侧】，又【没有在位者】——且它本身就是要吃掉“屏幕”的那个形态",
        ha="center", va="center", fontsize=10.2, color="#cbd5e1")

ax.text(50, 3.2, "● 满足　◐ 部分满足　○ 不满足",
        ha="center", va="center", fontsize=9.5, color="#888")

plt.tight_layout()
out = "/tmp/why_glasses.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
