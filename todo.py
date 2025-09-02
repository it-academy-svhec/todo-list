from flask import Blueprint, render_template_string, request, redirect, url_for
from flask_login import login_required, current_user

todo_bp = Blueprint("todo", __name__)

todo_template = """
<h2>Your To-Do List</h2>
<form method="post" action="{{ url_for('todo.add') }}">
  <input type="text" name="task" placeholder="New task" required>
  <button type="submit">Add</button>
</form>
<ul>
{% for task in tasks %}
  <li>{{ task['task'] }}
    <a href="{{ url_for('todo.delete', task_id=task['id']) }}">Delete</a>
  </li>
{% endfor %}
</ul>
<a href="{{ url_for('auth.logout') }}">Logout</a>
"""


@todo_bp.route("/")
@login_required
def index():
    from app import app
    conn = app.config["DB_CONNECTION"]()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM todos WHERE user_id = %s",
                   (current_user.id,))
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template_string(todo_template, tasks=tasks)


@todo_bp.route("/add", methods=["POST"])
@login_required
def add():
    from app import app
    task = request.form["task"]
    conn = app.config["DB_CONNECTION"]()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (user_id, task) VALUES (%s, %s)", (current_user.id, task))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("todo.index"))


@todo_bp.route("/delete/<int:task_id>")
@login_required
def delete(task_id):
    from app import app
    conn = app.config["DB_CONNECTION"]()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM todos WHERE id = %s AND user_id = %s", (task_id, current_user.id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("todo.index"))
