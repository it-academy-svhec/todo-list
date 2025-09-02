from flask import Blueprint, render_template_string, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import get_user_by_username, create_user

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


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    from app import app
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_user_by_username(username, app.config["DB_CONNECTION"])
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("todo.index"))
        flash("Invalid credentials")
    return render_template_string(login_template)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    from app import app
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        create_user(username, password, app.config["DB_CONNECTION"])
        flash("User created, please login.")
        return redirect(url_for("auth.login"))
    return render_template_string(register_template)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
