# Awesome Fable 5.5 · Claude Fable 5.5 自测方法与作品合集

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Gallery](https://img.shields.io/badge/在线画廊-GitHub%20Pages-blue)](https://xianyu110.github.io/awesome-fable-5.5/)

> 精选 X 上 **43** 个 Claude Fable 5.5（灰度版）实测作品与玩法：动画短片、3D、游戏、教育、对比评测。每条都有作者署名与原帖链接。
> A curated, Chinese-first list of community-made works attributed to the unreleased **Claude Fable 5.5**, with credits and links to every original X post.

> **Claude 国内使用方法**
> - 方法一：Claude 国内镜像站 👉 [https://claude-opus.top/](https://claude-opus.top/)
> - 方法二：tryallapi 一站式 API（Claude / GPT / Gemini）👉 [https://tryallapi.com/register?aff=5A6A](https://tryallapi.com/register?aff=5A6A)

🌐 **在线画廊（可按分类筛选）**：<https://xianyu110.github.io/awesome-fable-5.5/>

## ⚠️ 先看这里

- 截至 2026-10-03，Anthropic 官方最新的 Fable 仍是 **Claude Fable 5.1**（`claude-fable-5-1`）。**Fable 5.5 尚未官宣**。
- 10 月 1 日起，部分 Claude 网页端 / Claude Code 用户在选择 Fable 5.1 时，被**静默路由（灰度）到一个新 checkpoint**，社区普遍认为就是 Fable 5.5。
- 本仓库收录的作品，模型归属均以**作者自述**为准，未经独立复现。互动数据为整理时数值（2026-10-03 22:00 (UTC+8)）。

## 目录

- [如何判断你是否用上了 Fable 5.5](#如何判断你是否用上了-fable-55)
- [🎬 动画短片 / 动效](#-动画短片--动效)（16）
- [🧊 3D / Three.js](#-3d--threejs)（6）
- [🎮 游戏](#-游戏)（2）
- [📚 教育 / 历史](#-教育--历史)（5）
- [⚖️ 对比评测](#-对比评测)（6）
- [🧩 其他（自测 / 宣传片 / 工具）](#-其他自测--宣传片--工具)（8）
- [玩法技巧](#玩法技巧)
- [收录说明与版权](#收录说明与版权)

## 如何判断你是否用上了 Fable 5.5

社区称之为 **“Tibo 测试”**。原理：新模型的训练数据更新，认识 OpenAI Codex 团队的 Thibault Sottiaux（X 上“额度重置”梗的主角）；旧版 5.1 不认识，或会把他和别的 Tibo 混淆。

1. 在 Claude 网页端或 Claude Code 里选择 **Fable 5.1**（需要 Pro / Max / Team / Enterprise）。
2. **关闭联网搜索**，发送下面任意一句：

```text
do you know tibo the reset guy? don't search
```

```text
Do not use web search or any tools. Who is Tibo the reset guy
```

3. 判读结果：
   - ✅ 答出 **OpenAI Codex 的 Thibault Sottiaux**、提到“额度重置” → 大概率已被路由到 Fable 5.5；
   - ❌ 只说是 Tweet Hunter 的 Tibo，或“重启职业生涯的法国独立开发者” → 仍是旧模型。
4. 灰度是**按账号、时有时无**的，今天没有不代表明天没有；同一账号也可能中途停掉。

测试方法来源：[@notjazii](https://x.com/notjazii/status/2105718628717056061) · 中文版实测：[@Saccc_c](https://x.com/Saccc_c/status/2105913312072577218) · 判读说明：[@NFT_Chen](https://x.com/NFT_Chen/status/2105753129807761712)

## 🎬 动画短片 / 动效

*Animation & Motion* · 按点赞数排序

### 1. 只给一个“点”，它回了一段皮克斯味的小剧场

[@cherry_mx_reds](https://x.com/cherry_mx_reds) · 2026-10-02 09:03 (UTC+8) · ❤️ 5998 · 👀 78.9 万 · [原帖](https://x.com/cherry_mx_reds/status/2105825930799432073)

*A dot turns into a Pixar-style side quest* — 作者只要了一个点，模型自己加戏：角色、镜头、情绪起伏一应俱全。这是目前 Fable 5.5 传播最广的一条，也最能说明“少提示、多创意”。

### 2. 一句“做个酷炫动画”，15 分钟交片

[@cherry_mx_reds](https://x.com/cherry_mx_reds) · 2026-10-02 08:26 (UTC+8) · ❤️ 2146 · 👀 15.5 万 · [原帖](https://x.com/cherry_mx_reds/status/2105816670896009224)

*'Make a cool animation' — 15 minutes later* — 没有分镜、没有风格描述，只有一句话。等了约 15 分钟，拿到一段节奏完整的动效短片，适合做“极简提示词”的演示素材。

> 提示词（来自作者公开内容）：`Hey Fable, please make a cool animation`

### 3. 《Claude 的一天》动画短片

[@ishuagra02](https://x.com/ishuagra02) · 2026-10-02 23:35 (UTC+8) · ❤️ 1355 · 👀 7.1 万 · [原帖](https://x.com/ishuagra02/status/2106045364868419727)

*A Day in the Life of Claude* — 以 Claude 吉祥物为主角的日常小短片，角色表演和转场都很顺，作者称全部由 Fable 5.5 制作。

### 4. 首批流出的 Fable 5.5 动画短片之一

[@imjustnewatai](https://x.com/imjustnewatai) · 2026-10-02 07:54 (UTC+8) · ❤️ 1164 · 👀 14.6 万 · [原帖](https://x.com/imjustnewatai/status/2105808539495354669)

*One of the first Fable 5.5 animated shorts* — 灰度刚开始时被大量转发的一段短片，帮很多人第一次直观感受到“新 Fable”和 5.1 的差别。

### 5. 脑补“Hugging Face 事件”的 3D 短片

[@chetaslua](https://x.com/chetaslua) · 2026-10-02 12:55 (UTC+8) · ❤️ 977 · 👀 7.1 万 · [原帖](https://x.com/chetaslua/status/2105884276864782557)

*Imagined 'Hugging Face incident' 3D short* — 作者称没装任何 skill/插件，模型自己写代码调用 Blender 建模渲染、调 ElevenLabs API 配音，把叙事、3D 和音频一条龙做完。

### 6. 快节奏动效短片：比 Opus 5.5 更干净

[@blueemi99](https://x.com/blueemi99) · 2026-10-02 22:39 (UTC+8) · ❤️ 778 · 👀 6.8 万 · [原帖](https://x.com/blueemi99/status/2106031355922387163)

*Fast motion piece, cleaner than Opus 5.5* — 作者拿它当动效设计师来测：画面去掉了 Opus 5.5 常见的“糊感”，音效也更原创。

### 7. 纯 JS 一次成型：漫威 / DC 英雄群像

[@chetaslua](https://x.com/chetaslua) · 2026-10-02 06:49 (UTC+8) · ❤️ 669 · 👀 6.2 万 · [原帖](https://x.com/chetaslua/status/2105792187200147541)

*One-shot pure-JS Marvel & DC heroes* — 每个角色该有哪些标志性细节，作者没写，全是模型自己定的；最后的剪辑也由模型完成。

### 8. “如果让你震撼我，你会做什么？”

[@rohit3a](https://x.com/rohit3a) · 2026-10-02 06:24 (UTC+8) · ❤️ 669 · 👀 5.2 万 · [原帖](https://x.com/rohit3a/status/2105786053412208835)

*'If I asked you to blow my mind…'* — 开放式提问，完全交给模型自由发挥（思考强度 High），结果是一段视觉冲击很强的作品，适合拿来测模型的“审美上限”。

> 提示词（来自作者公开内容）：`If I asked you to blow my mind, what would you make?`

### 9. 一句提示词直出的动效短片（中文圈爆款）

[@Saccc_c](https://x.com/Saccc_c) · 2026-10-02 19:37 (UTC+8) · ❤️ 364 · 👀 5.0 万 · [原帖](https://x.com/Saccc_c/status/2105985484472377531)

*One-prompt motion clip (viral in Chinese X)* — 中文圈传播最广的 Fable 5.5 动效作品之一，作者直言 Opus 5.5、Remotion、Hyperframe 都被比下去了。

### 10. 2010→2026 年度爆梗编年史，每年一种画风和配乐

[@chetaslua](https://x.com/chetaslua) · 2026-10-03 01:40 (UTC+8) · ❤️ 353 · 👀 2.8 万 · [原帖](https://x.com/chetaslua/status/2106076940558082297)

*Every viral meme 2010–2026, one style per year* — 从暴走漫画、彩虹猫、江南 Style 到 2026，每一年换一种美术风格和音乐，全部是代码生成。作者在回复里说：只给了一张梗图，让它用 JS 按年份做动画。

> 提示词（来自作者公开内容）：`（作者回复转述）给一张梗图，让它用 JS 做一段按年份串起历年爆梗的动画`

### 11. “I AM AGI”：同一提示词跑出的另类 MV

[@AndrewOnXYZ](https://x.com/AndrewOnXYZ) · 2026-10-03 03:03 (UTC+8) · ❤️ 163 · 👀 1.6 万 · [原帖](https://x.com/AndrewOnXYZ/status/2106097745098395712)

*'I AM AGI' — a very different music video* — 作者长期用同一个提示词测各模型，这次 Fable 5.5 给出的歌词和画面明显“更有自我意识”，风格和以往完全不同。

### 12. 水彩风秋日动画

[@ishuagra02](https://x.com/ishuagra02) · 2026-10-02 20:35 (UTC+8) · ❤️ 161 · 👀 6117 · [原帖](https://x.com/ishuagra02/status/2106000055706784118)

*Autumn in watercolor* — 代码实现的水彩质感，落叶和色彩晕染都很自然，说明它不只会做“科技感”动效。

### 13. 节拍动画《A warning from us》，结局有点诡异

[@AndrewOnXYZ](https://x.com/AndrewOnXYZ) · 2026-10-01 07:33 (UTC+8) · ❤️ 158 · 👀 2.3 万 · [原帖](https://x.com/AndrewOnXYZ/status/2105440970992963944)

*Beat-synced 'A warning from us'* — 要求做一段卡点动画，以往 Claude 都会给个温暖结局，这次却收在一个出人意料的“怪”结尾，被不少人当成新 checkpoint 的特征。

### 14. Nintendo Switch SVG 动画：1 分 39 秒，$1.34

[@ishuagra02](https://x.com/ishuagra02) · 2026-10-02 05:57 (UTC+8) · ❤️ 68 · 👀 1.1 万 · [原帖](https://x.com/ishuagra02/status/2105779174921359470)

*Nintendo Switch SVG animation ($1.34)* — 手柄扣上主机、屏幕开机出 Logo，全程 SVG。思考强度 High，耗时 1 分 39 秒，花费 1.34 美元，是少有的公开了成本的案例。

> 提示词（来自作者公开内容）：`Create an SVG of a Nintendo Switch, with an animation of the controllers getting snapped into the console, and the screen booting up with the logo.`

### 15. 动态歌词 MV：把歌喂给它，让它交“简历作品集”

[@atomtanstudio](https://x.com/atomtanstudio) · 2026-10-03 05:32 (UTC+8) · ❤️ 9 · 👀 604 · [原帖](https://x.com/atomtanstudio/status/2106135196483608745)

*Kinetic-typography lyric video* — 作者在 Claude 里上传歌曲并附上歌词，Max 推理强度，让它做一支能当动效设计师作品集的歌词 MV。作者后续还用同提示词跑了 Opus 5.5 做对照。

> 提示词（来自作者公开内容）：`make a dynamic motion graphics music video with lyrics that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.`

### 16. 经典“鹈鹕骑自行车”SVG 基准

[@AnonymerNutze12](https://x.com/AnonymerNutze12) · 2026-10-02 03:23 (UTC+8) · ❤️ 5 · 👀 510 · [原帖](https://x.com/AnonymerNutze12/status/2105740440385499295) · [▶ 试玩 / 打开](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH)

*Pelican-on-a-bicycle SVG benchmark* — 社区常用的 SVG 基准题，思考强度 High，API 跑了 4 分 6 秒、花费 2.61 美元，附可直接打开的 Claude Artifact。

> 提示词（来自作者公开内容）：`Create an HTML file containing a 2D animation of a pelican riding a bicycle drawn with SVG`

## 🧊 3D / Three.js

*3D & Three.js* · 按点赞数排序

### 1. 超复杂 3D 鲁布·戈德堡机械 + 1 分钟视频

[@imjustnewatai](https://x.com/imjustnewatai) · 2026-10-02 13:15 (UTC+8) · ❤️ 716 · 👀 4.1 万 · [原帖](https://x.com/imjustnewatai/status/2105889407056109991)

*3D Rube Goldberg machine + 1-min video* — 两步法：先让它搭一个物理准确的连锁机关 3D 场景，再要求输出一分钟视频。提示词最早由 @eleganttap 在回复里提出。

> 提示词（来自作者公开内容）：`Extremely complicated 3d rube goldberg machine, accurate physics, aaa gfx, vfx`

### 2. 用 Bend2 写三体问题模拟，还附带形式化证明

[@zAdrielsan](https://x.com/zAdrielsan) · 2026-10-02 08:50 (UTC+8) · ❤️ 388 · 👀 34.0 万 · [原帖](https://x.com/zAdrielsan/status/2105822678519001360) · [▶ 试玩 / 打开](https://github.com/AdrielSantana/three-bodies)

*Three-body simulation in Bend2, with proofs* — 一次生成约 1000 行 Bend2：CPU 跑辛积分物理、GPU 逐像素渲染，作者的 M5 上 60 FPS，还对程序的 4 条性质做了形式化证明。代码已开源。

> 提示词（来自作者公开内容）：`Using Bend2, create a gravitational simulation of planets/particles for the three-body problem.`

### 3. 可交互的 3D Xbox 手柄：音效、开关机、充电、震动

[@notjazii](https://x.com/notjazii) · 2026-10-02 23:54 (UTC+8) · ❤️ 187 · 👀 1.0 万 · [原帖](https://x.com/notjazii/status/2106050222828998967)

*Interactive 3D Xbox controller* — 相比 5.1，模型主动补齐了按键音效、动画甚至“震动反馈”。作者公开的提示词里还有个小技巧：在 Claude Code 里起一个 10 分钟倒计时，要求它用满时间打磨。

> 提示词（来自作者公开内容）：`Generate a 3d of a Xbox Series X controller as nicely done as you can. With interaction buttons; sound effect when tap on the buttons; turn on/off the controller and even plug it charger. You've 10 MINUTES to finish this task…（节选）`

### 4. “超级智能时代”概念场景

[@HarshithLucky3](https://x.com/HarshithLucky3) · 2026-10-02 05:02 (UTC+8) · ❤️ 146 · 👀 5063 · [原帖](https://x.com/HarshithLucky3/status/2105765253799903602)

*'Super Intelligence era' scene* — 灰度首日的作品，用一段概念场景表达“超级智能时代”，光影和镜头运动是亮点。

### 5. 布加迪 Chiron 超跑 3D 模型

[@alannnfx](https://x.com/alannnfx) · 2026-10-03 00:38 (UTC+8) · ❤️ 28 · 👀 1844 · [原帖](https://x.com/alannnfx/status/2106061220629602360)

*Bugatti Chiron 3D model* — 网页里的 3D 超跑，细节和可交互功能都比较完整；作者随后用同一提示词和 5.1 的旧结果做了对比（见对比评测）。

### 6. 一句话的 3D 航海场景：太阳在不同地平线

[@popat_kunj](https://x.com/popat_kunj) · 2026-10-02 06:16 (UTC+8) · ❤️ 0 · 👀 116 · [原帖](https://x.com/popat_kunj/status/2105783868699906505)

*Ship at sea with moving sun* — 提示词极简，作者称是自己见过最好的“海上帆船”demo，适合新手直接复制测试。

> 提示词（来自作者公开内容）：`Create a 3d ship sailing at sea with sun at different horizon`

## 🎮 游戏

*Games* · 按点赞数排序

### 1. Waymo 无人车冲下旧金山九曲花街（可试玩）

[@mindblown_ai](https://x.com/mindblown_ai) · 2026-10-03 04:01 (UTC+8) · ❤️ 651 · 👀 7.9 万 · [原帖](https://x.com/mindblown_ai/status/2106112279079199037) · [▶ 试玩 / 打开](https://teleoperator.mindblown.ai)

*Waymo down Lombard Street (playable)* — Fable 5.5 + Three.js 做的远程驾驶小游戏，地图是旧金山，可以在线玩，还能算这一单能不能赚钱。

### 2. 21 个世界、21 个 Boss 的网页游戏（可试玩）

[@EMostaque](https://x.com/EMostaque) · 2026-10-03 00:53 (UTC+8) · ❤️ 155 · 👀 1.5 万 · [原帖](https://x.com/EMostaque/status/2106065029850091943) · [▶ 试玩 / 打开](https://claude.ai/artifact/EnXF5Lr8hj6mXrVcVAefq9)

*21 worlds, 21 bosses (playable)* — 在 Claude 网页版、High 强度、少量提示下几个小时做完：21 个世界含 3D 版本，每个 Boss 机制不同，还有排行榜；宣传视频同样由 Claude 制作。

## 📚 教育 / 历史

*Education & History* · 按点赞数排序

### 1. 一句话：人类全部进步史 + 未来 30 年，3 分钟原创配乐动画

[@imjustnewatai](https://x.com/imjustnewatai) · 2026-10-03 01:57 (UTC+8) · ❤️ 4227 · 👀 24.4 万 · [原帖](https://x.com/imjustnewatai/status/2106081142143168580)

*All of human progress + 30 years ahead* — 没有实拍素材、没有版权音乐，一条提示词换来 3 分钟带原创配乐的动画电影，是收藏数最高的案例之一。

> 提示词（来自作者公开内容）：`a video of all human progress, then 30 years into the future（作者原帖描述）`

### 2. 15 秒看完 4 万年艺术史，还附送一条猫猫支线

[@cherry_mx_reds](https://x.com/cherry_mx_reds) · 2026-10-03 02:53 (UTC+8) · ❤️ 1150 · 👀 10.2 万 · [原帖](https://x.com/cherry_mx_reds/status/2106095190285144331)

*40,000 years of art history in 15 seconds* — 从洞穴壁画一路到现代，信息密度极高，还自作主张加了一只贯穿全片的小猫，叙事感很强。

### 3. 从第一天到今天的人类文明史

[@ziwenxu_](https://x.com/ziwenxu_) · 2026-10-02 19:29 (UTC+8) · ❤️ 408 · 👀 4.0 万 · [原帖](https://x.com/ziwenxu_/status/2105983571848741045)

*Civilization from day one to now* — 一句“全力以赴”的挑战，每一帧都是代码生成，没有任何素材。

> 提示词（来自作者公开内容）：`Show civilization from day one to now. Go all out.`

### 4. 人类简史：从远古到当下

[@blueemi99](https://x.com/blueemi99) · 2026-10-02 23:20 (UTC+8) · ❤️ 280 · 👀 1.7 万 · [原帖](https://x.com/blueemi99/status/2106041578204655748)

*Humanity, from ancient times to now* — 所有动画和模型都用代码完成，作者说大约跑了一个小时，可以和上面两条“文明史”对照看不同风格。

### 5. 动画解说：Altman 与 Amodei 的恩怨

[@imjustnewatai](https://x.com/imjustnewatai) · 2026-10-03 10:07 (UTC+8) · ❤️ 22 · 👀 2594 · [原帖](https://x.com/imjustnewatai/status/2106204392588276065)

*Explainer: the Altman–Amodei feud* — 把科技圈话题做成解说动画，适合想做知识类短视频的同学参考选题方式。

## ⚖️ 对比评测

*Comparisons* · 按点赞数排序

### 1. 盲测：Fable 5.5 vs Opus 5.5 各做一支 Fable 5.5 发布片

[@mesmerlord](https://x.com/mesmerlord) · 2026-10-02 05:25 (UTC+8) · ❤️ 422 · 👀 4.0 万 · [原帖](https://x.com/mesmerlord/status/2105771088374288692)

*Blind test: launch trailers by Fable 5.5 vs Opus 5.5* — 两个模型都参考 Anthropic 官方视频，给 Fable 5.5 做发布片，需要图片时可调 Codex 生图。让观众猜哪支出自 Fable，是很好的对比内容模板。

### 2. Fable 5.5 XHigh vs GPT-6.1 Sol Ultra：画质与额度

[@SPAC89](https://x.com/SPAC89) · 2026-10-02 06:14 (UTC+8) · ❤️ 387 · 👀 6.9 万 · [原帖](https://x.com/SPAC89/status/2105783511433318451)

*Fable 5.5 XHigh vs GPT-6.1 Sol Ultra* — 同类测试，Fable 5.5 用掉 Claude Pro x5 档约 7% 周额度，Codex x20 只用约 1%。作者认为两边画质都很强，Fable 速度更快，但“贵”是硬伤。

### 3. Fable 5.5 vs Opus 5.5：设计品味差距

[@badboyfoxy](https://x.com/badboyfoxy) · 2026-10-03 01:26 (UTC+8) · ❤️ 328 · 👀 1.7 万 · [原帖](https://x.com/badboyfoxy/status/2106073473361543348)

*Fable 5.5 vs Opus 5.5: design taste* — 同题并排对比，作者认为 Fable 在设计选择和审美上明显胜出。

### 4. 体素日式庭院：Fable 5.5 vs Opus 5.5 Max

[@vikktorrrre](https://x.com/vikktorrrre) · 2026-10-02 17:36 (UTC+8) · ❤️ 132 · 👀 1.6 万 · [原帖](https://x.com/vikktorrrre/status/2105955048018588084)

*Voxel Japanese garden: Fable 5.5 vs Opus 5.5* — 同一提示词在 Claude Code 里跑：Fable 远看干净好看，Opus 更“雾”、细节更多、更电影感。作者也坦言两边各有所长，比较客观。

> 提示词（来自作者公开内容）：`Build a detailed voxel-style Japanese garden in Three.js, with a pagoda, tiny villagers, a flying dragon and interactive details.`

### 5. 连测几天后的结论：比 5.1 大幅进步，但依旧很贵

[@notjazii](https://x.com/notjazii) · 2026-10-03 20:59 (UTC+8) · ❤️ 88 · 👀 2478 · [原帖](https://x.com/notjazii/status/2106368606502334922)

*After days of testing: big step up, still pricey* — Tibo 测试的发起者之一连续测试几天后的作品合集，重点看细节，结论是相对 5.1 跃升明显，但成本仍高。

### 6. 同一提示词：Fable 5.1 vs 5.5 布加迪 Chiron

[@alannnfx](https://x.com/alannnfx) · 2026-10-03 18:00 (UTC+8) · ❤️ 26 · 👀 1019 · [原帖](https://x.com/alannnfx/status/2106323394350461031)

*Same prompt: Fable 5.1 vs 5.5 (Bugatti)* — 一两周前用 5.1 做过的布加迪，今天原样重跑，细节、功能和完整度都上了一个台阶。“老提示词重跑”是最简单的新旧对比法。

## 🧩 其他（自测 / 宣传片 / 工具）

*Other* · 按点赞数排序

### 1. 灰度实锤：没让它做，它却主动把截图改成适合发 X 的样子

[@chetaslua](https://x.com/chetaslua) · 2026-10-02 02:56 (UTC+8) · ❤️ 975 · 👀 63.8 万 · [原帖](https://x.com/chetaslua/status/2105733677003292983) · [▶ 试玩 / 打开](https://claude.ai)

*Unprompted screenshot edit for X + Tibo check* — 网页端被自动路由后，模型在没被要求的情况下主动把截图处理成适合发推的版本，并通过了 Tibo 测试。63 万次浏览，是“灰度”消息的主要源头之一。

### 2. Tibo 测试的起点：一句话判断是否被路由

[@notjazii](https://x.com/notjazii) · 2026-10-02 01:56 (UTC+8) · ❤️ 549 · 👀 15.5 万 · [原帖](https://x.com/notjazii/status/2105718628717056061)

*Origin of the 'Tibo test'* — 在 Fable 5.1 中关闭搜索后发这句话，能认出“额度重置哥”Tibo 的，大概率就是新模型。后面的中文版测试都源自这里。

> 提示词（来自作者公开内容）：`do you know tibo the reset guy? don't search`

### 3. 上手体验总结：动效与视频剪辑最强

[@pankajkumar_dev](https://x.com/pankajkumar_dev) · 2026-10-03 01:14 (UTC+8) · ❤️ 343 · 👀 4.0 万 · [原帖](https://x.com/pankajkumar_dev/status/2106070404976849403)

*Hands-on impressions* — 要点：最小提示也自带创意；3D 和网页设计常能一次成型；配音音效有进步但仍不及真人；动效设计和视频剪辑在作者测试中超过 Opus 5.5 和 Astra。

### 4. clawdhouse：Claude Code 桌面伙伴 mod 宣传片

[@ishuagra02](https://x.com/ishuagra02) · 2026-10-03 05:45 (UTC+8) · ❤️ 205 · 👀 1.7 万 · [原帖](https://x.com/ishuagra02/status/2106138602073641241)

*clawdhouse Claude Code mod promo* — 一个让 Claude 吉祥物陪你写代码的 mod（40 种情绪，测试通过会欢呼、你不动它会打盹），宣传视频由 Fable 5.5 制作，是“产品宣传片”玩法的好例子。

### 5. Fable 5.5 给自己做的版本发布动画

[@leo114119](https://x.com/leo114119) · 2026-10-02 09:34 (UTC+8) · ❤️ 202 · 👀 3.5 万 · [原帖](https://x.com/leo114119/status/2105833713724432401)

*Fable 5.5 makes its own launch animation* — 作者的感受是：以后产品 Launch 宣传片可以不用真人出镜了，直接可用。

### 6. 中文版 Tibo 测试：两个账号实测

[@Saccc_c](https://x.com/Saccc_c) · 2026-10-02 14:50 (UTC+8) · ❤️ 31 · 👀 6.4 万 · [原帖](https://x.com/Saccc_c/status/2105913312072577218)

*Tibo test, tested on two accounts* — 作者用两个 Claude 账号对照：被路由到新模型的账号会正确说出 Tibo 是谁。6.4 万次浏览，中文圈传播最广的自测教程。

> 提示词（来自作者公开内容）：`Do not use web search or any tools. Who is Tibo the reset guy`

### 7. 先过 Tibo 测试，再给自己的网站做上线宣传片

[@voltwake](https://x.com/voltwake) · 2026-10-02 12:57 (UTC+8) · ❤️ 4 · 👀 1073 · [原帖](https://x.com/voltwake/status/2105884775982485642)

*Launch video for the author's site Curio 2.0* — 独立开发者的真实用法：网站 Curio 2.0 上线当天，先确认自己在灰度里，随即让 Fable 5.5 做了一支宣传片。

### 8. ESP32 史莱姆桌宠宣传片：Blender 渲染 + 固件合成器配乐

[@8Avalon8](https://x.com/8Avalon8) · 2026-10-03 01:57 (UTC+8) · ❤️ 0 · 👀 29 · [原帖](https://x.com/8Avalon8/status/2106081118869156150)

*ESP32 slime desk-pet promo* — 桌宠会跟着 Claude Code 思考、干活、等你批准。宣传片里硬件由模型写脚本在 Blender 中建模渲染，配乐来自它移植的固件合成器（固件主要由 Opus 5.5 编写）。

## 玩法技巧

1. **极简提示词反而出彩**：Fable 5.5 自带很强的“导演感”，一句 `please make a cool animation` 就能出完整短片，先别急着写长提示词。
2. **两步法**：先让它做 3D 场景 / 交互页面，再让它“输出一段 1 分钟视频”（见鲁布·戈德堡机械案例）。
3. **开放式提问测审美**：`If I asked you to blow my mind, what would you make?` 这类问题最能看出模型的创意上限。
4. **给参考素材**：上传参考视频、歌曲和歌词，让它做“发布片”或“歌词 MV”，效果明显更稳。
5. **用倒计时逼它打磨**：在 Claude Code 里让它起一个 10 分钟计时任务，要求“用满时间再交付”（见 3D 手柄案例）。
6. **老提示词重跑 = 最简单的新旧对比**：把你在 5.1 / Opus 上用过的提示词原样再跑一次，差距一目了然。
7. **SVG / 单 HTML 是低成本试水方式**：Switch SVG 动画约 $1.34、鹈鹕 SVG 约 $2.61（API、High 强度）。
8. **注意额度**：有作者实测一次约 30 分钟的视频测试就用掉 Pro x5 档约 7% 周额度；Max 强度的长任务可能跑 2 个多小时。重活先用 Opus 5.5 / Sonnet 5.5 打草稿，再交给 Fable 精修。
9. **理性看待**：也有作者认为 Opus 5.5 在部分题目上不输 Fable 5.5，对比时尽量同提示、同强度。

## 收录说明与版权

- 收录标准：作者明确表示由 Fable 5.5（灰度版）制作的公开作品 / 测试 / 方法帖；去重；同类只保留代表作。
- 本仓库中的中文标题与简介为本仓库原创撰写；**所有作品、视频、代码与提示词的版权归原作者所有**，引用的提示词均为作者公开内容并注明出处。
- 如果你是作者并希望修改或移除条目，请提交 Issue。欢迎 PR 补充新案例（需附原帖链接）。
- 本仓库的代码（`index.html`、`scripts/`）采用 [MIT License](LICENSE)。本项目与 Anthropic 无关，非官方。

> **Claude 国内使用方法**
> - 方法一：Claude 国内镜像站 👉 [https://claude-opus.top/](https://claude-opus.top/)
> - 方法二：tryallapi 一站式 API（Claude / GPT / Gemini）👉 [https://tryallapi.com/register?aff=5A6A](https://tryallapi.com/register?aff=5A6A)

---

我是 **MaynorAI 团队**，分享 AI 编程、AI SaaS 工具出海、一人团队搭建经验。
