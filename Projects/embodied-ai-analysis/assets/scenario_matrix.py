# -*- coding: utf-8 -*-
"""场景放置矩阵：哪些在端，哪些在云（修正版）"""
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

fig, ax = plt.subplots(figsize=(15.5, 11.5), dpi=170)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
fig.patch.set_facecolor("#fbfbfb")

GREEN = "#1e7a34"; GREEN_BG = "#e8f5ea"
GRAY  = "#7a6a1a"; GRAY_BG  = "#fdf6e3"
BLUE  = "#1f4e79"; BLUE_BG  = "#e8f0fa"

XC = [24, 51.5, 79]      # 三列中心
CW = 25                   # 列宽
LABEL_X = 5               # 左侧功能域标签

ax.text(50, 96.8, "场景放置矩阵：哪些在端，哪些在云",
        ha="center", va="center", fontsize=22, fontweight="bold", color="#111")
ax.text(50, 92.8, "端做「快、私、常」的活　·　云做「重、久、险」的活",
        ha="center", va="center", fontsize=12, color="#666")

# 列标题
for x, name, sub, c in [(XC[0], "端  侧", "端侧小模型 · 实时 · 隐私", GREEN),
                        (XC[1], "混  合", "端优先 + 云兜底（级联）", GRAY),
                        (XC[2], "云  侧", "大模型 · 持久 · 隔离", BLUE)]:
    ax.add_patch(FancyBboxPatch((x-CW/2, 84.5), CW, 6.4,
        boxstyle="round,pad=0.4,rounding_size=1.2", fc=c, ec="none"))
    ax.text(x, 87.9, name, ha="center", va="center", fontsize=15,
            fontweight="bold", color="white")
    ax.text(x, 85.6, sub, ha="center", va="center", fontsize=8.4, color="white")

data = [
    (79.0, "感  知", ["唤醒词检测", "基础视觉/人脸", "生物识别", "传感器采集"],
        ["复杂视觉理解"], ["多模态深度理解"]),
    (66.0, "交  互", ["UI 响应 / 动画", "语音转文字", "意图识别"],
        ["实时翻译", "语音草稿"], ["复杂意图澄清"]),
    (53.0, "信  息", ["本地查询（时间/天气）", "缓存类回答"],
        ["一般问答", "图片理解"], ["深度研究", "多源综合"]),
    (40.0, "通  讯", ["通知接收", "通话"],
        ["消息起草 / 润色"], ["代发邮件/消息", "跨服务沟通"]),
    (27.0, "执  行", ["单步设备操作", "闹钟 / 提醒"],
        ["多步任务（端起步）", "跨设备协同"], ["浏览器操作", "后台监控/等待", "长任务"]),
    (15.5, "交易/健康", ["家居 / 车机控制", "心率/睡眠采集"],
        ["比价选方案"], ["下单 / 支付", "长期健康分析", "医疗建议"]),
]

BH = 10.6
for y, domain, left, mid, right in data:
    # 左侧功能域标签（旋转）
    ax.text(LABEL_X, y, domain, ha="center", va="center", fontsize=11,
            fontweight="bold", color="#555", rotation=90)
    for x, items, c, bg in [(XC[0], left, GREEN, GREEN_BG),
                            (XC[1], mid, GRAY, GRAY_BG),
                            (XC[2], right, BLUE, BLUE_BG)]:
        ax.add_patch(FancyBboxPatch((x-CW/2, y-BH/2), CW, BH,
            boxstyle="round,pad=0.4,rounding_size=1.0", fc=bg, ec=c, lw=1.4))
        n = len(items)
        step = 2.7
        y0 = y + (n-1)*step/2
        for i, it in enumerate(items):
            ax.text(x, y0-i*step, it, ha="center", va="center",
                    fontsize=9.3, color=c)

# 底部
ax.add_patch(FancyBboxPatch((6, 0.6), 88, 6.8,
    boxstyle="round,pad=0.4,rounding_size=1.2", fc="#111827", ec="none"))
ax.text(50, 5.2, "唯一指标：端侧命中率", ha="center", va="center",
        fontsize=11, color="#cbd5e1")
ax.text(50, 2.5, "能不上云就不上云（快·私·省）　|　必须要上云才上云（重·久·险）",
        ha="center", va="center", fontsize=11.5, fontweight="bold", color="white")

plt.tight_layout()
out = "/tmp/scenario_matrix.png"
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print("saved:", out)
