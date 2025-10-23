# GeoMap Admin

## Описание
Это Django-приложение для управления интерактивной картой. Через Django admin можно создавать и редактировать точки на карте, указывать их координаты, заголовки, описания и изображения.

## Основные возможности
- Добавлять новые точки на карту через django admin
- Редактировать информацию о точках: название, описание, координаты
- Сортировать изображения с помощью drag & drop прямо в django admin
- Удалять точки и связанные с ними изображения

## Технологии
- Django
- HTML, CSS, JavaScript
- PostgreSQL  
- Docker, Docker Compose  
- CKEditor
- django-admin-sortable2

# URLs проекта
- Главная страница приложения http://34.122.197.212:8000/
- Админка Django http://34.122.197.212:8000/admin/
login - user, password - 123

## Локальная установка и запуск проекта

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Suetosha/django-geomap.git
```

### 2. Создайте .env файл
Пример содержимого .env:
```
DJANGO_SECRET_KEY='django-insecure-$wj2xi#s11rhu@79v3+43e6ezmbf#hp@owamu)hm28^pe1rc-p'

DB_ENGINE=django.db.backends.postgresql
DB_NAME=geomap
DB_USER=postgres
DB_PASSWORD=123
DB_HOST=db
DB_PORT=5432
```

### 3. Запуск через Docker Compose
```bash
docker-compose up -d
```

### 4. Создание django admin superuser через docker контейнер
```
docker exec -it container_id python manage.py createsuperuser
```

### Рекомендации

#### Перед первым запуском убедитесь, что порт 5432 свободен для PostgreSQL.