from flask import Flask, render_template_string, redirect, url_for
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from models import db, User
from auth import auth_bp
from todo import todo_bp

load_dotenv()
# Ensure MySQL driver is available for SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()



app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-in-production")

# Database config - Students will create this database manually
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/todo_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Register blueprints FIRST
app.register_blueprint(auth_bp)
app.register_blueprint(todo_bp)

# Configure login manager AFTER registering blueprints
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None


@app.route("/")
def index():
    """If DB is reachable, go straight to /todos. Otherwise show setup page."""
    try:
        # Quick DB check (runs a trivial query)
        db.session.execute("SELECT 1")
        return redirect(url_for("todo.todos"))  # assumes todo_bp has a "todos" route
    except Exception as e:
        # If DB not available, show setup instructions
        setup_instructions = """
        <h1>Flask Todo App - Database Setup Required</h1>
        <p style="color: red;">⚠️ The application cannot run until the database is set up.</p>
        <p>Error: {}</p>
        <p>Follow the setup instructions to create the database and tables.</p>
        <ul>
            <li><a href="/login">Try to Login</a></li>
            <li><a href="/register">Try to Register</a></li>
        </ul>
        """.format(e)
        return render_template_string(setup_instructions)


if __name__ == "__main__":
    print("🚀 Flask Todo App - Database Setup Lab")
    print("=" * 50)
    print("❌ Database setup required (unless DB already exists).")
    print("Visit http://127.0.0.1:5000 for detailed setup instructions")
    print("=" * 50)

    app.run(debug=False, host="0.0.0.0", port=5000)
