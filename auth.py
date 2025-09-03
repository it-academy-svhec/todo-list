from flask import Blueprint, render_template_string, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import get_user_by_username, create_user
from sqlalchemy.exc import OperationalError

auth_bp = Blueprint("auth", __name__)

# Simple HTML templates inline for demo purposes
login_template = """
<h2>Login</h2>
<form method="post">
  <input type="text" name="username" placeholder="Username" required><br>
  <input type="password" name="password" placeholder="Password" required><br>
  <button type="submit">Login</button>
</form>
<a href="{{ url_for('auth.register') }}">Register</a>
"""

register_template = """
<h2>Register</h2>
<form method="post">
  <input type="text" name="username" placeholder="Username" required><br>
  <input type="password" name="password" placeholder="Password" required><br>
  <button type="submit">Register</button>
</form>
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


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = get_user_by_username(username)
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for("todo.index"))
            flash("Invalid credentials")
        return render_template_string(login_template)
    except OperationalError as e:
        return render_template_string(database_error_template, 
                                   error_message="Database tables do not exist. Run the migration commands first.")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            create_user(username, password)
            flash("User created, please login.")
            return redirect(url_for("auth.login"))
        return render_template_string(register_template)
    except OperationalError as e:
        return render_template_string(database_error_template, 
                                   error_message="Database tables do not exist. Run the migration commands first.")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
