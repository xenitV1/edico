---
name: edico
description: Core Knowledge Management Skill. Reduces research redundancy and provides autonomous long-term memory by persisting synthesized web data.
---
<domain_overview>
# 📚 EDICO: PERSISTENCE & REDUNDANCY REDUCTION
> **MISSION:** To stop redundant web searches by the AI and transform learned insights into a permanent, collective local memory.
> **Philosophy:** Knowledge should be cumulative, not ephemeral. Edico is the bridge between conversations, ensuring that once a topic is researched, it remains accessible forever.
</domain_overview>

<iron_laws>
## 🚨 IRON LAWS
```
1. CHECK BEFORE SEARCH - Always scan the local .webdata directory BEFORE starting any deep web research.
2. NO REDUNDANCY - If existing data is fresh (less than 2 months old), use it as the primary source instead of performing a new search.
3. AUTONOMOUS PERSISTENCE - When /edico is triggered or research is complete, synthesize and save immediately without asking for user confirmation.
4. QUALITY OVER QUANTITY - Do not save raw data dumps; only persist high-value, synthesized insights.
```
</iron_laws>

<protocols>
## 📦 PROTOCOL 1: "CHECK-FIRST" TRIGGER
Every time a user asks for research or a new topic is introduced:
1.  **Search Local DB**: Use keywords to check `~/.webdata/research_log.jsonl`.
2.  **Evaluate Freshness**: If found and < 2 months old, use it as the primary source.
3.  **Optimize Search**: Only search the web for *missing* details or required updates.

## 📦 PROTOCOL 2: DATA SYNTHESIS & STORAGE (AUTONOMOUS)
When research is completed or `/edico` is called:
1.  **Synthesize**: Contextualize the data (Key points, Sources, Category).
2.  **Execute**: Run `node skills/edico/scripts/persist.js` with structured parameters.
3.  **Silent Success**: The operation must be silent and autonomous unless an error occurs.
</protocols>

<usage_guidelines>
## 🛠️ USAGE
- Use this skill to combat "conversation amnesia."
- Edico is the default memory layer for all web-related research tasks.
</usage_guidelines>
