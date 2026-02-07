# Edico: Persistent AI Knowledge Base

Edico is a Google Antigravity skill designed to provide long-term memory for AI-driven web research. 

## 🚀 Overview
Normally, research results are lost between AI conversations. Edico solves this by:
1. Synthesizing web search results into concise summaries.
2. Appending them to a local `research_log.jsonl` file.
3. Making historical data accessible to future AI sessions.

## 📁 Installation
To use this skill locally:
1. Copy the `skills/edico` folder to your Antigravity skills directory (usually `~/.gemini/antigravity/skills/`).
2. Copy the `.agent/workflows/edico.md` to your workspace's workflow directory.

## 🛠️ Usage
Trigger the synthesis and storage manually or via the slash command:
- **Slash Command**: `/edico`
- **Manual**: Use the `edico` skill protocols defined in `SKILL.md`.

## 💾 Storage
All data is stored in line-delimited JSON (JSONL) at:
`~/.webdata/research_log.jsonl`
