# TaskTracker 

[![codecov](https://codecov.io/gh/DumanIbrahm/TaskTracker/branch/main/graph/badge.svg)](https://codecov.io/gh/DumanIbrahim/TaskTracker)
[![codecov](https://codecov.io/gh/DumanIbrahm/reposlug/branch/main/graph/badge.svg?token=TOKEN)](https://codecov.io/gh/kullaniciadi/reposlug)
[![CI](https://img.shields.io/badge/CI-pending-lightgrey)](#) <!-- Replace with actual GitHub Actions badge after CI passes -->
[![Coverage](https://img.shields.io/badge/coverage---%25-lightgrey)](#) <!-- Optional: replace with real coverage badge if added -->

## 🚀 Proje Açıklaması

**TaskTracker**, küçük ekipler için görev yönetimi sağlayan gerçekçi bir RESTful API'dir. Bu proje aynı zamanda DevOps yeteneklerini sergilemek için tasarlandı: containerization, test otomasyonu, CI, monitoring ve alerting gibi bileşenler entegre edildi.

---

## 🛠️ Özellikler

### API Özellikleri
- **Görev oluşturma:** `POST /tasks` ile yeni görev ekleme.  
- **Görev listeleme:** `GET /tasks` ile tüm görevleri çekme.  
- **Görev tamamlama:** `PATCH /tasks/<id>/complete` ile görevi tamamlandı olarak işaretleme.  
- **Görev silme:** `DELETE /tasks/<id>` ile görev silme.  
- **Health check:** `GET /health` ile uygulamanın çalışır durumda olup olmadığını kontrol etme.  
- **Hata senaryosu:** `GET /error` endpoint’i ile hata oluşturulabilir (Loki ile loglanır).

### DevOps / Altyapı Özellikleri
- **Containerization:** Dockerfile ile uygulama imajı tanımlandı.  
- **Ortamda çalıştırma:** `docker-compose.yml` ile kolay lokal çalıştırma.  
- **Test otomasyonu:** Pytest ile CRUD operasyonlarını ve health check’i kapsayan testler yazıldı.  
- **CI pipeline:** GitHub Actions ile push üzerine testlerin koşulduğu pipeline kuruldu.  
- **Logging & Monitoring:** Uygulama logları Promtail ile toplanıp Loki’ye gönderiliyor, Grafana üzerinden takip edilebiliyor.  
- **Alerting:** Grafana üzerinden hatalı loglara göre alert oluşturulabiliyor (`error` log içeriğine göre).  
- **Geçici veritabanı testi:** Testler için dosya bazlı geçici SQLite DB (tmp_path) kullanılıyor, in-memory’in izolasyon sorunları aşılmış oldu.  

---

## 🧩 Mimari Özeti

- **Backend:** Flask  
- **Veri:** SQLite (testlerde geçici dosya bazlı)  
- **Containerization:** Docker + Docker Compose  
- **CI:** GitHub Actions  
- **Monitoring:** Prometheus + Grafana + Loki  
- **Alerting:** Grafana alert kuralları  
- **(İleride)** Canlıya alma: Terraform + AWS EC2  

---

## 📈 İlerlemişlik / Progress

- [x] **Flask ile RESTful API oluşturuldu** (`/tasks`, `/tasks/<id>/complete`, `/health`, vs.)
- [x] **SQLite veritabanı entegrasyonu yapıldı** (dosya bazlı test DB ile çalışıyor)
- [x] **Pytest ile testler yazıldı** (task ekleme, tamamlama, silme, health check dahil)
- [x] **Dockerfile yazıldı** (Flask uygulaması için)
- [x] **docker-compose.yml eklendi** (uygulama kolayca ayağa kaldırılabiliyor)
- [x] **GitHub Actions CI pipeline kuruldu** (push üzerine testler koşuyor)
- [ ] **Test coverage raporu eklenecek**
- [x] **Kod kalitesi araçları entegre edildi** (`black`, `isort`, `flake8`)
- [x] **pre-commit hook kuruldu** (otomatik formatlama ve kontrol)
- [ ] **Structured logging eklenecek** (örneğin `python-json-logger`)
- [ ] **Docker container’a healthcheck tanımı yapılacak**
- [x] **Monitoring kuruldu** (Prometheus + Grafana ile)
- [x] **Alert sistemi eklendi** (Slack + Alertmanager yerine şu anlık e-posta)
- [ ] **Canlıya alma yapılacak** (Terraform + AWS EC2 ile deployment)


---

## ⚙️ Hızlı Başlangıç

### Gereksinimler
- Python 3.10+  
- Docker & Docker Compose  
- Git  

### Lokal Geliştirme
```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı çalıştır
python run.py

# Health check
curl http://localhost:5000/health
