# -*- coding: utf-8 -*-
"""眼镜成熟后的生态重构"""
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

fig, ax = plt.subplots(figsize=(15.5, 11), dpi=170)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

RED="#c0392b"; RED_BG="#fbeae8"
GREEN="#1e7a34"; GREEN_BG="#e8f5ea"
BLUE="#1f4e79"; BLUE_BG="#e8f0fa"
PURPLE="#6a3d9a"; PURPLE_BG="#f0e8f7"

ax.text(50, 96.5, "眼镜突破之后：生态会怎样重构",
        ha="center", va="center", fontsize=21, fontweight="bold", color="#111")
ax.text(50, 92.3, "它一头吃掉屏幕，一头被人依附",
        ha="center", va="center", fontsize=12, color="#666")

# 中心：眼镜
ax.add_patch(FancyBboxPatch((38, 78), 24, 10,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc="#111827", ec="none"))
ax.text(50, 84.5, "眼 镜", ha="center", va="center", fontsize=16,
        fontweight="bold", color="white")
ax.text(50, 80.8, "虚拟屏幕 · 第一视角大脑入口", ha="center", va="center",
        fontsize=8.6, color="#cbd5e1")

# 四象限
quads = [
    (4,  47, 44, 29, "被 吃 掉", RED, RED_BG,
     "平板 · 折叠屏 · 电视/显示器\n相机 · 手机（部分场景）\n\n—— 屏幕被虚拟化"),
    (52, 47, 44, 29, "会 依 附", GREEN, GREEN_BG,
     "耳机（音频 I/O）\n手表（体征数据）\n键盘（高带宽输入）\n戒指/手环（手势）· 云端 VM"),
    (4,  13, 44, 29, "新 生 的", BLUE, BLUE_BG,
     "光学 / 波导供应商\n微显示（MicroLED/LCoS）\n低功耗 SoC\n眼镜专用 OS（Agent OS 首宿主）"),
    (52, 13, 44, 29, "不 变 的", PURPLE, PURPLE_BG,
     "主权：数据归属锚点\n问责：社会事实\n物理接触：贴皮肤 / 在耳边 / 握手里"),
]

for x, y, w, h, title, c, bg, body in quads:
    ax.add_patch(FancyArrowPatch((50, 78.5), (x+w/2, y+h+0.6),
        arrowstyle="-|>", mutation_scale=14, color=c, lw=1.6, alpha=0.55,
        connectionstyle="arc3,rad=0.08"))
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0.5,rounding_size=1.2", fc=bg, ec=c, lw=1.8))
    ax.text(x+w/2, y+h-3.5, title, ha="center", va="center", fontsize=14,
            fontweight="bold", color=c)
    ax.text(x+w/2, y+h/2-2.5, body, ha="center", va="center", fontsize=9.8,
            color="#444", linespacing=1.75)

plt.tight_layout()
out = "/tmp/glasses_ecosystem.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
