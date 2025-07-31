# TaskTracker

[![CI](https://img.shields.io/badge/CI-pending-lightgrey)](#) <!-- Replace with actual GitHub Actions badge after CI passes -->
[![Coverage](https://img.shields.io/badge/coverage---%25-lightgrey)](#) <!-- Optional: replace with real coverage badge if added -->

## 🚀 Proje Açıklaması

**TaskTracker**, küçük ekipler için görev yönetimi sağlayan gerçekçi bir RESTful API'dir. Bu proje aynı zamanda DevOps yeteneklerini sergilemek için tasarlandı: containerization, test otomasyonu, CI, ileride monitoring ve alerting gibi bileşenler entegre edilebilir.

---

## 🛠️ Özellikler

### API Özellikleri
- **Görev oluşturma:** `POST /tasks` ile yeni görev ekleme.  
- **Görev listeleme:** `GET /tasks` ile tüm görevleri çekme.  
- **Görev tamamlama:** `PATCH /tasks/<id>/complete` ile görevi tamamlandı olarak işaretleme.  
- **Görev silme:** `DELETE /tasks/<id>` ile görev silme.  
- **Health check:** `GET /health` ile uygulamanın çalışır durumda olup olmadığını kontrol etme.  

### DevOps / Altyapı Özellikleri
- **Containerization:** Dockerfile ile uygulama imajı tanımlandı.  
- **Ortamda çalıştırma:** `docker-compose.yml` ile kolay lokal çalıştırma.  
- **Test otomasyonu:** Pytest ile CRUD operasyonlarını ve health check’i kapsayan testler yazıldı.  
- **CI pipeline:** GitHub Actions ile push üzerine testlerin koşulduğu pipeline kuruldu.  
- **Geçici veritabanı testi:** Testler için dosya bazlı geçici SQLite DB (tmp_path) kullanılıyor, in-memory’in izolasyon sorunları aşılmış oldu.  

### Geliştirme ve Kalite Planlanan / Gelecek
- Test coverage raporu  
- Kod kalitesi araçları (black, isort, flake8)  
- pre-commit hook ile commit öncesi otomatik kontrol ve formatlama  
- Structured logging (örneğin JSON formatında)  
- Docker içinde healthcheck  
- Monitoring: Prometheus + Grafana  
- Alerting: Slack / Alertmanager  
- Canlıya alma: Terraform + AWS EC2 (opsiyonel)

---

## 🧩 Mimari Özeti

- **Backend:** Flask  
- **Veri:** SQLite (testlerde geçici dosya bazlı)  
- **Containerization:** Docker + Docker Compose  
- **CI:** GitHub Actions  
- **(İleride)** Monitoring: Prometheus + Grafana  
- **(İleride)** Alerting: Slack + Alertmanager  
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
- [ ] **Kod kalitesi araçları entegre edilecek** (`black`, `isort`, `flake8`)
- [ ] **pre-commit hook kurulacak** (otomatik formatlama ve kontrol)
- [ ] **Structured logging eklenecek** (örneğin `python-json-logger`)
- [ ] **Docker container’a healthcheck tanımı yapılacak**
- [ ] **Monitoring kurulacak** (Prometheus + Grafana ile)
- [ ] **Alert sistemi eklenecek** (Slack + Alertmanager ile bildirim)
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
