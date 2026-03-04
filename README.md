# deep-ppt

> Input a topic, get an editable, in-depth presentation — no more screenshot-based slides.
>
> 输入一个主题，获得可编辑的深度分析演示文稿 —— 告别截图式PPT。

[English](#the-problem) | [中文](#问题)

---

## The Problem

Engineers spend hours on technical research presentations:
1. **Research** — scattered across docs, papers, and articles
2. **Analyze** — synthesize findings into a coherent narrative
3. **Build slides** — manually create PPT, fight with layouts

Existing AI tools (NotebookLM) generate slides as **images with garbled text** — you can't edit them, and the analysis is shallow.

## The Solution

**deep-ppt** takes a topic and produces a fully **editable .pptx** file with deep, structured analysis:

```bash
pip install deep-ppt
deep-ppt generate "Kubernetes vs Docker Swarm for microservices"
```

Output: a 20+ page editable PowerPoint with:
- Deep technical analysis (not surface-level bullet points)
- Clean, professional layouts
- Editable text (no garbled image-based slides)
- Speaker notes for each slide

## How It Works

```
Topic → NotebookLM API (base analysis)
      → Agent Loop (deep-dive research, gap analysis, synthesis)
      → PPTX Engine (editable slides with professional layouts)
      → your_presentation.pptx
```

## Quick Start

```bash
# Install
pip install deep-ppt

# Generate a presentation
deep-ppt generate "Your Topic Here"

# Generate with options
deep-ppt generate "Your Topic" --pages 30 --lang zh --output slides.pptx
```

## Comparison

| Feature | deep-ppt | NotebookLM | Manual PPT |
|---------|----------|------------|------------|
| Analysis Depth | Deep (multi-step AI) | Shallow | Depends on you |
| Output Format | Editable .pptx | Image (not editable) | Editable .pptx |
| Text Quality | Clean, correct | Garbled/typos | Clean |
| Time to Create | Minutes | Minutes | Hours |
| Customizable | Yes | No | Yes |

## Roadmap

- [x] Project setup
- [ ] NotebookLM API integration
- [ ] Agent Loop deep analysis pipeline
- [ ] PPTX generation engine
- [ ] CLI interface
- [ ] pip package distribution
- [ ] Template system

---

## 问题

工程师在技术预研演示上花费大量时间：
1. **查资料** —— 散落在各种文档、论文和文章中
2. **做分析** —— 将零散发现梳理成连贯的叙述
3. **做PPT** —— 手动创建幻灯片，和排版搏斗

现有的AI工具（如NotebookLM）生成的幻灯片是**图片格式，文字乱码严重** —— 无法编辑，分析深度也不够。

## 解决方案

**deep-ppt** 输入一个主题，输出一份完全**可编辑的 .pptx** 文件，包含深度结构化分析：

```bash
pip install deep-ppt
deep-ppt generate "微服务架构中Kubernetes与Docker Swarm的对比分析"
```

输出：一份20页以上可编辑的PowerPoint，包含：
- 深度技术分析（不是敷衍的要点罗列）
- 专业排版布局
- 可编辑的纯文本（没有图片乱码）
- 每页附带演讲者备注

## 工作原理

```
主题 → NotebookLM API（基础分析）
     → Agent Loop（深度研究、知识缺口分析、内容综合）
     → PPTX 引擎（可编辑幻灯片 + 专业排版）
     → 你的演示文稿.pptx
```

## 快速开始

```bash
# 安装
pip install deep-ppt

# 生成演示文稿
deep-ppt generate "你的主题"

# 带参数生成
deep-ppt generate "你的主题" --pages 30 --lang zh --output 演示文稿.pptx
```

## 功能对比

| 特性 | deep-ppt | NotebookLM | 手动做PPT |
|------|----------|------------|----------|
| 分析深度 | 深度（多步AI分析） | 浅层 | 取决于你 |
| 输出格式 | 可编辑 .pptx | 图片（不可编辑） | 可编辑 .pptx |
| 文字质量 | 清晰无误 | 乱码/错字 | 清晰无误 |
| 生成时间 | 分钟级 | 分钟级 | 数小时 |
| 可定制 | 是 | 否 | 是 |

## 路线图

- [x] 项目搭建
- [ ] NotebookLM API 集成
- [ ] Agent Loop 深度分析管线
- [ ] PPTX 生成引擎
- [ ] 命令行界面
- [ ] pip 包发布
- [ ] 模板系统

---

## Contributing

Contributions welcome! Please open an issue first to discuss what you'd like to change.

欢迎贡献！请先开一个issue讨论你想改什么。

## License

MIT
