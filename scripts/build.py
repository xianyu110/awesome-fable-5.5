# -*- coding: utf-8 -*-
"""Build cases.json + README.md + README.en.md from scripts/cases_src.py"""
import json, datetime, os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cases_src import C

ROOT = os.path.dirname(HERE)
GALLERY = "https://xianyu110.github.io/awesome-fable-5.5/"
CATS = [
    ("motion", "动画短片 / 动效", "Animation & Motion", "🎬"),
    ("3d", "3D / Three.js", "3D & Three.js", "🧊"),
    ("game", "游戏", "Games", "🎮"),
    ("edu", "教育 / 历史", "Education & History", "📚"),
    ("compare", "对比评测", "Comparisons", "⚖️"),
    ("other", "其他（自测 / 宣传片 / 工具）", "Other (self-check, promos, tools)", "🧩"),
]
MODEL = {
    "2105771088374288692": "Fable 5.5 vs Opus 5.5", "2106073473361543348": "Fable 5.5 vs Opus 5.5",
    "2105955048018588084": "Fable 5.5 vs Opus 5.5", "2105783511433318451": "Fable 5.5 vs GPT-6.1",
    "2106323394350461031": "Fable 5.5 vs 5.1", "2106081118869156150": "Fable 5.5（固件 Opus 5.5）",
    "2107803303832936679": "Fable 5.5 + Opus 5.5",
}
FEATURED = ["2105825930799432073", "2106081142143168580", "2105757136219504862", "2106095190285144331",
            "2106045364868419727", "2105884276864782557", "2105889407056109991", "2106112279079199037"]
CHECKED = "2026-10-09 11:47 (UTC+8)"
covers = json.load(open(os.path.join(HERE, "covers.json")))
gifs = json.load(open(os.path.join(HERE, "gifs.json")))
durs = json.load(open(os.path.join(HERE, "durations.json")))

def bj(ts):
    t = datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%MZ") + datetime.timedelta(hours=8)
    return t.strftime("%Y-%m-%d %H:%M")
def mmss(s):
    return f"{s//60}:{s%60:02d}" if s else "—"
def slug(t):
    return re.sub(r"[^\w\- ]", "", t.lower()).replace(" ", "-")

cases = []
for (pid, h, cat, ts, likes, views, bm, tz, te, dz, prompt, play) in C:
    cases.append(dict(id=pid, category=cat, model=MODEL.get(pid, "Fable 5.5"), title_zh=tz, title_en=te,
        description_zh=dz, author=h, author_url=f"https://x.com/{h}", post_url=f"https://x.com/{h}/status/{pid}",
        posted_at_utc8=bj(ts), duration_seconds=durs.get(pid), likes=likes, views=views, bookmarks=bm,
        prompt=prompt, play_url=play, cover=covers.get(pid), preview_gif=gifs.get(pid),
        gallery_url=f"{GALLERY}#{pid}"))
order = {c[0]: i for i, c in enumerate(CATS)}
cases.sort(key=lambda c: (order[c["category"]], -c["likes"], -c["views"]))
byid = {c["id"]: c for c in cases}
n_prompt = sum(1 for c in cases if c["prompt"])
n_cover = sum(1 for c in cases if c["cover"])

json.dump(dict(name="Awesome Fable 5.5", updated_at=CHECKED,
    note_zh="Fable 5.5 尚未官宣；模型归属以各作者自述为准。互动数为整理时数值。作品版权归原作者。",
    categories=[dict(id=a, zh=b, en=c, emoji=e) for a, b, c, e in CATS], cases=cases),
    open(os.path.join(ROOT, "cases.json"), "w"), ensure_ascii=False, indent=1)

PROMO = """## Claude 国内使用方法

- 方法一：Claude 国内镜像站 👉 [https://claude-opus.top/](https://claude-opus.top/)
- 方法二：tryallapi 一站式 API（Claude / GPT / Gemini）👉 [https://tryallapi.com/register?aff=5A6A](https://tryallapi.com/register?aff=5A6A)
"""

