# -*- coding: utf-8 -*-
"""Build cases.json + README.md from scripts/cases_src.py"""
import json, datetime, os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from cases_src import C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = [
    ("motion", "🎬 动画短片 / 动效", "Animation & Motion"),
    ("3d", "🧊 3D / Three.js", "3D & Three.js"),
    ("game", "🎮 游戏", "Games"),
    ("edu", "📚 教育 / 历史", "Education & History"),
    ("compare", "⚖️ 对比评测", "Comparisons"),
    ("other", "🧩 其他（自测 / 宣传片 / 工具）", "Other"),
]
CHECKED = "2026-10-03 22:00 (UTC+8)"

def bj(ts):
    t = datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%MZ") + datetime.timedelta(hours=8)
    return t.strftime("%Y-%m-%d %H:%M")

cases = []
for (pid, h, cat, ts, likes, views, bm, tz, te, dz, prompt, play) in C:
    cases.append(dict(id=pid, category=cat, title_zh=tz, title_en=te, description_zh=dz,
        author=h, author_url=f"https://x.com/{h}", post_url=f"https://x.com/{h}/status/{pid}",
        posted_at_utc8=bj(ts), likes=likes, views=views, bookmarks=bm,
        prompt=prompt, play_url=play))
order = {c[0]: i for i, c in enumerate(CATS)}
cases.sort(key=lambda c: (order[c["category"]], -c["likes"], -c["views"]))

meta = dict(name="Awesome Fable 5.5", updated_at=CHECKED,
    note_zh="Fable 5.5 尚未官宣；模型归属以各作者自述为准。互动数为整理时数值。作品版权归原作者。",
    categories=[dict(id=a, zh=b, en=c) for a, b, c in CATS], cases=cases)
json.dump(meta, open(os.path.join(ROOT, "cases.json"), "w"), ensure_ascii=False, indent=1)

def fmt(n):
    return f"{n/10000:.1f} 万" if n >= 10000 else str(n)

PROMO = """> **Claude 国内使用方法**
> - 方法一：Claude 国内镜像站 👉 [https://claude-opus.top/](https://claude-opus.top/)
> - 方法二：tryallapi 一站式 API（Claude / GPT / Gemini）👉 [https://tryallapi.com/register?aff=5A6A](https://tryallapi.com/register?aff=5A6A)
"""

