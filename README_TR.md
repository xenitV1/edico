# Edico: Kalıcı Yapay Zeka Bilgi Tabanı ve Tekrar Koruyucu

Edico, yapay zeka agent'ları için geliştirilmiş, "konuşma amnezisi" (oturumlar arası unutkanlık) ve gereksiz web araması sorunlarını çözen temel bir mimari eklentidir.

## 🎯 Misyon
Edico'nun birincil hedefleri şunlardır:
1.  **Tekrarı Ortadan Kaldırmak**: Yapay zekanın her yeni konuşmada aynı web aramalarını tekrar yapmasını engellemek.
2.  **Kapsamlı Analiz**: Basit bir özet yerine, başka bir araştırmaya gerek bırakmayacak kadar detaylı, kalıcı ve yerel bir bilgi veritabanı oluşturmak.
3.  **Otonom Doğrulama**: Yapay zekanın canlı web'e erişmeden önce kontrol edeceği güvenilir, yerel bir "tek gerçek kaynak" sağlamak.

## 📁 Proje Yapısı
- `skills/edico/SKILL.md`: Agent'ın hafıza davranışını yöneten temel mantık ve "Katı Kurallar" (Özet yerine Kapsamlı Analiz).
- `skills/edico/scripts/persist.js`: Yerel JSONL veritabanını yöneten depolama motoru (Node.js).
- `workflows/edico.md`: Tam otonom bir araştırma-kalıcılık hattı sağlayan `/edico` slash komutu tanımı.

## 🚀 Nasıl Çalışır?
1.  **Önce Kontrol Et**: Bir konu tanıtıldığında, agent önce `~/.webdata/research_log.jsonl` dosyasını tarar.
2.  **Tazelik Kontrolü**: Veri mevcutsa ve 2 aydan yeniyse, doğrudan kullanılır.
3.  **Kapsamlı Analiz**: Yeni araştırmalar, "özet" (summary) değil, derinlemesine bir "ayrıntılı analiz" (detailed_analysis) olarak sentezlenir.
4.  **Kaynak Bazlı Tarih**: Kayıtlar, bugünün tarihi yerine kaynaklarda belirtilen (makale yayın tarihi vb.) gerçek tarihlerle saklanır.
5.  **Otonom Kayıt**: Agent, kullanıcıyı bölmeden verileri otomatik olarak kalıcı hale getirir.

## 💾 Depolama Konumu
Veriler, şu konumda satır tabanlı JSON (JSONL) dosyası olarak saklanır:
`~/.webdata/research_log.jsonl`

## 🛠️ Kurulum
1.  `skills/edico` klasörünü yetenekler dizininize ekleyin.
2.  `/edico` komutunu çalışma alanı workflow'larınıza dahil edin.
3.  Geri kalan her şeyi agent'ın otonom olarak halletmesine izin verin.
