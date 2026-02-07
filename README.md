# Edico: Persistent AI Knowledge Base & Redundancy Guard

Edico is a core architectural expansion for AI agents, designed to solve the problem of "conversation amnesia" and redundant web searching.

## 🎯 The Mission
The primary goal of Edico is to:
1.  **Eliminate Redundancy**: Prevent the AI from performing the same web searches in every new conversation.
2.  **Long-Term Memory**: Act as a persistent, local database of exhaustive analysis that spans across multiple AI sessions.
3.  **Autonomous Grounding**: Provide a reliable, local source of truth that the AI checks *before* reaching out to the live web.

## 📁 Project Structure
- `skills/edico/SKILL.md`: The core logic and "Iron Laws" (Exhaustive Analysis over Summaries).
- `skills/edico/scripts/persist.js`: The storage engine (Node.js) that manages the local JSONL database.
- `workflows/edico.md`: The `/edico` slash command providing a fully autonomous research-persistence pipeline.

## 🚀 How it Works
1.  **Check First**: When a topic is introduced, the agent first scans `~/.webdata/research_log.jsonl`.
2.  **Freshness Check**: If data exists and is less than 2 months old, it's used immediately.
3.  **Exhaustive Analysis**: New research is synthesized into a deep-dive "detailed_analysis" field.
4.  **Source Date**: Records use the actual publication date from the source for historical accuracy.
5.  **Autonomous Save**: The agent persists the new data without interrupting the user.

## 💾 Storage Location
Data is stored as a line-delimited JSON (JSONL) file at:
`~/.webdata/research_log.jsonl`

## 🛠️ Installation
1.  Add the `skills/edico` folder to your skills directory.
2.  Add the `/edico` command to your workspace workflows.
3.  Let the agent handle the rest autonomously.
