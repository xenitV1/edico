---
name: edico
description: Persistent Knowledge Base. Saves synthesized web research results to a local JSONL file for future conversations.
---
<domain_overview>
# 📚 EDICO: PERSISTENT WEB RESEARCH
> **Philosophy:** Knowledge should not be ephemeral. This skill makes data acquired from web searches and reading operations permanent, creating the agent's "long-term memory."
</domain_overview>

<iron_laws>
## 🚨 IRON LAWS
```
1. NO RAW DATA DUMPS - Data must always be synthesized and summarized.
2. NO DUPLICATE TOPICS - New research on the same topic should complement previous data.
3. CONCISE JSONL - Maintain a single-line JSON format for file size and readability.
```
</iron_laws>

<protocols>
## 📦 PROTOCOL 1: DATA SYNTHESIS
After completing web research, the agent must follow these steps:
1. **Synthesize**: Separate raw text into key points, sources, and categories.
2. **Structure**: Adapt data to the following JSON schema:
   ```json
   {
     "timestamp": "ISO-8601",
     "topic": "Topic Title",
     "summary": "Synthesized Summary",
     "sources": ["URL1", "URL2"],
     "tags": ["tag1", "tag2"]
   }
   ```
3. **Save**: Use the `persist.py` script to add the data to the local database.

## ⚙️ PROTOCOL 2: STORAGE COMMAND
Run the following command to save the data:
`python skills/edico/scripts/persist.py --topic "[TOPIC]" --summary "[SUMMARY]" --sources "[URL1],[URL2]" --tags "[TAG1],[TAG2]"`
</protocols>

<usage_guidelines>
## 🛠️ USAGE
- The agent should activate this skill when the `/edico` command is received or when important research is completed.
- The database is stored by default at `~/.webdata/research_log.jsonl`.
</usage_guidelines>
