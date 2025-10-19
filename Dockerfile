# ==== 1. Python bazaviy imiji ====
FROM python:3.12-slim

# Ishchi katalog
WORKDIR /app

# ==== 2. Fayllarni konteynerga ko‘chirish ====
COPY . /app

# ==== 3. Zarur tizim paketlarini o‘rnatish ====
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# ==== 4. Python kutubxonalarini o‘rnatish ====
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ==== 5. Static fayllarni yig‘ish ====
RUN python manage.py collectstatic --noinput

# ==== 6. Serverni ishga tushirish (gunicorn) ====
CMD ["gunicorn", "gps_tracker.wsgi:application", "--bind", "0.0.0.0:8000"]
