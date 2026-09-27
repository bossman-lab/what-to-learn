# -*- coding: utf-8 -*-
"""工具化先行：历史证据与例外规律"""
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

fig, ax = plt.subplots(figsize=(16, 11), dpi=165)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

BROWN="#92400e"; GOLD="#c08a00"; GREEN="#1e7a34"; BLUE="#1f4e79"; RED="#c0392b"

ax.text(50, 96.5, "常态：规律被「用起来」远早于被「算出来」",
        ha="center", va="center", fontsize=20, fontweight="bold", color="#111")
ax.text(50, 92.5, "工具化先行 —— 工程常常领先于科学",
        ha="center", va="center", fontsize=12, color="#888")

# 图例
ax.add_patch(FancyBboxPatch((22, 86.5), 4, 2.6, boxstyle="round,pad=0.2,rounding_size=0.6", fc=BROWN, ec="none"))
ax.text(27.5, 87.8, "工具化（物理/工业）", ha="left", va="center", fontsize=10, color="#333")
ax.add_patch(FancyBboxPatch((52, 86.5), 4, 2.6, boxstyle="round,pad=0.2,rounding_size=0.6", fc=GOLD, ec="none"))
ax.text(57.5, 87.8, "理论形式化", ha="left", va="center", fontsize=10, color="#333")
ax.add_patch(FancyBboxPatch((72, 86.5), 4, 2.6, boxstyle="round,pad=0.2,rounding_size=0.6", fc=GREEN, ec="none"))
ax.text(77.5, 87.8, "计算抽象", ha="left", va="center", fontsize=10, color="#333")

# 左侧：常态（工具→理论→计算）
rows = [
    ("力学",     "远古·杠杆齿轮", "1687·牛顿",    "1950s·数值模拟"),
    ("热学",     "1712·蒸汽机",   "1824·卡诺",    "1960s·热仿真"),
    ("电磁",     "1830s·电报",    "1865·麦克斯韦", "1970s·电磁仿真"),
    ("流体",     "古代·泵/风车",  "1738·伯努利",  "1960s·CFD"),
    ("空气动力", "1903·首次飞行", "1920s·升力理论","1960s·CFD"),
    ("遗传",     "数千年·育种",   "1865·孟德尔",  "1990s·基因组计算"),
]
ax.text(4, 81.0, "常 态", ha="left", va="center", fontsize=13, fontweight="bold", color=BROWN)
y = 74.5
for name, tool, theory, comp in rows:
    ax.text(4, y, name, ha="left", va="center", fontsize=11.5, fontweight="bold", color="#222")
    x = 22
    for label, c in [(tool, BROWN), (theory, GOLD), (comp, GREEN)]:
        ax.add_patch(FancyBboxPatch((x, y-1.7), 20, 3.4,
            boxstyle="round,pad=0.25,rounding_size=0.8", fc=c, ec="none"))
        ax.text(x+10, y, label, ha="center", va="center", fontsize=8.6, color="white")
        x += 21.5
    y -= 6.3

# 右侧：例外（理论→工具）
ax.text(4, 33.5, "例 外", ha="left", va="center", fontsize=13, fontweight="bold", color=BLUE)
ax.text(11, 33.5, "（理论先行：当「能懂」比「能做」容易）", ha="left", va="center", fontsize=10, color="#888")

exc = [
    ("相对论 / 核能", "1905·理论", "1945·核能装置"),
    ("激光",          "1917·受激辐射", "1960·激光器"),
    ("通用计算",      "1936·图灵机", "1947·晶体管"),
]
y = 27.5
for name, t1, t2 in exc:
    ax.text(4, y, name, ha="left", va="center", fontsize=11, fontweight="bold", color="#222")
    ax.add_patch(FancyBboxPatch((30, y-1.7), 22, 3.4,
        boxstyle="round,pad=0.25,rounding_size=0.8", fc=GOLD, ec="none"))
    ax.text(41, y, t1, ha="center", va="center", fontsize=8.6, color="white")
    ax.text(53.5, y, "→", ha="center", va="center", fontsize=12, color="#999")
    ax.add_patch(FancyBboxPatch((56, y-1.7), 22, 3.4,
        boxstyle="round,pad=0.25,rounding_size=0.8", fc=BROWN, ec="none"))
    ax.text(67, y, t2, ha="center", va="center", fontsize=8.6, color="white")
    y -= 6.0

# 底部规则
ax.add_patch(FancyBboxPatch((5, 2.5), 90, 8.5,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#111827", ec="none"))
ax.text(50, 8.6, "决定次序的规则：哪条路更便宜，就走哪条",
        ha="center", va="center", fontsize=12.5, fontweight="bold", color="white")
ax.text(50, 4.6, "「能做」比「能懂」容易 → 工具先行（且工具产出数据，是抽象的原料）",
        ha="center", va="center", fontsize=9.4, color="#cbd5e1")

plt.tight_layout()
out = "/tmp/tool_first.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
