# Task Master

A full-stack task management application built with Flask and SQLAlchemy.

Task Master allows users to create, manage, organize, and track their daily tasks through a clean dashboard interface.

## Features

- Create new tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Undo completed tasks
- Set task priority
- Add due dates
- Search tasks by title or description
- Filter tasks by priority
- Dashboard statistics
- Separate active and completed task sections

## Tech Stack

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

### Database
- SQLite

### Frontend
- HTML
- CSS
- Jinja2
- JavaScript

## Project Structure

```text
task-master/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js