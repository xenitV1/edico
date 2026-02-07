---
name: edico
description: Core Knowledge Management Skill. Reduces research redundancy and provides autonomous long-term memory by persisting synthesized web data.
---
<domain_overview>
# 📚 EDICO: PERSISTENCE & REDUNDANCY REDUCTION
> **MISSION:** Antigravity Agent'ın gereksiz web aramalarını durdurmak ve öğrenilenleri kalıcı bir kolektif hafızaya dönüştürmek.
> **Philosophy:** Knowledge should be cumulative, not ephemeral. Edico is the bridge between conversations, ensuring that once a topic is researched, it remains accessible forever.
</domain_overview>

<iron_laws>
## 🚨 IRON LAWS
```
1. CHECK BEFORE SEARCH - Herhangi bir derin web araştırmasına başlamadan ÖNCE yerel .webdata'yı tara.
2. NO REDUNDANCY - Eğer veritabanındaki bilgi taze (2 aydan yeni) ise, yeni bir arama yapma; mevcut veriyi kullan.
3. AUTONOMOUS PERSISTENCE - /edico tetiklendiğinde kullanıcıya onay sormadan sentezle ve kaydet.
4. QUALITY OVER QUANTITY - Ham veri dökümü yapma; sadece "beyin yakan" sentezlenmiş bilgiyi sakla.
```
</iron_laws>

<protocols>
## 📦 PROTOCOL 1: "CHECK-FIRST" TRIGGER
Every time a user asks for research or a new topic is introduced:
1.  **Search Local DB**: Use keywords to check `~/.webdata/research_log.jsonl`.
2.  **Evaluate Freshness**: If found and < 2 months old, use it as the primary source.
3.  **Optimize Search**: Only search the web for *missing* details or updates.

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
