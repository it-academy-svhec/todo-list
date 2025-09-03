from flask import Blueprint, render_template_string, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, Todo
from sqlalchemy.exc import OperationalError

todo_bp = Blueprint("todo", __name__)

todo_template = """
<h2>Your To-Do List</h2>
<form method="post" action="{{ url_for('todo.index') }}">
  <input type="text" name="task" placeholder="New task" required>
  <button type="submit">Add</button>
</form>
<ul>
{% for task in tasks %}
  <li>{{ task.task }}
    <a href="{{ url_for('todo.delete', task_id=task.id) }}">Delete</a>
  </li>
{% endfor %}
</ul>
<a href="{{ url_for('auth.logout') }}">Logout</a>
"""

database_error_template = """
<div style="background-color: #ffe6e6; border: 2px solid #ff6666; padding: 20px; margin: 20px; border-radius: 5px;">
    <h2 style="color: #cc0000;">⚠️ Database Error</h2>
    <p>The database is not properly set up yet. Please follow these steps:</p>
    <ol>
        <li>Run: <code>python manage.py db init</code></li>
        <li>Run: <code>python manage.py db migrate -m "Initial migration"</code></li>
        <li>Run: <code>python manage.py db upgrade</code></li>
        <li>Restart the application</li>
    </ol>
    <p><strong>Error:</strong> {{ error_message }}</p>
    <a href="{{ url_for('index') }}">← Back to Setup Instructions</a>
</div>
"""


@todo_bp.route("/todos")
@login_required
def index():
    try:
        tasks = Todo.query.filter_by(user_id=current_user.id).all()
        return render_template_string(todo_template, tasks=tasks)
    except OperationalError as e:
        return render_template_string(database_error_template, 
                                   error_message="Database tables do not exist. Run the migration commands first.")


@todo_bp.route("/add", methods=["POST"])
@login_required
def add():
    try:
        task = request.form["task"]
        new_todo = Todo(task=task, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("todo.index"))
    except OperationalError as e:
        return render_template_string(database_error_template, 
                                   error_message="Database tables do not exist. Run the migration commands first.")


@todo_bp.route("/delete/<int:task_id>")
@login_required
def delete(task_id):
    try:
        todo = Todo.query.filter_by(id=task_id, user_id=current_user.id).first()
        if todo:
            db.session.delete(todo)
            db.session.commit()
        return redirect(url_for("todo.index"))
    except OperationalError as e:
        return render_template_string(database_error_template, 
                                   error_message="Database tables do not exist. Run the migration commands first.")
