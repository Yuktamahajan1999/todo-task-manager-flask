# Task Master 

> A modern, full-stack task management dashboard engineered for quick task tracking, intuitive organization, and clean workflow management.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-D71F00?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

## 📌 Overview

**Task Master** is a lightweight, responsive Web application designed to help users streamline daily task management. Built with Python (Flask) and SQLAlchemy, the application features an interactive dual-column Kanban-style board, real-time client-side search/filtering, dynamic task priorities, due-date tracking with intelligent date status badges, and aggregate dashboard statistics.

---

## ✨ Features

- 📊 **Dashboard Analytics:** Live visual counters tracking Total, Active, Completed, and High-Priority task metrics.
- 📋 **Dual-Column Task Board:** Clear separation between active tasks (`To Do / Active`) and completed tasks (`Completed`).
- ⚡ **Real-Time Search & Priority Filter:** Instant client-side filtering by task title, notes, or priority levels without page reloads.
- 🗓️ **Due Date Tracking:** Smart status indicators identifying **Overdue**, **Due Today**, and **Upcoming** tasks at a glance.
- 🎯 **Priority Management:** Color-coded priority badges (`High`, `Medium`, `Low`) for effective workflow planning.
- ✏️ **Full CRUD Capabilities:** Seamless interface to create, read, edit via modal UI, mark complete/undo, and delete tasks.
- 🎨 **Responsive UI:** Clean, modern interface designed with custom CSS variables and smooth interactive transitions.

---

## 🛠️ Tech Stack

### Backend
- **Framework:** [Flask](https://flask.palletsprojects.com/)
- **ORM:** [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) / [SQLAlchemy 2.0](https://www.sqlalchemy.org/)
- **Database:** [SQLite](https://www.sqlite.org/)

### Frontend
- **Templating:** Jinja2
- **Structure & Styling:** HTML5, Modern CSS3 (CSS Variables, Flexbox, CSS Grid)
- **Scripting:** Vanilla JavaScript (ES6+)

---

## 📁 Project Structure

```text
task-master/
├── main.py                # Flask application routes and database models
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Standard git ignore config
│
├── templates/
│   └── index.html         # Main dashboard template with Jinja2 rendering
│
└── static/
    ├── style.css          # Custom application stylesheet
    └── script.js          # Modal interaction & live search/filtering logic
