# 📝 Task Manager (Django)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

A professional and efficient web-based **Task Management System** built with Django. A high-performance, responsive web application to streamline your daily productivity.This application allows users to organize their daily tasks, track progress, and manage deadlines effectively.

The application is designed for individuals or teams who want a simple, web-based solution to manage productivity.  
Built using **Django (Python)** for the backend, **SQLite** for the database, and **HTML,CSS,Bootstrap** for the frontend.

---

## Features
- **Task CRUD:** Create, Read, Update, and Delete tasks easily.
- **Task Status:** Mark tasks as 'Completed' or 'Pending'.
- **Status Tracking:** Mark tasks as Pending or Completed.
- **Responsive UI:** Clean and modern design that works on mobile and desktop.
- **Mobile First:** Fully responsive UI powered by Bootstrap 5.
- **Progress Tracking:** Toggle status between Pending and Completed with one click.
- **Priority Levels:** Organize tasks based on importance.

---
## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, Bootstrap (for responsive design)

---

## Demo
![image alt](https://github.com/sajjadali-fullstack/task-manager-django/blob/3047ffd3ab612dc0801f4010e211b9c8b2578232/django-to-do-pp.png)

---



# ✅ TaskFlow — Django To-Do App with REST API

A full-stack **To-Do List application** built with **Django**, featuring user authentication, per-user task management, and a **Django REST Framework (DRF) API** — deployed on **Railway**.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django)
![DRF](https://img.shields.io/badge/DRF-REST_API-red?logo=django)
![Deploy](https://img.shields.io/badge/Deployed_on-Railway-0B0D0E?logo=railway)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Live Demo

🔗 **[Live App on Railway](#)** ← 

---

## ✨ Features

- 🔐 **User Authentication** — Signup, Login, Logout (Django auth system)
- 👤 **Per-user Task Isolation** — har user apne hi tasks dekh/edit/delete kar sakta hai
- ✅ **Task CRUD** — Add, Edit, Mark as Done/Undone, Delete
- 🌐 **REST API** — DRF-powered endpoints (`ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`)
- 🎨 Clean, minimal UI with Django templates
- ☁️ Production-ready deployment config for **Railway**

---

## 🛠️ Tech Stack

| Layer          | Technology                     |
|----------------|---------------------------------|
| Backend        | Django, Django REST Framework   |
| Database       | PostgreSQL (prod) / SQLite (dev)|
| Auth           | Django built-in Auth system     |
| Deployment     | Railway, Gunicorn, WhiteNoise   |
| Frontend       | Django Templates + Bootstrap    |

---

6. Railway auto-deploys on every push 🚀

---

## 📡 API Endpoints

| Method | Endpoint                              | Description                  |
|--------|----------------------------------------|-------------------------------|
| GET    | `/api/list-api/`                       | List logged-in user's tasks   |
| POST   | `/api/list-api/`                       | Create a new task             |
| GET    | `/api/list-api-r-u-d/<id>/`            | Retrieve a single task        |
| PUT    | `/api/list-api-r-u-d/<id>/`            | Update a task                 |
| DELETE | `/api/list-api-r-u-d/<id>/`            | Delete a task                 |

> 🔒 All API endpoints require authentication and return only the logged-in user's tasks.

---


## 🗺️ Roadmap

- [ ] Task categories / labels
- [ ] Due dates + reminders
- [ ] Dark mode UI
- [ ] JWT-based API auth for mobile clients

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Your Name**
[LinkedIn](#) • [GitHub](#) • [Portfolio](#)