L = []
L.append("# Awesome Fable 5.5 · Claude Fable 5.5 自测方法与作品合集\n")
L.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Gallery](https://img.shields.io/badge/在线画廊-GitHub%20Pages-blue)](https://xianyu110.github.io/awesome-fable-5.5/)\n")
L.append(f"> 精选 X 上 **{len(cases)}** 个 Claude Fable 5.5（灰度版）实测作品与玩法：动画短片、3D、游戏、教育、对比评测。每条都有作者署名与原帖链接。")
L.append("> A curated, Chinese-first list of community-made works attributed to the unreleased **Claude Fable 5.5**, with credits and links to every original X post.\n")
L.append(PROMO)
L.append("🌐 **在线画廊（可按分类筛选）**：<https://xianyu110.github.io/awesome-fable-5.5/>\n")
L.append("## ⚠️ 先看这里\n")
L.append("- 截至 2026-10-03，Anthropic 官方最新的 Fable 仍是 **Claude Fable 5.1**（`claude-fable-5-1`）。**Fable 5.5 尚未官宣**。")
L.append("- 10 月 1 日起，部分 Claude 网页端 / Claude Code 用户在选择 Fable 5.1 时，被**静默路由（灰度）到一个新 checkpoint**，社区普遍认为就是 Fable 5.5。")
L.append("- 本仓库收录的作品，模型归属均以**作者自述**为准，未经独立复现。互动数据为整理时数值（" + CHECKED + "）。\n")
L.append("## 目录\n")
L.append("- [如何判断你是否用上了 Fable 5.5](#如何判断你是否用上了-fable-55)")
for cid, zh, en in CATS:
    n = sum(1 for c in cases if c["category"] == cid)
    anchor = zh.split(" ", 1)[1]
    slug = re.sub(r"[^\w\- ]", "", zh.lower()).replace(" ", "-")
    L.append(f"- [{zh}](#{slug})（{n}）")
L.append("- [玩法技巧](#玩法技巧)\n- [收录说明与版权](#收录说明与版权)\n")

L.append("## 如何判断你是否用上了 Fable 5.5\n")
L.append("社区称之为 **“Tibo 测试”**。原理：新模型的训练数据更新，认识 OpenAI Codex 团队的 Thibault Sottiaux（X 上“额度重置”梗的主角）；旧版 5.1 不认识，或会把他和别的 Tibo 混淆。\n")
L.append("1. 在 Claude 网页端或 Claude Code 里选择 **Fable 5.1**（需要 Pro / Max / Team / Enterprise）。")
L.append("2. **关闭联网搜索**，发送下面任意一句：\n")
L.append("```text\ndo you know tibo the reset guy? don't search\n```\n")
L.append("```text\nDo not use web search or any tools. Who is Tibo the reset guy\n```\n")
L.append("3. 判读结果：")
L.append("   - ✅ 答出 **OpenAI Codex 的 Thibault Sottiaux**、提到“额度重置” → 大概率已被路由到 Fable 5.5；")
L.append("   - ❌ 只说是 Tweet Hunter 的 Tibo，或“重启职业生涯的法国独立开发者” → 仍是旧模型。")
L.append("4. 灰度是**按账号、时有时无**的，今天没有不代表明天没有；同一账号也可能中途停掉。\n")
L.append("测试方法来源：[@notjazii](https://x.com/notjazii/status/2105718628717056061) · 中文版实测：[@Saccc_c](https://x.com/Saccc_c/status/2105913312072577218) · 判读说明：[@NFT_Chen](https://x.com/NFT_Chen/status/2105753129807761712)\n")

for cid, zh, en in CATS:
    L.append(f"## {zh}\n")
    L.append(f"*{en}* · 按点赞数排序\n")
    i = 0
    for c in cases:
        if c["category"] != cid: continue
        i += 1
        L.append(f"### {i}. {c['title_zh']}\n")
        meta_line = f"[@{c['author']}]({c['author_url']}) · {c['posted_at_utc8']} (UTC+8) · ❤️ {fmt(c['likes'])} · 👀 {fmt(c['views'])} · [原帖]({c['post_url']})"
        if c["play_url"]:
            meta_line += f" · [▶ 试玩 / 打开]({c['play_url']})"
        L.append(meta_line + "\n")
        L.append(f"*{c['title_en']}* — {c['description_zh']}\n")
        if c["prompt"]:
            L.append(f"> 提示词（来自作者公开内容）：`{c['prompt']}`\n")

L.append("""## 玩法技巧

1. **极简提示词反而出彩**：Fable 5.5 自带很强的“导演感”，一句 `please make a cool animation` 就能出完整短片，先别急着写长提示词。
2. **两步法**：先让它做 3D 场景 / 交互页面，再让它“输出一段 1 分钟视频”（见鲁布·戈德堡机械案例）。
3. **开放式提问测审美**：`If I asked you to blow my mind, what would you make?` 这类问题最能看出模型的创意上限。
4. **给参考素材**：上传参考视频、歌曲和歌词，让它做“发布片”或“歌词 MV”，效果明显更稳。
5. **用倒计时逼它打磨**：在 Claude Code 里让它起一个 10 分钟计时任务，要求“用满时间再交付”（见 3D 手柄案例）。
6. **老提示词重跑 = 最简单的新旧对比**：把你在 5.1 / Opus 上用过的提示词原样再跑一次，差距一目了然。
7. **SVG / 单 HTML 是低成本试水方式**：Switch SVG 动画约 $1.34、鹈鹕 SVG 约 $2.61（API、High 强度）。
8. **注意额度**：有作者实测一次约 30 分钟的视频测试就用掉 Pro x5 档约 7% 周额度；Max 强度的长任务可能跑 2 个多小时。重活先用 Opus 5.5 / Sonnet 5.5 打草稿，再交给 Fable 精修。
9. **理性看待**：也有作者认为 Opus 5.5 在部分题目上不输 Fable 5.5，对比时尽量同提示、同强度。
""")
L.append("## 收录说明与版权\n")
L.append("- 收录标准：作者明确表示由 Fable 5.5（灰度版）制作的公开作品 / 测试 / 方法帖；去重；同类只保留代表作。")
L.append("- 本仓库中的中文标题与简介为本仓库原创撰写；**所有作品、视频、代码与提示词的版权归原作者所有**，引用的提示词均为作者公开内容并注明出处。")
L.append("- 如果你是作者并希望修改或移除条目，请提交 Issue。欢迎 PR 补充新案例（需附原帖链接）。")
L.append("- 本仓库的代码（`index.html`、`scripts/`）采用 [MIT License](LICENSE)。本项目与 Anthropic 无关，非官方。\n")
L.append(PROMO)
L.append("---\n\n我是 **MaynorAI 团队**，分享 AI 编程、AI SaaS 工具出海、一人团队搭建经验。\n")
open(os.path.join(ROOT, "README.md"), "w").write("\n".join(L))
print("cases", len(cases))
