# 🛡️ CyberSecurity Projects

<div align="center">

![OakAcademy](https://img.shields.io/badge/OakAcademy-13.Batch_Siber_Güvenlik_Mühendisliği-6C47FF?style=for-the-badge&logo=bookstack&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge)

> **OakAcademy 13. Batch Siber Güvenlik Mühendisliği Kariyer Kursu kapsamında**
> **gerçekleştirilen proje çalışmaları ve raporları.**

[![TryHackMe](https://img.shields.io/badge/TryHackMe-BY--EKREM-212C42?style=flat-square&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/BY-EKREM)
[![GitHub](https://img.shields.io/badge/GitHub-ekremtunckir35-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ekremtunckir35)

</div>

---

## 📁 Projeler

| # | Proje | Teknoloji | Tarih | Durum |
|---|-------|-----------|-------|-------|
| 01 | [EDR — Sophos Endpoint Detection & Response](#-proje-01--sophos-edr-yönetimi) | Sophos Central, EDR, DLP, Zero Trust | Nisan 2026 | ✅ Tamamlandı |

---

## 🔐 Proje 01 — Sophos EDR Yönetimi

<div align="center">

![Sophos](https://img.shields.io/badge/Sophos-EDR-0073CF?style=for-the-badge&logo=sophos&logoColor=white)
![Zero Trust](https://img.shields.io/badge/Zero_Trust-Security-E84545?style=for-the-badge)
![Windows](https://img.shields.io/badge/Windows-Endpoint-0078D4?style=for-the-badge&logo=windows&logoColor=white)

</div>

### 📋 Proje Bilgileri

| Parametre | Değer |
|-----------|-------|
| Proje Adı | Sophos EDR Sisteminin Zero Trust Güvenlik Politikaları ile Kurulumu ve Yönetimi |
| Süre | 2 Nisan 2026 – 10 Nisan 2026 (9 Gün) |
| Platform | Sophos Central (cloud.sophos.com) |
| Test Cihazı | Std12 — IP: 10.10.200.22 |
| Toplam Endpoint | 21 Windows Endpoint |
| Rapor Tarihi | 11 Nisan 2026 |

---

### 🎯 Proje Hedefleri

```
✅ Sophos EDR ajanının 21 Windows endpoint'e dağıtımı
✅ Zero Trust tabanlı Threat Protection politikası
✅ Web Control politikası (Kumar, Sosyal Ağlar, P2P engelleme)
✅ Application Control politikası (TeamViewer, uTorrent engelleme)
✅ DLP politikası (TC Kimlik No, Kredi Kartı sızıntı engeli)
✅ EICAR test dosyası ile malware engelleme doğrulaması
✅ Admin Isolation ile endpoint izolasyonu
✅ Live Query ile proaktif tehdit avcılığı
```

---

### 📊 Aşama 1 — Dağıtım ve Temel Politikalar

#### 1.1 Ajan Dağıtımı

| Bilgi | Değer |
|-------|-------|
| Platform | Sophos Central (cloud.sophos.com) |
| Agent Sürümü | Core Agent 2025.2.3.8.0 / Sophos Intercept X 2024.1.2.1.0 |
| Agent Modu | XDR (Extended Detection & Response) |
| Toplam Cihaz | 21 Windows Endpoint (Online) |
| Tamper Protection | Aktif |
| Heartbeat Durumu | Yeşil (Aktif) |

#### 1.2 Threat Protection Politikası

**Politika:** `Custom Threat Protection grup2` — Güncelleme: 2 Nisan 2026

| Özellik | Durum | Açıklama |
|---------|-------|----------|
| Live Protection | ✅ AKTİF | SophosLabs ile anlık tehdit doğrulama |
| Deep Learning (ML) | ✅ AKTİF | Yapay zeka tabanlı malware tespiti |
| Real-time Scanning | ✅ AKTİF | Yerel dosyalar ve ağ paylaşımları |
| CryptoGuard | ✅ AKTİF | Ransomware dosya şifreleme engeli |
| MBR Ransomware | ✅ AKTİF | Boot record saldırıları engeli |
| Exploit Prevention | ✅ AKTİF | Browser, Java, Office, Media koruması |
| Process Hollowing | ✅ AKTİF | Bellek tabanlı saldırı engeli |
| Credential Theft | ✅ AKTİF | Kimlik bilgisi hırsızlığı engeli |
| AMSI Protection | ✅ AKTİF | PowerShell/script tabanlı tehdit engeli |
| C2 Beacon Engelleme | ✅ AKTİF | Command & Control sunucu bağlantısı engeli |
| Adaptive Attack Protection | ✅ AKTİF | Saldırı anında otomatik sıkıştırma |
| Threat Graph | ✅ AKTİF | Saldırı zinciri görselleştirme |

#### 1.3 Web Control Politikası

**Politika:** `WC-STD12-WebControl`

| Test Sitesi | Kategori | Sophos Tepkisi | Sonuç |
|-------------|----------|----------------|-------|
| betsson.com | Gambling | Website Blocked | ✅ ENGELLENDİ |
| facebook.com | Blogs & Forums | Website Blocked | ✅ ENGELLENDİ |
| instagram.com | Blogs & Forums | Website Blocked | ✅ ENGELLENDİ |
| utorrent.com | Peer-to-Peer | Website Blocked | ✅ ENGELLENDİ |

**Haftalık Web Kontrol Raporu (Son 7 Gün):**

| Engellenen Kategori | Ziyaret Sayısı | Benzersiz Kullanıcı |
|--------------------|----------------|---------------------|
| Streaming Media | 1127 | 14 |
| Shopping | 67 | 1 |
| Chat | 42 | 2 |
| Blogs & Forums | 9 | 2 |
| Peer-to-Peer | 5 | 1 |
| Gambling | 2 | 1 |
| Proxies & Translators | 1 | 1 |

---

### 📊 Aşama 2 — Zero Trust İleri Seviye Politikalar

#### 2.1 Application Control

**Politika:** `AC-STD12-ApplicationControl`

| Uygulama | Kategori | Eylem | Neden |
|----------|----------|-------|-------|
| TeamViewer | Remote Management Tool | 🚫 BLOCK | Yetkisiz uzaktan erişim riski |
| uTorrent | File Sharing Application | 🚫 BLOCK | P2P malware yayılma vektörü |

#### 2.2 DLP Politikası

**Politika:** `DLP-STD12-Hassas Veri Engelleme`

| Parametre | Değer |
|-----------|-------|
| Kural Adı | Data Upload Block |
| Eylem | Block Transfer |
| Hedef Kanallar | Email Client, Internet Browser, External Processes, Storage |
| Korunan Veriler | TC Kimlik No, Kredi Kartı, Banka Hesap Bilgileri |
| DLP Log Kaydı | `dlp-test.txt` — STD12\\std — 7 Nisan 2026 02:31 — **BLOCKED** |

---

### 📊 Aşama 3 — Tehdit Simülasyonu ve Müdahale

#### 3.1 EICAR Test — Malware Tespit ve Temizleme

| Tarih/Saat | Olay | Dosya | Eylem |
|------------|------|-------|-------|
| 10 Nisan 2026, 15:24 | Malware detected: EICAR-AV-Test | New Text Document.txt | 🔍 TESPİT |
| 10 Nisan 2026, 15:26 | Malware cleaned up: EICAR-AV-Test | New Text Document.txt | 🧹 TEMİZLENDİ |
| 10 Nisan 2026, 15:26 | Malware detected: EICAR-AV-Test | text.txt | 🔍 TESPİT |
| 10 Nisan 2026, 15:27 | Malware cleaned up: EICAR-AV-Test | text.txt | 🧹 TEMİZLENDİ |

#### 3.2 Endpoint İzolasyonu — Admin Isolation

| Parametre | Değer |
|-----------|-------|
| İzolasyon Zamanı | 10 Nisan 2026, 15:34 PM |
| İzolasyon Türü | Admin Isolation (Manuel) |
| Uygulayan | Ekrem Tunçkır |
| İzolasyon Nedeni | EICAR-AV-Test zararlı yazılımı tespit edildi |
| Sophos Central Erişimi | ✅ AKTİF (haberleşme devam etti) |
| Dış Ağ Erişimi | ❌ KESİLDİ |
| İzolasyon Kaldırma | 10 Nisan 2026, 15:39 PM |

#### 3.3 Live Query A — Açık Ağ Bağlantıları

**Sorgu:** `Processes with an open network connection` | Süre: 328ms

| Path | Uzak IP | Port | Değerlendirme |
|------|---------|------|---------------|
| System32\... | 10.81.128.3 | 3389 | ✅ RDP — Normal |
| Program Files\... | 3.69.153.227 | 443 | ✅ Amazon AWS / Sophos Agent |
| Program Files\... | 3.66.205.161 | 443 | ✅ Amazon AWS / Sophos Agent |
| System32\... | 172.211.123.249 | 443 | ✅ Microsoft Servisi — Normal |
| Program Files\... | 8.8.8.8 | 443 | ✅ Google DNS — Normal |
| 0:0 (Kernel) | 8.8.4.4 | 443 | ✅ Google DNS — Normal |

> **Analiz:** Tehdit göstergesi bulunmadı. RDP, Google DNS ve AWS/Sophos agent bağlantıları normal.

#### 3.4 Live Query B — Registry Startup Uygulamaları

**Sorgu:** `Applications in the startup section of the registry` | Süre: 249ms

| Path | Değerlendirme |
|------|---------------|
| cmd.exe (`/q /c del`) | ⚠️ ŞÜPHELİ — EICAR temizleme kalıntısı |
| cmd.exe (`/q /c rmdir`) | ⚠️ ŞÜPHELİ — EICAR temizleme kalıntısı |
| Google Drive | ✅ Normal |
| OneDrive | ✅ Normal |
| Windows Defender | ✅ Normal |
| Sophos Agent | ✅ Normal |

> **Analiz:** cmd.exe kayıtları EICAR temizleme sürecinden kaynaklanmaktadır. Aktif tehdit göstergesi tespit edilmemiştir.

---

### 📄 Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `EDR_Projesi.docx` | Orijinal proje görev tanımı |
| `EDR_Rapor_EkremTunckir.docx` | Tamamlanan proje raporu |

---

## ⚠️ Yasal Uyarı

Bu repo'daki tüm testler **kontrollü eğitim ortamında** ve **izinli sistemlerde** gerçekleştirilmiştir. Gerçek sistemlerde izinsiz uygulama **yasaktır**.

---

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ekremtunçkır)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/BY-EKREM)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ekremtunckir35)

*"Bir sistemi korumak için önce onu anlamak gerekir."*

</div>
