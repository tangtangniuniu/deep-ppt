# deep-ppt

> Input a topic, get an editable, in-depth presentation — no more screenshot-based slides.

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

## Contributing

Contributions welcome! Please open an issue first to discuss what you'd like to change.

## License

MIT
