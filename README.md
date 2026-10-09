# Awesome Fable 5.5（Claude Fable 5.5 作品与自测合集）

[English](README.en.md) | 简体中文

这里收集了 X 上创作者自称用 **Claude Fable 5.5**（目前仅灰度、尚未官宣）做出的动画短片、3D 场景、小游戏、科普视频和对比测试。去重筛选后共 **56 个作品**，分 6 类，其中 **16 个附有作者公开的提示词**，56 个带预览图。每条都署名并链接到原帖。

**[🌐 打开在线画廊：按分类筛选、搜索、一键复制提示词 →](https://xianyu110.github.io/awesome-fable-5.5/)**

<table>
  <tr>
    <td width="25%" align="center"><a href="https://x.com/cherry_mx_reds/status/2105825930799432073"><img src="https://upload.maynor1024.live/file/1791037304616_g_2105825930799432073.gif" width="200" alt="只给一个“点”，它回了一段皮克斯味的小剧场"></a><br><sub>只给一个“点”，它回了一段皮克斯味的小剧场 · @cherry_mx_reds</sub></td>
    <td width="25%" align="center"><a href="https://x.com/imjustnewatai/status/2106081142143168580"><img src="https://upload.maynor1024.live/file/1791037302133_g_2106081142143168580.gif" width="200" alt="一句话：人类全部进步史 + 未来 30 年，3 分钟原创配乐动画"></a><br><sub>一句话：人类全部进步史 + 未来 30 年，3 分钟原创配乐动画 · @imjustnewatai</sub></td>
    <td width="25%" align="center"><a href="https://x.com/chetaslua/status/2105757136219504862"><img src="https://upload.maynor1024.live/file/1791037296081_g_2105757136219504862.gif" width="200" alt="超人连续变身：一镜到底穿越多种美术风格"></a><br><sub>超人连续变身：一镜到底穿越多种美术风格 · @chetaslua</sub></td>
    <td width="25%" align="center"><a href="https://x.com/cherry_mx_reds/status/2106095190285144331"><img src="https://upload.maynor1024.live/file/1791037303524_g_2106095190285144331.gif" width="200" alt="15 秒看完 4 万年艺术史，还附送一条猫猫支线"></a><br><sub>15 秒看完 4 万年艺术史，还附送一条猫猫支线 · @cherry_mx_reds</sub></td>
  </tr>
  <tr>
    <td width="25%" align="center"><a href="https://x.com/ishuagra02/status/2106045364868419727"><img src="https://upload.maynor1024.live/file/1791037307248_g_2106045364868419727.gif" width="200" alt="《Claude 的一天》动画短片"></a><br><sub>《Claude 的一天》动画短片 · @ishuagra02</sub></td>
    <td width="25%" align="center"><a href="https://x.com/chetaslua/status/2105884276864782557"><img src="https://upload.maynor1024.live/file/1791037298646_g_2105884276864782557.gif" width="200" alt="脑补“Hugging Face 事件”的 3D 短片"></a><br><sub>脑补“Hugging Face 事件”的 3D 短片 · @chetaslua</sub></td>
    <td width="25%" align="center"><a href="https://x.com/imjustnewatai/status/2105889407056109991"><img src="https://upload.maynor1024.live/file/1791037307146_g_2105889407056109991.gif" width="200" alt="超复杂 3D 鲁布·戈德堡机械 + 1 分钟视频"></a><br><sub>超复杂 3D 鲁布·戈德堡机械 + 1 分钟视频 · @imjustnewatai</sub></td>
    <td width="25%" align="center"><a href="https://x.com/mindblown_ai/status/2106112279079199037"><img src="https://upload.maynor1024.live/file/1791037311202_g_2106112279079199037.gif" width="200" alt="Waymo 无人车冲下旧金山九曲花街（可试玩）"></a><br><sub>Waymo 无人车冲下旧金山九曲花街（可试玩） · @mindblown_ai</sub></td>
  </tr>
</table>

[动画短片 / 动效](#动画短片--动效) · [3D / Three.js](#3d--threejs) · [游戏](#游戏) · [教育 / 历史](#教育--历史) · [对比评测](#对比评测) · [其他（自测 / 宣传片 / 工具）](#其他自测--宣传片--工具) · [自测方法](#如何判断你是否用上了-fable-55) · [数据](#数据)

## 收录标准

- 只收**创作者本人发布的原帖**；搬运、转发别人视频的帖子不收，发现后改链到原作者。
- 作者在帖子里**明确写了是 Fable 5.5 做的**。Fable 5.5 截至 2026 年 10 月初**还没有正式发布**，大家拿到的是 Fable 5.1 被静默路由后的版本，所以模型归属**完全以作者的说法为准**，本仓库没有逐条复现。
- 提示词只引用**公开可查**的内容：原帖正文或作者本人的回复，并保留英文原文；找不到出处的留空。
- 同一作者的相似作品只留代表作；按点赞数排序，互动数为整理时的快照（2026-10-09 11:47 (UTC+8)）。

## 如何判断你是否用上了 Fable 5.5

在 Claude 里选 **Fable 5.1**（需 Pro / Max / Team / Enterprise），**关闭联网搜索**，发送：

```text
do you know tibo the reset guy? don't search
```

能说出 **OpenAI Codex 的 Thibault Sottiaux**（“额度重置”梗的主角）→ 大概率已被灰度到 Fable 5.5；只认识 Tweet Hunter 的 Tibo，或胡编一个法国独立开发者 → 还是旧模型。灰度按账号发放、时有时无。方法来源 [@notjazii](https://x.com/notjazii/status/2105718628717056061)，中文版对照实测 [@Saccc_c](https://x.com/Saccc_c/status/2105913312072577218)。

## 动画短片 / 动效

20 个作品 · [在线画廊查看](https://xianyu110.github.io/awesome-fable-5.5/?cat=motion)

| 预览 | 作品 | 模型 | 创作者 | 时长 | 提示词 |
|---|---|---|---|---|---|
| <a href="https://x.com/cherry_mx_reds/status/2105825930799432073"><img src="https://upload.maynor1024.live/file/1791037319155_c_2105825930799432073_mid.jpg" width="160" alt="只给一个“点”，它回了一段皮克斯味的小剧场"></a> | [只给一个“点”，它回了一段皮克斯味的小剧场](https://x.com/cherry_mx_reds/status/2105825930799432073) | Fable 5.5 | [@cherry_mx_reds](https://x.com/cherry_mx_reds) | 0:15 | — |
| <a href="https://x.com/chetaslua/status/2105757136219504862"><img src="https://upload.maynor1024.live/file/1791037192101_c_2105757136219504862.jpg" width="160" alt="超人连续变身：一镜到底穿越多种美术风格"></a> | [超人连续变身：一镜到底穿越多种美术风格](https://x.com/chetaslua/status/2105757136219504862) | Fable 5.5 | [@chetaslua](https://x.com/chetaslua) | 0:40 | — |
| <a href="https://x.com/cherry_mx_reds/status/2105816670896009224"><img src="https://upload.maynor1024.live/file/1791037167388_c_2105816670896009224.jpg" width="160" alt="一句“做个酷炫动画”，15 分钟交片"></a> | [一句“做个酷炫动画”，15 分钟交片](https://x.com/cherry_mx_reds/status/2105816670896009224) | Fable 5.5 | [@cherry_mx_reds](https://x.com/cherry_mx_reds) | 0:17 | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105816670896009224) |
| <a href="https://x.com/ishuagra02/status/2106045364868419727"><img src="https://upload.maynor1024.live/file/1791037705498_u_2106045364868419727.jpg" width="160" alt="《Claude 的一天》动画短片"></a> | [《Claude 的一天》动画短片](https://x.com/ishuagra02/status/2106045364868419727) | Fable 5.5 | [@ishuagra02](https://x.com/ishuagra02) | 1:31 | — |
| <a href="https://x.com/imjustnewatai/status/2105808539495354669"><img src="https://upload.maynor1024.live/file/1791037704557_u_2105808539495354669.jpg" width="160" alt="首批流出的 Fable 5.5 动画短片之一"></a> | [首批流出的 Fable 5.5 动画短片之一](https://x.com/imjustnewatai/status/2105808539495354669) | Fable 5.5 | [@imjustnewatai](https://x.com/imjustnewatai) | 1:02 | — |
| <a href="https://x.com/chetaslua/status/2105884276864782557"><img src="https://upload.maynor1024.live/file/1791037706553_u_2105884276864782557.jpg" width="160" alt="脑补“Hugging Face 事件”的 3D 短片"></a> | [脑补“Hugging Face 事件”的 3D 短片](https://x.com/chetaslua/status/2105884276864782557) | Fable 5.5 | [@chetaslua](https://x.com/chetaslua) | 3:41 | — |
| <a href="https://x.com/blueemi99/status/2107459553369760024"><img src="https://pbs.twimg.com/amplify_video_thumb/2107191414140411904/img/Av_DHTnwHSqG5aD3.jpg" width="160" alt="Brainrot 剪辑：自称只要 25 美元"></a> | [Brainrot 剪辑：自称只要 25 美元](https://x.com/blueemi99/status/2107459553369760024) | Fable 5.5 | [@blueemi99](https://x.com/blueemi99) | 0:30 | — |
| <a href="https://x.com/blueemi99/status/2106031355922387163"><img src="https://upload.maynor1024.live/file/1791037699614_u_2106031355922387163.jpg" width="160" alt="快节奏动效短片：比 Opus 5.5 更干净"></a> | [快节奏动效短片：比 Opus 5.5 更干净](https://x.com/blueemi99/status/2106031355922387163) | Fable 5.5 | [@blueemi99](https://x.com/blueemi99) | 0:15 | — |
| <a href="https://x.com/AndrewOnXYZ/status/2107262468502544435"><img src="https://pbs.twimg.com/amplify_video_thumb/2107261834931650560/img/nyFrC9GJYEmTG6Ii.jpg" width="160" alt="经典火柴人互殴，动作顺到离谱"></a> | [经典火柴人互殴，动作顺到离谱](https://x.com/AndrewOnXYZ/status/2107262468502544435) | Fable 5.5 | [@AndrewOnXYZ](https://x.com/AndrewOnXYZ) | 2:36 | — |
| <a href="https://x.com/chetaslua/status/2105792187200147541"><img src="https://upload.maynor1024.live/file/1791037172811_c_2105792187200147541.jpg" width="160" alt="纯 JS 一次成型：漫威 / DC 英雄群像"></a> | [纯 JS 一次成型：漫威 / DC 英雄群像](https://x.com/chetaslua/status/2105792187200147541) | Fable 5.5 | [@chetaslua](https://x.com/chetaslua) | 0:47 | — |
| <a href="https://x.com/rohit3a/status/2105786053412208835"><img src="https://upload.maynor1024.live/file/1791037174888_c_2105786053412208835.jpg" width="160" alt="“如果让你震撼我，你会做什么？”"></a> | [“如果让你震撼我，你会做什么？”](https://x.com/rohit3a/status/2105786053412208835) | Fable 5.5 | [@rohit3a](https://x.com/rohit3a) | 0:53 | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105786053412208835) |
| <a href="https://x.com/Saccc_c/status/2105985484472377531"><img src="https://upload.maynor1024.live/file/1791037176947_c_2105985484472377531.jpg" width="160" alt="一句提示词直出的动效短片（中文圈爆款）"></a> | [一句提示词直出的动效短片（中文圈爆款）](https://x.com/Saccc_c/status/2105985484472377531) | Fable 5.5 | [@Saccc_c](https://x.com/Saccc_c) | 0:15 | — |
| <a href="https://x.com/chetaslua/status/2106076940558082297"><img src="https://upload.maynor1024.live/file/1791037181007_c_2106076940558082297.jpg" width="160" alt="2010→2026 年度爆梗编年史，每年一种画风和配乐"></a> | [2010→2026 年度爆梗编年史，每年一种画风和配乐](https://x.com/chetaslua/status/2106076940558082297) | Fable 5.5 | [@chetaslua](https://x.com/chetaslua) | 1:38 | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2106076940558082297) |
| <a href="https://x.com/AndrewOnXYZ/status/2106097745098395712"><img src="https://upload.maynor1024.live/file/1791037707404_u_2106097745098395712.jpg" width="160" alt="“I AM AGI”：同一提示词跑出的另类 MV"></a> | [“I AM AGI”：同一提示词跑出的另类 MV](https://x.com/AndrewOnXYZ/status/2106097745098395712) | Fable 5.5 | [@AndrewOnXYZ](https://x.com/AndrewOnXYZ) | 4:26 | — |
| <a href="https://x.com/ishuagra02/status/2106000055706784118"><img src="https://upload.maynor1024.live/file/1791037175887_c_2106000055706784118.jpg" width="160" alt="水彩风秋日动画"></a> | [水彩风秋日动画](https://x.com/ishuagra02/status/2106000055706784118) | Fable 5.5 | [@ishuagra02](https://x.com/ishuagra02) | 0:25 | — |
| <a href="https://x.com/AndrewOnXYZ/status/2105440970992963944"><img src="https://upload.maynor1024.live/file/1791037695313_u_2105440970992963944.jpg" width="160" alt="节拍动画《A warning from us》，结局有点诡异"></a> | [节拍动画《A warning from us》，结局有点诡异](https://x.com/AndrewOnXYZ/status/2105440970992963944) | Fable 5.5 | [@AndrewOnXYZ](https://x.com/AndrewOnXYZ) | 4:26 | — |
| <a href="https://x.com/ishuagra02/status/2105779174921359470"><img src="https://upload.maynor1024.live/file/1791037702199_u_2105779174921359470.jpg" width="160" alt="Nintendo Switch SVG 动画：1 分 39 秒，$1.34"></a> | [Nintendo Switch SVG 动画：1 分 39 秒，$1.34](https://x.com/ishuagra02/status/2105779174921359470) | Fable 5.5 | [@ishuagra02](https://x.com/ishuagra02) | 0:05 | [完整提示词](https://xianyu110.github.io/awesome-fable-5.5/#2105779174921359470) |
| <a href="https://x.com/notdwd/status/2107816799840690589"><img src="https://pbs.twimg.com/amplify_video_thumb/2107804568998567936/img/A5uhWWR9q-uB7qje.jpg" width="160" alt="1 小时内复刻高质量动效设计（附完整提示词）"></a> | [1 小时内复刻高质量动效设计（附完整提示词）](https://x.com/notdwd/status/2107816799840690589) | Fable 5.5 | [@notdwd](https://x.com/notdwd) | 0:20 | [完整提示词](https://xianyu110.github.io/awesome-fable-5.5/#2107816799840690589) |
| <a href="https://x.com/atomtanstudio/status/2106135196483608745"><img src="https://upload.maynor1024.live/file/1791037707238_u_2106135196483608745.jpg" width="160" alt="动态歌词 MV：把歌喂给它，让它交“简历作品集”"></a> | [动态歌词 MV：把歌喂给它，让它交“简历作品集”](https://x.com/atomtanstudio/status/2106135196483608745) | Fable 5.5 | [@atomtanstudio](https://x.com/atomtanstudio) | 4:39 | [完整提示词](https://xianyu110.github.io/awesome-fable-5.5/#2106135196483608745) |
| <a href="https://x.com/AnonymerNutze12/status/2105740440385499295"><img src="https://upload.maynor1024.live/file/1791037572859_c_pelican.jpg" width="160" alt="经典“鹈鹕骑自行车”SVG 基准"></a> | [经典“鹈鹕骑自行车”SVG 基准](https://x.com/AnonymerNutze12/status/2105740440385499295) · [▶ 试玩](https://claude.ai/artifact/697meWJLt1jck5iq14x9HH) | Fable 5.5 | [@AnonymerNutze12](https://x.com/AnonymerNutze12) | — | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105740440385499295) |

## 3D / Three.js

7 个作品 · [在线画廊查看](https://xianyu110.github.io/awesome-fable-5.5/?cat=3d)

| 预览 | 作品 | 模型 | 创作者 | 时长 | 提示词 |
|---|---|---|---|---|---|
| <a href="https://x.com/JaydenDavisNC/status/2107086714820870617"><img src="https://pbs.twimg.com/amplify_video_thumb/2107086270514044928/img/zujM-sQh4dqJNAEW.jpg" width="160" alt="Blender 全流程点阵动画：音乐/建模/绑定"></a> | [Blender 全流程点阵动画：音乐/建模/绑定](https://x.com/JaydenDavisNC/status/2107086714820870617) | Fable 5.5 | [@JaydenDavisNC](https://x.com/JaydenDavisNC) | 0:17 | — |
| <a href="https://x.com/imjustnewatai/status/2105889407056109991"><img src="https://upload.maynor1024.live/file/1791037183240_c_2105889407056109991.jpg" width="160" alt="超复杂 3D 鲁布·戈德堡机械 + 1 分钟视频"></a> | [超复杂 3D 鲁布·戈德堡机械 + 1 分钟视频](https://x.com/imjustnewatai/status/2105889407056109991) | Fable 5.5 | [@imjustnewatai](https://x.com/imjustnewatai) | 1:00 | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105889407056109991) |
| <a href="https://x.com/zAdrielsan/status/2105822678519001360"><img src="https://upload.maynor1024.live/file/1791037187087_c_2105822678519001360.jpg" width="160" alt="用 Bend2 写三体问题模拟，还附带形式化证明"></a> | [用 Bend2 写三体问题模拟，还附带形式化证明](https://x.com/zAdrielsan/status/2105822678519001360) · [▶ 试玩](https://github.com/AdrielSantana/three-bodies) | Fable 5.5 | [@zAdrielsan](https://x.com/zAdrielsan) | 2:14 | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105822678519001360) |
| <a href="https://x.com/notjazii/status/2106050222828998967"><img src="https://upload.maynor1024.live/file/1791037189568_c_2106050222828998967.jpg" width="160" alt="可交互的 3D Xbox 手柄：音效、开关机、充电、震动"></a> | [可交互的 3D Xbox 手柄：音效、开关机、充电、震动](https://x.com/notjazii/status/2106050222828998967) | Fable 5.5 | [@notjazii](https://x.com/notjazii) | 0:34 | [完整提示词](https://xianyu110.github.io/awesome-fable-5.5/#2106050222828998967) |
| <a href="https://x.com/alannnfx/status/2106061220629602360"><img src="https://upload.maynor1024.live/file/1791037192549_c_2106061220629602360.jpg" width="160" alt="布加迪 Chiron 超跑 3D 模型"></a> | [布加迪 Chiron 超跑 3D 模型](https://x.com/alannnfx/status/2106061220629602360) | Fable 5.5 | [@alannnfx](https://x.com/alannnfx) | — | — |
| <a href="https://x.com/popat_kunj/status/2105783868699906505"><img src="https://upload.maynor1024.live/file/1791037194928_c_2105783868699906505.jpg" width="160" alt="一句话的 3D 航海场景：太阳在不同地平线"></a> | [一句话的 3D 航海场景：太阳在不同地平线](https://x.com/popat_kunj/status/2105783868699906505) | Fable 5.5 | [@popat_kunj](https://x.com/popat_kunj) | — | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105783868699906505) |
| <a href="https://x.com/RobinDenmark/status/2108194732744888801"><img src="https://pbs.twimg.com/amplify_video_thumb/2108194611084591104/img/XAybfvMKXPxkPUX2.jpg" width="160" alt="密封热带雨林：Three.js 微型生态箱"></a> | [密封热带雨林：Three.js 微型生态箱](https://x.com/RobinDenmark/status/2108194732744888801) · [▶ 试玩](https://silva-minima.vercel.app/) | Fable 5.5 | [@RobinDenmark](https://x.com/RobinDenmark) | 0:42 | — |

## 游戏

6 个作品 · [在线画廊查看](https://xianyu110.github.io/awesome-fable-5.5/?cat=game)

| 预览 | 作品 | 模型 | 创作者 | 时长 | 提示词 |
|---|---|---|---|---|---|
| <a href="https://x.com/anshuc/status/2107180724399075488"><img src="https://pbs.twimg.com/amplify_video_thumb/2107180356981997569/img/c5WEnmn7Rk6KHPUe.jpg" width="160" alt="POKERMON：宝可梦 × Balatro 可玩页"></a> | [POKERMON：宝可梦 × Balatro 可玩页](https://x.com/anshuc/status/2107180724399075488) · [▶ 试玩](https://pokermon.anshu.dev) | Fable 5.5 | [@anshuc](https://x.com/anshuc) | 0:47 | — |
| <a href="https://x.com/blueemi99/status/2107108802440900621"><img src="https://pbs.twimg.com/amplify_video_thumb/2107108711537745920/img/0e0hH7adfbKywwB8.jpg" width="160" alt="Clawd 像素打怪：Artifact 可玩"></a> | [Clawd 像素打怪：Artifact 可玩](https://x.com/blueemi99/status/2107108802440900621) · [▶ 试玩](https://claude.ai/artifact/Bor4eKVfaKakr6QSfoT8UZ) | Fable 5.5 | [@blueemi99](https://x.com/blueemi99) | 1:24 | — |
| <a href="https://x.com/mindblown_ai/status/2106112279079199037"><img src="https://upload.maynor1024.live/file/1791037193156_c_2106112279079199037.jpg" width="160" alt="Waymo 无人车冲下旧金山九曲花街（可试玩）"></a> | [Waymo 无人车冲下旧金山九曲花街（可试玩）](https://x.com/mindblown_ai/status/2106112279079199037) · [▶ 试玩](https://teleoperator.mindblown.ai) | Fable 5.5 | [@mindblown_ai](https://x.com/mindblown_ai) | 1:13 | — |
| <a href="https://x.com/oalanicolas/status/2107803303832936679"><img src="https://pbs.twimg.com/amplify_video_thumb/2107801963777687552/img/EPmn9zUSh83dTVpQ.jpg" width="160" alt="浏览器里跑的“GTA6”（Fable 5.5 + Opus 5.5）"></a> | [浏览器里跑的“GTA6”（Fable 5.5 + Opus 5.5）](https://x.com/oalanicolas/status/2107803303832936679) | Fable 5.5 + Opus 5.5 | [@oalanicolas](https://x.com/oalanicolas) | 1:50 | — |
| <a href="https://x.com/blueemi99/status/2108221060655055242"><img src="https://pbs.twimg.com/amplify_video_thumb/2108220392938545152/img/VLeytYV7Zz9SakIu.jpg" width="160" alt="一小时 oneshot 的 Minecraft 克隆（UI/生物/生物群系齐全）"></a> | [一小时 oneshot 的 Minecraft 克隆（UI/生物/生物群系齐全）](https://x.com/blueemi99/status/2108221060655055242) · [▶ 试玩](https://claude.ai/artifact/QJQU3kDzXpMG1CBFCZceZ3) | Fable 5.5 | [@blueemi99](https://x.com/blueemi99) | 1:29 | — |
| <a href="https://x.com/EMostaque/status/2106065029850091943"><img src="https://upload.maynor1024.live/file/1791037199682_c_2106065029850091943.jpg" width="160" alt="21 个世界、21 个 Boss 的网页游戏（可试玩）"></a> | [21 个世界、21 个 Boss 的网页游戏（可试玩）](https://x.com/EMostaque/status/2106065029850091943) · [▶ 试玩](https://claude.ai/artifact/EnXF5Lr8hj6mXrVcVAefq9) | Fable 5.5 | [@EMostaque](https://x.com/EMostaque) | 0:59 | — |

## 教育 / 历史

8 个作品 · [在线画廊查看](https://xianyu110.github.io/awesome-fable-5.5/?cat=edu)

| 预览 | 作品 | 模型 | 创作者 | 时长 | 提示词 |
|---|---|---|---|---|---|
| <a href="https://x.com/imjustnewatai/status/2106081142143168580"><img src="https://upload.maynor1024.live/file/1791037712510_u_2106081142143168580.jpg" width="160" alt="一句话：人类全部进步史 + 未来 30 年，3 分钟原创配乐动画"></a> | [一句话：人类全部进步史 + 未来 30 年，3 分钟原创配乐动画](https://x.com/imjustnewatai/status/2106081142143168580) | Fable 5.5 | [@imjustnewatai](https://x.com/imjustnewatai) | 3:09 | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2106081142143168580) |
| <a href="https://x.com/cherry_mx_reds/status/2106095190285144331"><img src="https://upload.maynor1024.live/file/1791037197113_c_2106095190285144331.jpg" width="160" alt="15 秒看完 4 万年艺术史，还附送一条猫猫支线"></a> | [15 秒看完 4 万年艺术史，还附送一条猫猫支线](https://x.com/cherry_mx_reds/status/2106095190285144331) | Fable 5.5 | [@cherry_mx_reds](https://x.com/cherry_mx_reds) | 0:15 | — |
| <a href="https://x.com/ziwenxu_/status/2105983571848741045"><img src="https://upload.maynor1024.live/file/1791037206584_c_2105983571848741045.jpg" width="160" alt="从第一天到今天的人类文明史"></a> | [从第一天到今天的人类文明史](https://x.com/ziwenxu_/status/2105983571848741045) | Fable 5.5 | [@ziwenxu_](https://x.com/ziwenxu_) | 3:06 | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105983571848741045) |
| <a href="https://x.com/blueemi99/status/2106041578204655748"><img src="https://upload.maynor1024.live/file/1791037706955_u_2106041578204655748.jpg" width="160" alt="人类简史：从远古到当下"></a> | [人类简史：从远古到当下](https://x.com/blueemi99/status/2106041578204655748) | Fable 5.5 | [@blueemi99](https://x.com/blueemi99) | 2:00 | — |
| <a href="https://x.com/imjustnewatai/status/2107615459822453187"><img src="https://pbs.twimg.com/amplify_video_thumb/2107615366415331328/img/zCeTbw6K4nJwi1rV.jpg" width="160" alt="准黎曼假设证明：2 分钟 3D 讲解"></a> | [准黎曼假设证明：2 分钟 3D 讲解](https://x.com/imjustnewatai/status/2107615459822453187) | Fable 5.5 | [@imjustnewatai](https://x.com/imjustnewatai) | 2:13 | — |
| <a href="https://x.com/oalanicolas/status/2107958931230241037"><img src="https://pbs.twimg.com/amplify_video_thumb/2107956735025500160/img/-P_YJ25lEZwgL6z1.jpg" width="160" alt="涂鸦版人类史：16 个时代，每段换画风和配乐"></a> | [涂鸦版人类史：16 个时代，每段换画风和配乐](https://x.com/oalanicolas/status/2107958931230241037) | Fable 5.5 | [@oalanicolas](https://x.com/oalanicolas) | 1:29 | — |
| <a href="https://x.com/imjustnewatai/status/2107970825542345211"><img src="https://pbs.twimg.com/amplify_video_thumb/2107970490560049153/img/j-Sb8OPW9MZpglNo.jpg" width="160" alt="OpenAI 23 页 π 证明：2 分钟配音 3D 讲解"></a> | [OpenAI 23 页 π 证明：2 分钟配音 3D 讲解](https://x.com/imjustnewatai/status/2107970825542345211) | Fable 5.5 | [@imjustnewatai](https://x.com/imjustnewatai) | 2:14 | — |
| <a href="https://x.com/imjustnewatai/status/2106204392588276065"><img src="https://upload.maynor1024.live/file/1791037716213_u_2106204392588276065.jpg" width="160" alt="动画解说：Altman 与 Amodei 的恩怨"></a> | [动画解说：Altman 与 Amodei 的恩怨](https://x.com/imjustnewatai/status/2106204392588276065) | Fable 5.5 | [@imjustnewatai](https://x.com/imjustnewatai) | 1:41 | — |

## 对比评测

7 个作品 · [在线画廊查看](https://xianyu110.github.io/awesome-fable-5.5/?cat=compare)

| 预览 | 作品 | 模型 | 创作者 | 时长 | 提示词 |
|---|---|---|---|---|---|
| <a href="https://x.com/mesmerlord/status/2105771088374288692"><img src="https://upload.maynor1024.live/file/1791037698252_u_2105771088374288692.jpg" width="160" alt="盲测：Fable 5.5 vs Opus 5.5 各做一支 Fable 5.5 发布片"></a> | [盲测：Fable 5.5 vs Opus 5.5 各做一支 Fable 5.5 发布片](https://x.com/mesmerlord/status/2105771088374288692) | Fable 5.5 vs Opus 5.5 | [@mesmerlord](https://x.com/mesmerlord) | 1:20 | — |
| <a href="https://x.com/SPAC89/status/2105783511433318451"><img src="https://upload.maynor1024.live/file/1791037210127_c_2105783511433318451.jpg" width="160" alt="Fable 5.5 XHigh vs GPT-6.1 Sol Ultra：画质与额度"></a> | [Fable 5.5 XHigh vs GPT-6.1 Sol Ultra：画质与额度](https://x.com/SPAC89/status/2105783511433318451) | Fable 5.5 vs GPT-6.1 | [@SPAC89](https://x.com/SPAC89) | 0:20 | — |
| <a href="https://x.com/badboyfoxy/status/2106073473361543348"><img src="https://upload.maynor1024.live/file/1791037205497_c_2106073473361543348.jpg" width="160" alt="Fable 5.5 vs Opus 5.5：设计品味差距"></a> | [Fable 5.5 vs Opus 5.5：设计品味差距](https://x.com/badboyfoxy/status/2106073473361543348) | Fable 5.5 vs Opus 5.5 | [@badboyfoxy](https://x.com/badboyfoxy) | 0:35 | — |
| <a href="https://x.com/vikktorrrre/status/2105955048018588084"><img src="https://upload.maynor1024.live/file/1791037211367_c_2105955048018588084.jpg" width="160" alt="体素日式庭院：Fable 5.5 vs Opus 5.5 Max"></a> | [体素日式庭院：Fable 5.5 vs Opus 5.5 Max](https://x.com/vikktorrrre/status/2105955048018588084) | Fable 5.5 vs Opus 5.5 | [@vikktorrrre](https://x.com/vikktorrrre) | 1:04 | [完整提示词](https://xianyu110.github.io/awesome-fable-5.5/#2105955048018588084) |
| <a href="https://x.com/notjazii/status/2106368606502334922"><img src="https://upload.maynor1024.live/file/1791037217317_c_2106368606502334922.jpg" width="160" alt="连测几天后的结论：比 5.1 大幅进步，但依旧很贵"></a> | [连测几天后的结论：比 5.1 大幅进步，但依旧很贵](https://x.com/notjazii/status/2106368606502334922) | Fable 5.5 | [@notjazii](https://x.com/notjazii) | 1:25 | — |
| <a href="https://x.com/notjazii/status/2107497752217460896"><img src="https://pbs.twimg.com/amplify_video_thumb/2107497541386608640/img/A68to733RgDy5n1c.jpg" width="160" alt="Claude vs GPT：全代码对比视频"></a> | [Claude vs GPT：全代码对比视频](https://x.com/notjazii/status/2107497752217460896) | Fable 5.5 | [@notjazii](https://x.com/notjazii) | 1:24 | — |
| <a href="https://x.com/alannnfx/status/2106323394350461031"><img src="https://upload.maynor1024.live/file/1791037214674_c_2106323394350461031.jpg" width="160" alt="同一提示词：Fable 5.1 vs 5.5 布加迪 Chiron"></a> | [同一提示词：Fable 5.1 vs 5.5 布加迪 Chiron](https://x.com/alannnfx/status/2106323394350461031) | Fable 5.5 vs 5.1 | [@alannnfx](https://x.com/alannnfx) | 0:16 | — |

## 其他（自测 / 宣传片 / 工具）

8 个作品 · [在线画廊查看](https://xianyu110.github.io/awesome-fable-5.5/?cat=other)

| 预览 | 作品 | 模型 | 创作者 | 时长 | 提示词 |
|---|---|---|---|---|---|
| <a href="https://x.com/chetaslua/status/2105733677003292983"><img src="https://upload.maynor1024.live/file/1791037211883_c_2105733677003292983.jpg" width="160" alt="灰度实锤：没让它做，它却主动把截图改成适合发 X 的样子"></a> | [灰度实锤：没让它做，它却主动把截图改成适合发 X 的样子](https://x.com/chetaslua/status/2105733677003292983) | Fable 5.5 | [@chetaslua](https://x.com/chetaslua) | — | — |
| <a href="https://x.com/notjazii/status/2105718628717056061"><img src="https://upload.maynor1024.live/file/1791037218854_c_2105718628717056061.jpg" width="160" alt="Tibo 测试的起点：一句话判断是否被路由"></a> | [Tibo 测试的起点：一句话判断是否被路由](https://x.com/notjazii/status/2105718628717056061) | Fable 5.5 | [@notjazii](https://x.com/notjazii) | — | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105718628717056061) |
| <a href="https://x.com/pankajkumar_dev/status/2106070404976849403"><img src="https://upload.maynor1024.live/file/1791037216998_c_2106070404976849403.jpg" width="160" alt="上手体验总结：动效与视频剪辑最强"></a> | [上手体验总结：动效与视频剪辑最强](https://x.com/pankajkumar_dev/status/2106070404976849403) | Fable 5.5 | [@pankajkumar_dev](https://x.com/pankajkumar_dev) | — | — |
| <a href="https://x.com/ishuagra02/status/2107164574239604925"><img src="https://pbs.twimg.com/amplify_video_thumb/2107164545152131073/img/2RCGBr_PFX8wnqOf.jpg" width="160" alt="Hello Claude 产品宣传动画"></a> | [Hello Claude 产品宣传动画](https://x.com/ishuagra02/status/2107164574239604925) | Fable 5.5 | [@ishuagra02](https://x.com/ishuagra02) | 0:58 | — |
| <a href="https://x.com/ishuagra02/status/2106138602073641241"><img src="https://upload.maynor1024.live/file/1791037714145_u_2106138602073641241.jpg" width="160" alt="clawdhouse：Claude Code 桌面伙伴 mod 宣传片"></a> | [clawdhouse：Claude Code 桌面伙伴 mod 宣传片](https://x.com/ishuagra02/status/2106138602073641241) | Fable 5.5 | [@ishuagra02](https://x.com/ishuagra02) | 0:37 | — |
| <a href="https://x.com/Saccc_c/status/2105913312072577218"><img src="https://upload.maynor1024.live/file/1791037224866_c_2105913312072577218.jpg" width="160" alt="中文版 Tibo 测试：两个账号实测"></a> | [中文版 Tibo 测试：两个账号实测](https://x.com/Saccc_c/status/2105913312072577218) | Fable 5.5 | [@Saccc_c](https://x.com/Saccc_c) | — | [一句话指令](https://xianyu110.github.io/awesome-fable-5.5/#2105913312072577218) |
| <a href="https://x.com/voltwake/status/2105884775982485642"><img src="https://upload.maynor1024.live/file/1791037706923_u_2105884775982485642.jpg" width="160" alt="先过 Tibo 测试，再给自己的网站做上线宣传片"></a> | [先过 Tibo 测试，再给自己的网站做上线宣传片](https://x.com/voltwake/status/2105884775982485642) | Fable 5.5 | [@voltwake](https://x.com/voltwake) | 1:03 | — |
| <a href="https://x.com/8Avalon8/status/2106081118869156150"><img src="https://upload.maynor1024.live/file/1791037708780_u_2106081118869156150.jpg" width="160" alt="ESP32 史莱姆桌宠宣传片：Blender 渲染 + 固件合成器配乐"></a> | [ESP32 史莱姆桌宠宣传片：Blender 渲染 + 固件合成器配乐](https://x.com/8Avalon8/status/2106081118869156150) | Fable 5.5（固件 Opus 5.5） | [@8Avalon8](https://x.com/8Avalon8) | 1:42 | — |

## 玩法技巧

1. **先试极简提示词**：一句 `please make a cool animation` 往往就能出完整短片。
2. **两步法**：先搭 3D 场景或交互页面，再让它导出一段 1 分钟视频。
3. **开放式提问看审美**：`If I asked you to blow my mind, what would you make?`
4. **给参考素材**：上传参考视频、歌曲和歌词，做发布片或歌词 MV 更稳。
5. **倒计时打磨**：在 Claude Code 里让它起 10 分钟计时任务，要求用满时间再交付。
6. **老提示词重跑**：把在 5.1 / Opus 上用过的提示词原样再跑，就是最直观的新旧对比。
7. **算好额度**：有人一次约 30 分钟的视频测试用掉 Pro x5 档约 7% 周额度；先用 Opus / Sonnet 打草稿，再交给 Fable 精修。

## 数据

全部条目在 [`cases.json`](cases.json)，在线画廊直接读取这个文件。每条包含：`id`、`category`、`model`、中英文标题、中文简介、作者与原帖链接、发布时间（UTC+8）、时长、点赞 / 浏览 / 收藏、公开提示词、试玩链接、预览图 `cover`（以及部分条目的动图 `preview_gif`）和画廊锚点 `gallery_url`。

想补充新案例：编辑 `scripts/cases_src.py` 后运行 `python3 scripts/build.py`，会同时生成 README 和 `cases.json`，然后提 PR。

## 更正与下架

- 所有作品（视频、代码、图片、提示词）的版权归原作者所有；本仓库的中文标题和简介为自行撰写，预览图仅用于识别作品。
- 如果你是作者，想修改信息、换图或移除条目，直接[提交 Issue](https://github.com/xianyu110/awesome-fable-5.5/issues)，会尽快处理。
- 仓库代码（`index.html`、`scripts/`）使用 [MIT License](LICENSE)。本项目为社区整理，与 Anthropic 无关。

## Claude 国内使用方法

- 方法一：Claude 国内镜像站 👉 [https://claude-opus.top/](https://claude-opus.top/)
- 方法二：tryallapi 一站式 API（Claude / GPT / Gemini）👉 [https://tryallapi.com/register?aff=5A6A](https://tryallapi.com/register?aff=5A6A)

---

由 **MaynorAI** 整理。我是 MaynorAI 团队，分享 AI 编程、AI SaaS 工具出海、一人团队搭建经验。
