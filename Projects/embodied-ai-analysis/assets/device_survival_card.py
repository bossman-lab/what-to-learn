# -*- coding: utf-8 -*-
"""速查卡：这个设备能活下来吗？"""
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

RED = "#c0392b"; RED_BG = "#fbeae8"
GREEN = "#1e7a34"; GREEN_BG = "#e8f5ea"

# 卡头
ax.add_patch(FancyBboxPatch((4, 88.5), 92, 9.5,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc="#111827", ec="none"))
ax.text(50, 94.2, "速查卡", ha="center", va="center", fontsize=21,
        fontweight="bold", color="white")
ax.text(50, 90.4, "这个设备能活下来吗？", ha="center", va="center",
        fontsize=13, color="#cbd5e1")

# 核心问题
ax.text(50, 83.5, "第一问", ha="center", va="center", fontsize=12, color="#888")
ax.add_patch(FancyBboxPatch((14, 74.5), 72, 7.6,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc="#fffbe6", ec="#e0c86a", lw=1.8))
ax.text(50, 78.3, "它是【一个尺寸】还是【一个用途】？", ha="center", va="center",
        fontsize=16, fontweight="bold", color="#7a5a00")

# 分叉
ax.add_patch(FancyArrowPatch((36, 74.2), (27, 69.0), arrowstyle="-|>",
    mutation_scale=18, color=RED, lw=2.2))
ax.add_patch(FancyArrowPatch((64, 74.2), (73, 69.0), arrowstyle="-|>",
    mutation_scale=18, color=GREEN, lw=2.2))

# 左：形态定义
ax.add_patch(FancyBboxPatch((4, 27), 44, 41,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc=RED_BG, ec=RED, lw=2.2))
ax.text(26, 64.0, "一个尺寸 / 形状", ha="center", va="center", fontsize=14,
        fontweight="bold", color=RED)
ax.text(26, 59.5, "会被吃掉", ha="center", va="center", fontsize=13,
        fontweight="bold", color="#a02020")
ax.plot([10, 42], [56.6, 56.6], color=RED, lw=1.0, alpha=0.4)
ax.text(26, 50.0, "例：", ha="center", va="center", fontsize=10.5, color="#a06058")
ax.text(26, 42.0, "平板（更大的屏幕）\n折叠屏（能折的屏幕）\n笔记本屏",
        ha="center", va="center", fontsize=11, color=RED, linespacing=1.7)
ax.text(26, 30.5, "→ 被下一代形态吃掉", ha="center", va="center",
        fontsize=10.5, fontweight="bold", color="#a02020")

# 右：功能定义
ax.add_patch(FancyBboxPatch((52, 27), 44, 41,
    boxstyle="round,pad=0.6,rounding_size=1.5", fc=GREEN_BG, ec=GREEN, lw=2.2))
ax.text(74, 64.0, "一个用途", ha="center", va="center", fontsize=14,
        fontweight="bold", color=GREEN)
ax.text(74, 59.5, "能活 —— 再问第二问", ha="center", va="center", fontsize=11,
        fontweight="bold", color="#1e7a34")
ax.plot([58, 90], [56.6, 56.6], color=GREEN, lw=1.0, alpha=0.4)
ax.text(74, 52.5, "它依赖什么？", ha="center", va="center",
        fontsize=11, fontweight="bold", color=GREEN)
ax.text(74, 43.5, "① 物理接触 → 更稳\n　 （手表/耳机/键盘）\n② 社会事实 → 更稳\n　 （数据主权/问责）",
        ha="center", va="center", fontsize=10.2, color="#3a7a52", linespacing=1.6)
ax.text(74, 30.5, "③ 只是“看” → 最易被虚拟化", ha="center", va="center",
        fontsize=10.2, color="#a06a1a")

# 底部
ax.add_patch(FancyBboxPatch((6, 12.5), 88, 10,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#f0f0f0", ec="#aaa", lw=1.5))
ax.text(50, 19.6, "最后活下来的（当前推演）", ha="center", va="center",
        fontsize=10.5, color="#888")
ax.text(50, 15.4, "眼镜 · 手表 · 耳机 · 键盘 · 主权锚点",
        ha="center", va="center", fontsize=13, fontweight="bold", color="#333")

# 页脚
ax.text(50, 7.0, "形态 = 可约（会被替代）　·　功能 = 不可约（物理 / 社会锚定）",
        ha="center", va="center", fontsize=11, style="italic", color="#666")

plt.tight_layout()
out = "/tmp/device_survival_card.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
