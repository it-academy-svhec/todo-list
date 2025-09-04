from flask import Flask, render_template_string
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from models import db, User
from auth import auth_bp
from todo import todo_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-in-production")

# Database config - Students will create this database manually
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo_app.db"
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
    """Landing page with setup instructions - this route should NOT require login"""
    setup_instructions = """
    <h1>Flask Todo App - Database Setup Required</h1>
    
    <h2>Current Status: Database Not Initialized</h2>
    <p style="color: red;">⚠️ The application cannot run until the database is set up.</p>
    
    <h2>Setup Instructions for Students:</h2>
    
    <h3>Step 1: Install Dependencies</h3>
    <pre>pip install -r requirements.txt</pre>
    
    <h3>Step 2: Choose Your Database Setup Method</h3>
    
    <h4>Option A: Manual MySQL Table Creation (Recommended for Learning)</h4>
    <p>This approach teaches you exactly what's happening in the database:</p>
    <pre># Install MySQL (if not already installed)
# On Debian/Ubuntu:
sudo apt update
sudo apt install mysql-server mysql-client

# On Windows:
# Download and install MySQL from: https://dev.mysql.com/downloads/installer/

# Start MySQL service
sudo systemctl start mysql
sudo systemctl enable mysql

# Secure MySQL installation
sudo mysql_secure_installation

# Connect to MySQL as root
sudo mysql -u root -p

# Create the database
CREATE DATABASE todo_app;
USE todo_app;

# Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

# Create todos table
CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    task VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

# Verify tables were created
SHOW TABLES;

# Exit MySQL
EXIT;</pre>
    
    <h4>Option B: Using Flask Migrations (Production Approach)</h4>
    <p>This approach uses automated database migrations:</p>
    <pre># Initialize the migration system
python manage.py db init

# Create the initial migration
python manage.py db migrate -m "Initial migration"

# Apply the migration to create tables
python manage.py db upgrade</pre>
    
    <h3>Step 3: Verify Your Setup</h3>
    <pre>python check_setup.py</pre>
    
    <h3>Step 4: Run the Application</h3>
    <pre>python app.py</pre>
    
    <h3>What Each Method Teaches You:</h3>
    
    <h4>Manual SQL Creation (Option A):</h4>
    <ul>
        <li><strong>SQL syntax</strong> and table structure</li>
        <li><strong>Database relationships</strong> (foreign keys)</li>
        <li><strong>Data types</strong> and constraints</li>
        <li><strong>What happens under the hood</strong></li>
    </ul>
    
    <h4>Flask Migrations (Option B):</h4>
    <ul>
        <li><strong>Automated database management</strong></li>
        <li><strong>Version control</strong> for database changes</li>
        <li><strong>Team collaboration</strong> practices</li>
        <li><strong>Production deployment</strong> workflows</li>
    </ul>
    
    <h3>Expected Result:</h3>
    <p>After successful setup, you should see:</p>
    <ul>
        <li>A <code>todo_app.db</code> file in your project directory</li>
        <li>No more error messages when running the app</li>
        <li>The ability to register users and create todos</li>
    </ul>
    
    <h3>Troubleshooting:</h3>
    <ul>
        <li>Make sure you're in the correct directory</li>
        <li>Check that all dependencies are installed</li>
        <li>Look for error messages in the terminal output</li>
        <li>If using SQL: Check for typos and include semicolons</li>
    </ul>
    
    <hr>
    <p><em>This is a learning exercise to understand how web applications interact with databases.</em></p>
    
    <h3>Test the Current Broken State:</h3>
    <p>Try these links to see database errors:</p>
    <ul>
        <li><a href="/login">Try to Login</a> - Should show database error</li>
        <li><a href="/register">Try to Register</a> - Should show database error</li>
    </ul>
    
    <h3>Need Help?</h3>
    <p>Check the <code>SQL_REFERENCE.md</code> file for detailed SQL commands and explanations!</p>
    """
    
    return render_template_string(setup_instructions)


if __name__ == "__main__":
    print("🚀 Flask Todo App - Database Setup Lab")
    print("=" * 50)
    print("❌ Database setup required!")
    print("You have TWO OPTIONS:")
    print("")
    print("Option A: Manual MySQL Table Creation (Recommended for Learning)")
    print("  Install MySQL, create database 'todo_app', then create tables")
    print("  See detailed instructions at http://127.0.0.1:5000")
    print("")
    print("Option B: Flask Migrations (Production Approach)")
    print("  python manage.py db init")
    print("  python manage.py db migrate -m 'Initial migration'")
    print("  python manage.py db upgrade")
    print("")
    print("Starting app in setup mode...")
    print("Visit http://127.0.0.1:5000 for detailed setup instructions")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
