# Go_score

# chạy local
## Tạo môi trường ảo
```bash
python -m venv venv
source venv/Scripts/activate
```
## Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```
## Tạo database
```bash
python manage.py makemigrations 
python manage.py migrate
```
## Import data
```bash
python manage.py import_score diem_thi_thpt_2024.csv
```
## Chạy server
```bash
python manage.py runserver
```

# chạy Docker
## Tạo database và import data
```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py import_score diem_thi_thpt_2024.csv
```
## Build và chạy Docker
```bash
docker-compose build
docker-compose up
```

