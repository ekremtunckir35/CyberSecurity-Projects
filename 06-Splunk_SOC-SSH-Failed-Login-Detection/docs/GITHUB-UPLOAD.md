# GitHub yükleme ve doğrulama kontrol listesi

## 1. Dosyaları aç / içeriği doğrula

- [ ] `README.md` ve 21 ekran görüntüsünü kontrol et.
- [ ] Ekran görüntülerindeki kullanıcı adı, hostname, IP, tarayıcı sekmeleri, URL ve diğer bilgilerin herkese açık paylaşımını onayla.
- [ ] Herhangi bir gerçek parola, token, private key, lisans anahtarı veya kişisel veri olmadığını doğrula.
- [ ] `configs/*.example` dosyalarının yalnızca örnek olduğundan emin ol.
- [ ] `spl/06-scheduled-ssh-detection.spl` sorgusunun uygulanan kural ile örtüştüğünü doğrula.

## 2. GitHub'a gönder

```bash
# Bu komutları SOC-SSH-Failed-Login-Detection klasörü içinde çalıştır
# Git kullanıcı adını/repo adresini kendi hesabına göre belirle.
git init
git add README.md spl/ configs/ evidence/ docs/ .gitignore
git commit -m "Add Splunk SOC SSH detection engineering case study with evidence"
git branch -M main
git remote add origin https://github.com/USERNAME/SOC-SSH-Failed-Login-Detection.git
git push -u origin main
```

**Not:** `USERNAME` örnektir, gerçek uzak depo URL'si otomatik oluşturulmamıştır. Önce GitHub'da boş bir repo açılmalıdır. GitHub'a henüz yükleme yapılmamıştır.

## 3. Test sonrası iyileştirmeler

- [ ] Fields-based throttle: `host`, `src_ip`, `target_user` (5 dk) uygulayıp doğrula.
- [ ] `_time` / `_indextime` farkını ölç.
- [ ] Successful SSH login correlation ekle.
- [ ] Fedora log rotation sonrası ACL kontrol et.
- [ ] `root` yerine dedicated account kullan ve network sınırlarını sıkılaştır.

## 4. Kanıt niteliği

- `evidence/` içindeki PNG dosyaları kullanıcı tarafından sağlanan gerçek ekran görüntüleridir.
- `README.md` içinde gözlem ile yeniden uygulama talimatları ayrılmıştır.
- Tek başına event count = saldırı değil; Trigger History gerçekten otomatik tetikleme kanıtıdır.
