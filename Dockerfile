# Python base image
FROM python:3.10-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Flask environment ayarları
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Port aç
EXPOSE 5000

# Uygulamayı çalıştır
CMD ["flask", "run"]
