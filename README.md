# 从零造物

> 带着现代知识穿越回古代，只用当时能找到的材料，把技术一件件重新造出来；再反过来，用现代原理解开古人早已做到的技艺。每一步都讲清楚：为什么能做成。

一个科普视频系列的完整制作记录：选题、拍摄方案、旁白、按物理公式渲染的原理动画和粗剪样片。

## 在线浏览

**https://bluesky-rgb.github.io/cong-ling-zao-wu/**

所有内容都在网站上看，比在 GitHub 里翻文件方便得多：

| 入口 | 内容 |
| --- | --- |
| [项目首页](https://bluesky-rgb.github.io/cong-ling-zao-wu/) | 总览、视频画廊、各季拍摄本入口 |
| [选题详案](https://bluesky-rgb.github.io/cong-ling-zao-wu/episodes/) | 全部选题和每一季的播出计划 |
| [拍摄总排期与采购清单](https://bluesky-rgb.github.io/cong-ling-zao-wu/shooting/) | 拍摄顺序、要买的道具 |
| [项目全书](https://bluesky-rgb.github.io/cong-ling-zao-wu/plan/) | 定位、方法、科技树、制作流程、风险合规 |
| [发布素材](https://bluesky-rgb.github.io/cong-ling-zao-wu/publish/) | 每集标题、封面文字、简介、竖屏切片脚本 |

## 两条线

- **主线 · 穿越造物**：只用古代的材料，能不能造出 X？（科技树一层层往上长，第 01–191 集）
- **副线 · 古法解密**：古人不懂 X，为什么能做对？（B1–B149）

两条线按「一主一副」轮流排季，每季 10 集 + 1 集特辑。

## 仓库里有什么

```
README.md      本页
docs/          整个网站（GitHub Pages 从这里发布）
  ep01/ … ep191/     主线每集的拍摄本
  b1/ … b149/        副线每集的拍摄本
  season1/ … 35/     每季特辑
  media/             渲染好的视频和封面
  decisions.md       决定记录；journey.md 探索历程；sources.md 资料来源
source/        渲染全部动画和粗剪的 Python 源码
```

## 重新渲染视频

需要 Python 3、Pillow、ffmpeg 和 Noto CJK 字体。

```bash
cd source/video
python3 shot10.py            # 输出 MP4
python3 shot10.py 8          # 只渲染第 8 秒的一帧预览
```

## 原则

- 实验镜头必须实拍；原理动画用代码按公式渲染；AI 视频只用于氛围镜头，发布时标注。
- 每个史实都附来源，拿不准的标「拍摄前核对」，数值标「以实测为准」。
- 涉及明火、高温、强磁铁、激光的实验只由成年人操作；危险内容只做动画。
