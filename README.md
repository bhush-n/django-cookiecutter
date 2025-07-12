
# 🚀 Django-Cookiecutter

A production-ready, scalable, and secure Django-based backend.  
Generated with [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django).

> Built with ❤️ by [Bhushan Chaudhari](https://medium.com/@bhushanch45)

## 📦 Features

- ✅ Django 4+ with ASGI support (async-ready)
- 🐳 Docker + Docker Compose support
- 🛡️ Environment-specific settings with `.envs/`
- 📬 Optional integrations: Celery, Redis, Mailgun, Sentry
- 📁 PostgreSQL + Traefik reverse proxy
- 📜 Preconfigured for CI/CD (GitHub Actions, etc.)
- 🖥️ Ready for modern frontends (React, Vue, etc.)

---

## 🧰 Tech Stack

- Python 3.11+
- Django
- PostgreSQL
- Docker & Docker Compose
- Traefik
- Gunicorn (for production)
- Uvicorn (for async/dev)
- Nginx (optional if not using Traefik)

---

## 🚀 Getting Started (Local via Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-cookiecutter.git
cd django-cookiecutter
````

### 2. Set Up Environment Variables

Copy the example environment files:

```bash
cp .envs/.local/.django .env
cp .envs/.local/.postgres .env
```

Make sure to update secrets in `.env`.

---

### 3. Build and Run with Docker

```bash
docker-compose up --build
```

Once it's up, the app should be available at:

```
http://localhost/
```

---

## 🛠 Development Tips

### Access the Django Shell

```bash
docker-compose exec web python manage.py shell
```

### Create a Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

### Run Migrations

```bash
docker-compose exec web python manage.py migrate
```

---

## 🧪 Running Tests

```bash
docker-compose exec web pytest
```

For linting:

```bash
docker-compose exec web flake8
```

---

## 🚀 Deployment

You can deploy this project using:

* Docker Swarm
* DigitalOcean App Platform
* Heroku (via container registry)
* Any cloud VM with Docker & Docker Compose

Make sure to switch to `.envs/.production` for production environment variables.

---

## 📄 License

This project is licensed under the **MIT License**.
See [`LICENSE`](./LICENSE) for details.

---

## ✍️ Blog

Want to learn how this project was bootstrapped?

📖 [Kickstart Your Django Project in Minutes with Cookiecutter](https://medium.com/@bhushanch45/kick-start-your-django-project-in-minutes-with-cookie-cutter-d0ff7bfe5914)

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

Created by **Bhushan Chaudhari**
📧 [bhushanch45@gmail.com](mailto:bhushanch45@gmail.com)

Let’s connect on [LinkedIn](https://www.linkedin.com/in/bhushanchaudhari45)

```