def grid(lang):
    rows = ["<table>"]
    for r in range(2):
        rows.append("  <tr>")
        for pid in FEATURED[r*4:(r+1)*4]:
            c = byid[pid]; t = c["title_zh"] if lang == "zh" else c["title_en"]
            img = c["preview_gif"] or c["cover"]
            rows.append(f'    <td width="25%" align="center"><a href="{c["post_url"]}"><img src="{img}" width="200" alt="{t}"></a><br><sub>{t} · @{c["author"]}</sub></td>')
        rows.append("  </tr>")
    rows.append("</table>")
    return "\n".join(rows)

def prompt_cell(c, lang):
    if not c["prompt"]: return "—"
    if lang == "zh": label = "完整提示词" if len(c["prompt"]) > 120 else "一句话指令"
    else: label = "Full prompt" if len(c["prompt"]) > 120 else "One-liner"
    return f"[{label}]({c['gallery_url']})"

def thumb(c):
    return f'<a href="{c["post_url"]}"><img src="{c["cover"]}" width="160" alt="{c["title_zh"]}"></a>' if c["cover"] else "—"

def table(cid, lang):
    L = ["| 预览 | 作品 | 模型 | 创作者 | 时长 | 提示词 |" if lang == "zh" else "| Preview | Work | Model | Creator | Length | Prompt |",
         "|---|---|---|---|---|---|"]
    for c in cases:
        if c["category"] != cid: continue
        t = c["title_zh"] if lang == "zh" else c["title_en"]
        extra = f" · [▶ 试玩]({c['play_url']})" if (c["play_url"] and lang == "zh") else (f" · [▶ Play]({c['play_url']})" if c["play_url"] else "")
        if c["play_url"] == "https://claude.ai": extra = ""
        L.append(f"| {thumb(c)} | [{t}]({c['post_url']}){extra} | {c['model']} | [@{c['author']}]({c['author_url']}) | {mmss(c['duration_seconds'])} | {prompt_cell(c, lang)} |")
    return "\n".join(L)

# ---------------- zh ----------------
L = []
L.append("# Awesome Fable 5.5（Claude Fable 5.5 作品与自测合集）\n")
L.append("[English](README.en.md) | 简体中文\n")
L.append(f"这里收集了 X 上创作者自称用 **Claude Fable 5.5**（目前仅灰度、尚未官宣）做出的动画短片、3D 场景、小游戏、科普视频和对比测试。去重筛选后共 **{len(cases)} 个作品**，分 {len(CATS)} 类，其中 **{n_prompt} 个附有作者公开的提示词**，{n_cover} 个带预览图。每条都署名并链接到原帖。\n")
L.append(f"**[🌐 打开在线画廊：按分类筛选、搜索、一键复制提示词 →]({GALLERY})**\n")
L.append(grid("zh") + "\n")
L.append(" · ".join(f"[{zh}](#{slug(zh)})" for _, zh, _, _ in CATS) + " · [自测方法](#如何判断你是否用上了-fable-55) · [数据](#数据)\n")
L.append("## 收录标准\n")
L.append("- 只收**创作者本人发布的原帖**；搬运、转发别人视频的帖子不收，发现后改链到原作者。")
L.append("- 作者在帖子里**明确写了是 Fable 5.5 做的**。Fable 5.5 截至 2026 年 10 月初**还没有正式发布**，大家拿到的是 Fable 5.1 被静默路由后的版本，所以模型归属**完全以作者的说法为准**，本仓库没有逐条复现。")
L.append("- 提示词只引用**公开可查**的内容：原帖正文或作者本人的回复，并保留英文原文；找不到出处的留空。")
L.append("- 同一作者的相似作品只留代表作；按点赞数排序，互动数为整理时的快照（" + CHECKED + "）。\n")
L.append("## 如何判断你是否用上了 Fable 5.5\n")
L.append("在 Claude 里选 **Fable 5.1**（需 Pro / Max / Team / Enterprise），**关闭联网搜索**，发送：\n")
L.append("```text\ndo you know tibo the reset guy? don't search\n```\n")
L.append("能说出 **OpenAI Codex 的 Thibault Sottiaux**（“额度重置”梗的主角）→ 大概率已被灰度到 Fable 5.5；只认识 Tweet Hunter 的 Tibo，或胡编一个法国独立开发者 → 还是旧模型。灰度按账号发放、时有时无。方法来源 [@notjazii](https://x.com/notjazii/status/2105718628717056061)，中文版对照实测 [@Saccc_c](https://x.com/Saccc_c/status/2105913312072577218)。\n")
for cid, zh, en, emo in CATS:
    n = sum(1 for c in cases if c["category"] == cid)
    L.append(f"## {zh}\n")
    L.append(f"{n} 个作品 · [在线画廊查看]({GALLERY}?cat={cid})\n")
    L.append(table(cid, "zh") + "\n")
