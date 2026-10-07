# -*- coding: utf-8 -*-
"""自组织：AI 能发力的环节与不能发力的红线"""
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

fig, ax = plt.subplots(figsize=(16.5, 11), dpi=160)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

BLUE="#1f4e79"; GREEN="#1e7a34"; GOLD="#c08a00"; PURPLE="#6a3d9a"; RED="#c0392b"

ax.text(50, 96.5, "自组织：AI 的发力点在哪里",
        ha="center", va="center", fontsize=21, fontweight="bold", color="#111")
ax.text(50, 92.6, "AI 不能「制造」自组织，但能「找到让它发生的条件」",
        ha="center", va="center", fontsize=12, color="#666")

stages = [
    ("细胞群",   "分割 · 追踪 · 三维重建",     BLUE),
    ("命运决定", "细胞基础模型 · 扰动预测",     PURPLE),
    ("空间图案", "梯度建模 · 条件搜索 ★",       GOLD),
    ("形态发生", "代理模拟 · 力学建模",         GREEN),
    ("器官形成", "多尺度融合 · 轨迹预测",       "#0e7490"),
]

# 流程条
N = len(stages)
W, GAP = 16.4, 2.2
total = N*W + (N-1)*GAP
x0 = (100-total)/2
y_top = 78
for i, (name, tools, c) in enumerate(stages):
    x = x0 + i*(W+GAP)
    ax.add_patch(FancyBboxPatch((x, y_top), W, 8.2,
        boxstyle="round,pad=0.4,rounding_size=1.0", fc=c, ec="none"))
    ax.text(x+W/2, y_top+4.1, name, ha="center", va="center",
            fontsize=13, fontweight="bold", color="white")
    if i < N-1:
        ax.add_patch(FancyArrowPatch((x+W+0.15, y_top+4.1), (x+W+GAP-0.15, y_top+4.1),
            arrowstyle="-|>", mutation_scale=13, color="#9aa8b6", lw=1.8))
    # AI 手段
    ax.add_patch(FancyBboxPatch((x, y_top-11.5), W, 9.6,
        boxstyle="round,pad=0.4,rounding_size=1.0", fc="#ffffff", ec=c, lw=1.7))
    ax.text(x+W/2, y_top-6.7, tools, ha="center", va="center",
            fontsize=9.0, color=c, linespacing=1.5)
    ax.add_patch(FancyArrowPatch((x+W/2, y_top-0.25), (x+W/2, y_top-1.7),
        arrowstyle="-|>", mutation_scale=11, color=c, lw=1.5))

ax.text(x0, 88.6, "自组织的五个环节", ha="left", va="center",
        fontsize=11, fontweight="bold", color="#444")
ax.text(x0, 63.6, "AI 可介入的手段", ha="left", va="center",
        fontsize=11, fontweight="bold", color="#444")

# 红线区
ax.add_patch(FancyBboxPatch((6, 43.5), 88, 13,
    boxstyle="round,pad=0.5,rounding_size=1.2", fc="#fbeae8", ec=RED, lw=2.2))
ax.text(50, 52.4, "红 线 ： 自 组 织 的 执 行 本 身",
        ha="center", va="center", fontsize=14, fontweight="bold", color=RED)
ax.text(50, 47.4, "细胞必须自己「跑一遍」—— 形态发生是物理过程，不是信息过程\n"
                  "AI 可以优化条件、预测走向，但不能代替这一步",
        ha="center", va="center", fontsize=10.4, color="#8a3a30", linespacing=1.7)

# 三个最高杠杆
ax.text(6, 36.6, "三个最高杠杆点", ha="left", va="center",
        fontsize=12, fontweight="bold", color="#333")
levers = [
    ("① 培养条件优化", "因子 × 浓度 × 时序 × 几何 = 高维搜索\n主动学习 / 贝叶斯优化 —— AI 最擅长的形态", GOLD),
    ("② 扰动响应预测", "「敲掉基因 X 会怎样？」先在硅上试\n虚拟细胞 —— 大幅减少湿实验次数", PURPLE),
    ("③ 代理模型加速", "形态发生模拟很慢，ML 代理让它接近实时\n让「跑一遍」变得可交互", GREEN),
]
x = 6
for title, desc, c in levers:
    ax.add_patch(FancyBboxPatch((x, 12.0), 28.6, 22.0,
        boxstyle="round,pad=0.45,rounding_size=1.1", fc="#ffffff", ec=c, lw=1.9))
    ax.text(x+14.3, 30.2, title, ha="center", va="center", fontsize=12,
            fontweight="bold", color=c)
    ax.text(x+14.3, 21.2, desc, ha="center", va="center", fontsize=9.0,
            color="#555", linespacing=1.8)
    x += 30.0

# 底部
ax.add_patch(FancyBboxPatch((6, 2.5), 88, 7.5,
    boxstyle="round,pad=0.45,rounding_size=1.1", fc="#111827", ec="none"))
ax.text(50, 6.2, "AI 的真实价值：把「设计—构建—测试—学习」的循环周期缩短",
        ha="center", va="center", fontsize=11.5, fontweight="bold", color="white")

plt.tight_layout()
out = "/tmp/selforg_ai.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
