# 🛡️ CyberSecurity Projects

<div align="center">

![OakAcademy](https://img.shields.io/badge/OakAcademy-13.Batch_Siber_Güvenlik_Mühendisliği-6C47FF?style=for-the-badge&logo=bookstack&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge)
![Projects](https://img.shields.io/badge/Projeler-3%2F16+-00C853?style=for-the-badge)

> **OakAcademy 13. Batch Siber Güvenlik Mühendisliği Kariyer Kursu kapsamında**
> **gerçekleştirilen proje çalışmaları ve raporları.**

[![TryHackMe](https://img.shields.io/badge/TryHackMe-BY--EKREM-212C42?style=flat-square&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/BY-EKREM)
[![OakAcademy](https://img.shields.io/badge/OakAcademy-Cyber_Security_Engineer-6C47FF?style=flat-square&logo=bookstack&logoColor=white)](https://oakacademy.de/en/)
[![GitHub](https://img.shields.io/badge/GitHub-ekremtunckir35-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ekremtunckir35)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ekremtunçkır)

</div>

---

## 📁 Proje Listesi

| # | Proje | Teknoloji | Süre | Sonuç |
|---|-------|-----------|------|-------|
| 01 | [🔐 EDR — Sophos Endpoint Detection & Response](./01-EDR-Sophos/) | Sophos Central, XDR, DLP, Zero Trust | Nisan 2026 (9 gün) | ✅ Tamamlandı |
| 02 | [🔥 Firewall — FortiGate Güvenlik Politikası](./02-FortiGate-Firewall/) | FortiGate, IPS, Web Filter, App Control | Nisan 2026 (~2 hafta) | ✅ Tamamlandı |
| 03 | [🔍 Vulnerability Management — Nmap & Nessus](./03-Vulnerability-Management/) | Nmap NSE, Tenable Nessus, CVSS, VPR, EPSS | Nisan 2026 (5 gün) | ✅ Tamamlandı |
| 04 | 🔜 Yakında | - | - | ⏳ |

---

## 🔐 Proje 01 — Sophos EDR

<div align="center">

![Sophos](https://img.shields.io/badge/Sophos-EDR-0073CF?style=for-the-badge&logo=sophos&logoColor=white)
![Zero Trust](https://img.shields.io/badge/Zero_Trust-Security-E84545?style=for-the-badge)
![Tasks](https://img.shields.io/badge/Tasks-8%2F8_Tamamlandı-00C853?style=for-the-badge)

</div>

**Kurs:** OakAcademy 13. Batch | **Süre:** 9 gün | **Platform:** Sophos Central

| Performans | Sonuç |
|-----------|-------|
| TryHackMe Rooms | ✅ %100 |
| CTF Tamamlama | ✅ %100 |
| Quiz Ortalaması | 94 / 100 |
| Modül Sınavı | 93 / 100 |

**Uygulanan Güvenlik Katmanları:**

```
✅ Threat Protection  — Deep Learning ML, CryptoGuard, Exploit Prevention
✅ Web Control        — Kumar, P2P, Sosyal Ağlar engelleme
✅ Application Control — TeamViewer, uTorrent engelleme
✅ DLP                — TC Kimlik No, Kredi Kartı sızıntı engeli
✅ EICAR Test         — Malware tespit & temizleme doğrulaması
✅ Admin Isolation    — Endpoint ağdan izole etme
✅ Live Query         — Proaktif tehdit avcılığı (ağ bağlantıları + Registry)
```

📂 [Proje Detayları ve Raporlar →](./01-EDR-Sophos/)

---

## 🔥 Proje 02 — FortiGate Firewall

<div align="center">

![FortiGate](https://img.shields.io/badge/FortiGate-Firewall-EE3124?style=for-the-badge&logo=fortinet&logoColor=white)
![Least Privilege](https://img.shields.io/badge/Least_Privilege-Zero_Trust-E84545?style=for-the-badge)
![Tasks](https://img.shields.io/badge/Tasks-16%2F16_Tamamlandı-00C853?style=for-the-badge)

</div>

**Kurs:** OakAcademy 13. Batch | **Süre:** ~2 Hafta | **Platform:** FortiGate VM — FortiOS

**Ağ Segmentasyonu:**

```
Finance Subnet  ──┐
Sales Subnet    ──┤──▶  FortiGate FW  ──▶  WAN / İnternet
IT Subnet       ──┤         │
DMZ (WinSrv)   ──┘    Least Privilege
```

**Tamamlanan 16 Task:**

```
✅ Task 01 — Linux SSH & ICMP erişimi (subnet içi)
✅ Task 02 — Windows RDP erişimi (subnet içi)
✅ Task 03 — Log kayıtlarıyla doğrulama
✅ Task 04 — Web sunucusu kurulumu + LAN erişimi (80, 8080, 9090)
✅ Task 05 — Virtual-IP / Port Forwarding
✅ Task 06 — LAN1 & LAN2 internet erişimi (NAT)
✅ Task 07 — LAN1 kısıtlı internet (URL Filter)
✅ Task 08 — LAN2 AWS engelleme (FQDN Filter)
✅ Task 09 — Uygulama kontrolü (Instagram, Gmail, Facebook engel)
✅ Task 10 — Web Filtering (kategori bazlı)
✅ Task 11 — Antivirus (EICAR testi)
✅ Task 12 — IPS (Intrusion Prevention System)
✅ Task 13 — DNS Filtering
✅ Task 14 — DMZ Windows Server politikası
✅ Task 15 — Linux web sunucusu log izleme
✅ Task 16 — Genel güvenlik politikası ve özet
```

📂 [Proje Detayları ve Raporlar →](./02-FortiGate-Firewall/)

---

## 📊 Genel İlerleme

```
Tamamlanan Projeler : 3
Toplam Task/Aşama   : 8 (EDR) + 16 (Firewall) + 9 (VM) = 33 görev
Başarı Oranı        : %100
Devam Eden Kurs     : OakAcademy 13. Batch — Security Module ⏳
```

---

## 🔍 Proje 03 — Vulnerability Management

<div align="center">

![Nessus](https://img.shields.io/badge/Tenable_Nessus-Professional-00C176?style=for-the-badge&logo=tenable&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-NSE_Scripts-0E83CD?style=for-the-badge)
![Tasks](https://img.shields.io/badge/Aşama-9%2F9_Tamamlandı-00C853?style=for-the-badge)

</div>

**Kurs:** OakAcademy 13. Batch | **Süre:** 5 gün | **Hedefler:** Windows 10, Linux Ubuntu, Metasploitable

**Tamamlanan 9 Aşama:**

```
✅ Aşama 1 — Topoloji ve hedef tanımlama (Nmap)
✅ Aşama 2-4 — Manuel port/servis/OS tarama + NSE vulnerability scriptleri
               → 31 TCP + 7 UDP açık port | 9 CVE | 3 zayıf kimlik doğrulama
✅ Aşama 5 — Nessus Kimliksiz Tarama → 45 bulgu (7 Critical, 7 High)
✅ Aşama 6 — Nessus Kimlikli Tarama  → 167 bulgu (30 Critical, 97 High)
✅ Aşama 7 — Karşılaştırma: Kimlikli tarama %271 daha fazla bulgu tespit etti
✅ Aşama 8 — Windows Authentication Failed simulasyonu + 9 neden analizi + çözüm
✅ Aşama 9 — Kapsamlı rapor hazırlama
```

**Risk Skorlama Sistemleri:**

| Sistem | Sorusu |
|--------|--------|
| CVSS v3.0 | "Bu zafiyet ne kadar şiddetli?" |
| VPR (Tenable) | "Önümüzdeki 28 günde önce neyi düzeltmeliyim?" |
| EPSS | "Bu zafiyet 30 günde istismar edilecek mi?" |

**Kimliksiz vs Kimlikli Tarama Karşılaştırması:**

| Metrik | Kimliksiz | Kimlikli | Artış |
|--------|-----------|----------|-------|
| Toplam Bulgu | 45 | 167 | **+271%** |
| Critical | 7 | 30 | **+329%** |
| High | 7 | 97 | **+1.286%** |

📂 [Proje Detayları ve Rapor →](./03-Vulnerability-Management/)

---

## 🛠️ Kullanılan Teknolojiler

![Sophos](https://img.shields.io/badge/Sophos-EDR-0073CF?style=flat-square&logo=sophos&logoColor=white)
![FortiGate](https://img.shields.io/badge/FortiGate-Firewall-EE3124?style=flat-square&logo=fortinet&logoColor=white)
![Nessus](https://img.shields.io/badge/Tenable_Nessus-Professional-00C176?style=flat-square)
![Nmap](https://img.shields.io/badge/Nmap-NSE-0E83CD?style=flat-square)
![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?style=flat-square&logo=tryhackme&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

---

## ⚠️ Yasal Uyarı

Tüm projeler **kontrollü eğitim ortamında** ve **izinli sistemlerde** gerçekleştirilmiştir.
Hassas bilgiler (IP adresleri, cihaz adları, ağ topolojisi) `[REDACTED]` ile gizlenmiştir.

---

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ekremtunçkır)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/BY-EKREM)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ekremtunckir35)

*"Bir sistemi korumak için önce onu anlamak gerekir."*

</div>
