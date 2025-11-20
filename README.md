# 📘 Django Blog App (Django 5 + PostgreSQL + Docker)


A clean and functional Blog Application built with Django 5, using PostgreSQL for the database and Docker for development.
This project includes all common blog features such as tags, search, comments, and similar post recommendations — plus a fully configured XML sitemap.

# 🚀 Features

 - 📝 Create, edit, delete blog posts

 - 🏷 Tag system for organizing posts and browse by tag

 - 🔍 Search (full-text search)

 - 🤝 Recommended / similar posts (based on shared tags)

 - 💬 Comment system

 - 📨 Share post via email (optional)

 - 🗺 XML Sitemap for SEO

 - 🗄 PostgreSQL database (Dockerized)

 - 🐳 Full Docker support for easy local development

 - 🔐 Environment variables via .env

# 📚 Technologies Used

 - Django 5

 - Python 3

 - PostgreSQL

 - Docker & Docker Compose

---

# 🐳 Running with Docker (Development)
##### 1. Create your .env
```bash
cp .env.example .env
```

##### 2. Build and start
```bash
docker-compose up --build
```
App runs at:

```bash
http://localhost:8000
```

##### 3.Run migrations
```bash
docker-compose exec web python manage.py migrate
```
##### 4.Create admin
```bash
docker-compose exec web python manage.py createsuperuser
```

##### 🛠 Running Locally (Without Docker)
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


