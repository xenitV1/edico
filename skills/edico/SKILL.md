---
name: edico
description: Persistent Knowledge Base. Sentezlenen web araştırmalarını gelecekteki konuşmalar için yerel bir JSONL dosyasına kaydeder.
---
<domain_overview>
# 📚 EDICO: PERSISTENT WEB RESEARCH
> **Philosophy:** Bilgi tek seferlik olmamalıdır. Bu yetenek, web aramaları ve okuma işlemlerinden elde edilen verileri kalıcı hale getirerek agent'ın "uzun süreli hafızasını" oluşturur.
</domain_overview>

<iron_laws>
## 🚨 IRON LAWS
```
1. NO RAW DATA DUMPS - Veriler her zaman sentezlenmeli ve özetlenmelidir.
2. NO DUPLICATE TOPICS - Aynı konu üzerine yapılan yeni araştırmalar önceki verileri tamamlamalıdır.
3. CONCISE JSONL - Dosya boyutu ve okunabilirlik için tek satırlık JSON formatı korunmalıdır.
```
</iron_laws>

<protocols>
## 📦 PROTOCOL 1: DATA SYNTHESIS
Agent, web araştırması bittikten sonra şu adımları izlemelidir:
1. **Sentezle**: Ham metinleri anahtar noktalar, kaynaklar ve kategorilere ayır.
2. **Yapılandır**: Veriyi şu JSON şemasına uyarla:
   ```json
   {
     "timestamp": "ISO-8601",
     "topic": "Konu Başlığı",
     "summary": "Sentezlenmiş Özet",
     "sources": ["URL1", "URL2"],
     "tags": ["etiket1", "etiket2"]
   }
   ```
3. **Kaydet**: `persist.py` scriptini kullanarak veriyi yerel veritabanına ekle.

## ⚙️ PROTOCOL 2: STORAGE COMMAND
Veriyi kaydetmek için şu komutu çalıştırın:
`python skills/edico/scripts/persist.py --topic "[KONU]" --summary "[OZET]" --sources "[URL1],[URL2]" --tags "[TAG1],[TAG2]"`
</protocols>

<usage_guidelines>
## 🛠️ USAGE
- Agent, `/edico` komutu geldiğinde veya önemli bir araştırma tamamlandığında bu yeteneği devreye almalıdır.
- Veritabanı varsayılan olarak `~/.webdata/research_log.jsonl` yolunda saklanır.
</usage_guidelines>
