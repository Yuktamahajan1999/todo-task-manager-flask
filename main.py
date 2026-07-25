from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date


app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Todo(db.Model):

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        db.String(15),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        db.String(250),
        nullable=False
    )

    priority: Mapped[str] = mapped_column(
        db.String(10),
        nullable=False
    )

    completed: Mapped[bool] = mapped_column(
        default=False,
        nullable=False
    )

    due_date: Mapped[date | None] = mapped_column(
        nullable=True
    )


with app.app_context():
    db.create_all()


@app.route("/")
def index():

    tasks = db.session.execute(
        db.select(Todo)
    ).scalars().all()

    today = date.today()

    return render_template(
        "index.html",
        tasks=tasks,
        today_date=today.strftime("%B %d, %Y"),
        today_date_obj=today
    )


@app.route("/add", methods=["POST"])
def add_task():

    due_date_string = request.form.get("due_date")

    task = Todo(

        title=request.form["title"],

        description=request.form["description"],

        priority=request.form["priority"],

        due_date=(
            date.fromisoformat(due_date_string)
            if due_date_string
            else None
        )
    )

    db.session.add(task)

    db.session.commit()

    return redirect(url_for("index"))


@app.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):

    task = db.get_or_404(
        Todo,
        task_id
    )

    task.title = request.form["title"]

    task.description = request.form["description"]

    task.priority = request.form["priority"]

    due_date_string = request.form.get("due_date")

    task.due_date = (

        date.fromisoformat(due_date_string)

        if due_date_string

        else None
    )

    db.session.commit()

    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):

    task = db.get_or_404(
        Todo,
        task_id
    )

    task.completed = not task.completed

    db.session.commit()

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):

    task = db.get_or_404(
        Todo,
        task_id
    )

    db.session.delete(task)

    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)