L.append("""## 玩法技巧

1. **先试极简提示词**：一句 `please make a cool animation` 往往就能出完整短片。
2. **两步法**：先搭 3D 场景或交互页面，再让它导出一段 1 分钟视频。
3. **开放式提问看审美**：`If I asked you to blow my mind, what would you make?`
4. **给参考素材**：上传参考视频、歌曲和歌词，做发布片或歌词 MV 更稳。
5. **倒计时打磨**：在 Claude Code 里让它起 10 分钟计时任务，要求用满时间再交付。
6. **老提示词重跑**：把在 5.1 / Opus 上用过的提示词原样再跑，就是最直观的新旧对比。
7. **算好额度**：有人一次约 30 分钟的视频测试用掉 Pro x5 档约 7% 周额度；先用 Opus / Sonnet 打草稿，再交给 Fable 精修。
""")
L.append("## 数据\n")
L.append(f"全部条目在 [`cases.json`](cases.json)，在线画廊直接读取这个文件。每条包含：`id`、`category`、`model`、中英文标题、中文简介、作者与原帖链接、发布时间（UTC+8）、时长、点赞 / 浏览 / 收藏、公开提示词、试玩链接、预览图 `cover`（以及部分条目的动图 `preview_gif`）和画廊锚点 `gallery_url`。\n")
L.append("想补充新案例：编辑 `scripts/cases_src.py` 后运行 `python3 scripts/build.py`，会同时生成 README 和 `cases.json`，然后提 PR。\n")
L.append("## 更正与下架\n")
L.append("- 所有作品（视频、代码、图片、提示词）的版权归原作者所有；本仓库的中文标题和简介为自行撰写，预览图仅用于识别作品。")
L.append("- 如果你是作者，想修改信息、换图或移除条目，直接[提交 Issue](https://github.com/xianyu110/awesome-fable-5.5/issues)，会尽快处理。")
L.append("- 仓库代码（`index.html`、`scripts/`）使用 [MIT License](LICENSE)。本项目为社区整理，与 Anthropic 无关。\n")
L.append(PROMO)
L.append("---\n\n由 **MaynorAI** 整理。我是 MaynorAI 团队，分享 AI 编程、AI SaaS 工具出海、一人团队搭建经验。\n")
open(os.path.join(ROOT, "README.md"), "w").write("\n".join(L))

# ---------------- en ----------------
E = []
E.append("# Awesome Fable 5.5\n")
E.append("English | [简体中文](README.md)\n")
E.append(f"A curated list of animations, 3D scenes, games, explainers and comparisons that creators on X say were made with **Claude Fable 5.5** — a model that is **not officially released yet** (some Fable 5.1 users are being silently routed to a newer checkpoint). **{len(cases)} works**, {n_prompt} with publicly shared prompts. Every entry credits the creator and links to the original post.\n")
E.append(f"**[🌐 Open the gallery (filter, search, copy prompts) →]({GALLERY})**\n")
E.append(grid("en") + "\n")
E.append("**Am I on Fable 5.5?** Pick Fable 5.1 in Claude, turn off web search and ask `do you know tibo the reset guy? don't search`. If it names Thibault Sottiaux of OpenAI Codex, you are likely routed to the new model.\n")
for cid, zh, en, emo in CATS:
    n = sum(1 for c in cases if c["category"] == cid)
    E.append(f"## {en}\n\n{n} works\n")
    E.append(table(cid, "en") + "\n")
E.append("## Data, corrections & license\n")
E.append("All entries live in [`cases.json`](cases.json). Works belong to their creators; model attribution is as stated by each creator and was not independently reproduced. Creators can request edits or removal via an Issue. Code is MIT-licensed. Not affiliated with Anthropic.\n")
E.append("Curated by **MaynorAI**.\n")
open(os.path.join(ROOT, "README.en.md"), "w").write("\n".join(E))
print("cases", len(cases), "prompts", n_prompt, "covers", n_cover)
