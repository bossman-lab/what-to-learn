# -*- coding: utf-8 -*-
"""剪刀差结构图：模型能力商品化 vs 互补资产寡头化"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
font_manager.fontManager.addfont(FONT)
font_manager.fontManager.addfont(FONT_B)
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "Noto Sans CJK JP"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(14, 8.5), dpi=170)
fig.patch.set_facecolor("#fbfbfb")

x = np.array([2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028])
# 模型能力单位价值：持续下降（商品化）
model = np.array([95, 88, 80, 68, 55, 42, 30, 20, 12])
# 互补资产壁垒：持续上升（寡头化）
asset = np.array([15, 22, 30, 42, 55, 70, 85, 97, 108])

ax.fill_between(x, model, asset, where=(asset >= model),
                color="#f4e8dd", alpha=0.55, label="结构性张力（剪刀差）")

ax.plot(x, model, color="#1f4e79", lw=3.2, marker="o", ms=7,
        label="模型能力 · 单位价值  ↘ 持续商品化")
ax.plot(x, asset, color="#8a3b12", lw=3.2, marker="s", ms=7,
        label="互补资产 · 进入壁垒  ↗ 持续寡头化")

# 标注
ax.annotate("开源冲击\nLlama / Mistral", xy=(2023, 42), xytext=(2022.1, 12),
            fontsize=10, color="#555", ha="center",
            arrowprops=dict(arrowstyle="->", color="#999", lw=1.2))
ax.annotate("DeepSeek R1\n算力垄断被重估", xy=(2025, 42), xytext=(2024.3, 6),
            fontsize=10, color="#555", ha="center",
            arrowprops=dict(arrowstyle="->", color="#999", lw=1.2))
ax.annotate("capex 军备竞赛\n$6000亿级", xy=(2026, 85), xytext=(2026.9, 74),
            fontsize=10, color="#8a3b12", ha="center",
            arrowprops=dict(arrowstyle="->", color="#c99", lw=1.2))
ax.annotate("三天三连发\nDS / GLM / Qwen", xy=(2026, 30), xytext=(2027.0, 34),
            fontsize=10, color="#1f4e79", ha="center",
            arrowprops=dict(arrowstyle="->", color="#88a", lw=1.2))

# 剪刀差标注
ax.annotate("", xy=(2028, 108), xytext=(2028, 12),
            arrowprops=dict(arrowstyle="<->", color="#c0392b", lw=2.2))
ax.text(2028.15, 60, "剪 刀 差", fontsize=13, fontweight="bold",
        color="#c0392b", rotation=90, va="center")

ax.set_title("剪刀差结构：模型持续商品化，互补资产持续寡头化",
             fontsize=17, fontweight="bold", pad=18, color="#111")
ax.set_xlabel("时间", fontsize=12, color="#555")
ax.set_ylabel("相对水平（示意）", fontsize=12, color="#555")
ax.set_xticks(x); ax.set_xticklabels([str(v) for v in x], fontsize=10.5)
ax.set_ylim(-2, 120)
ax.legend(loc="center left", fontsize=11.5, framealpha=0.95)
ax.grid(alpha=0.18, ls="--")
for s in ("top", "right"): ax.spines[s].set_visible(False)

ax.text(0.5, -0.135,
        "站在「互补资产」这一侧：数据 · 验证 · 供应链 · 分发 —— 不要站在「模型」这一侧",
        transform=ax.transAxes, ha="center", fontsize=11.5, style="italic", color="#666")

plt.tight_layout()
out = "/tmp/scissors_diagram.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
