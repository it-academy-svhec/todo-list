# Flask Todo App - Database Setup Lab

This is a Flask web application that demonstrates the relationship between web servers and databases. **The application will NOT work until you manually set up the database.**

## Learning Objectives

By completing this lab, you will:
- Install and configure MySQL database server
- Understand client-server database architecture vs file-based databases
- Learn the process of database initialization and migration
- **NEW: Manually create database tables using MySQL commands**
- See the difference between a working and non-working application
- Practice using Flask-Migrate for database management

## Current Status

⚠️ **The application is currently in "setup mode" and cannot function properly.**

When you first run the app, you'll see:
- A setup instructions page at the root URL
- Error messages when trying to access features
- Clear guidance on what needs to be done

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- **MySQL Server and Client (for manual table creation)**
- Basic command line knowledge

## Step-by-Step Setup

### 1. Set Up Python Virtual Environment

**Important**: Modern Linux systems require virtual environments for Python packages.

```bash
# Install virtual environment support
sudo apt install python3-venv python3-pip

# Install MySQL development libraries
sudo apt install python3-dev default-libmysqlclient-dev build-essential

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should now show (venv) at the beginning
```

### 2. Install Dependencies

```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### 2. Choose Your Database Setup Method

You have **TWO OPTIONS** for setting up the database:

#### **Option A: Manual MySQL Table Creation (Recommended for Learning)**

This approach teaches you exactly what's happening in the database:

```bash
# Install MySQL (if not already installed)
# On Debian/Ubuntu:
sudo apt update
sudo apt install mysql-server mysql-client

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
EXIT;
```

#### **Option B: Using Flask Migrations (Production Approach)**

This approach uses automated database migrations:

```bash
# Initialize the migration system
python manage.py db init

# Create the initial migration
python manage.py db migrate -m "Initial migration"

# Apply the migration to create tables
python manage.py db upgrade
```

### 3. Verify Your Setup

```bash
python check_setup.py
```

### 4. Update Database Password (Important!)

Before running the app, you need to update the database connection in `app.py`:

**File to edit**: `app.py` (line 17)

**Current line**:
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/todo_app"
```

**What to change**:
- Replace `password` with your actual MySQL root password
- Keep everything else the same

**Example**:
```python
# If your MySQL root password is "mypassword123"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mypassword123@localhost/todo_app"
```

**Important**: 
- Don't change `root` (the username)
- Don't change `localhost` (the host)  
- Don't change `todo_app` (the database name)
- **ONLY change the password part!**

### 5. Run the Application

```bash
python app.py
```

## What Each Method Teaches You

### **Manual MySQL Creation (Option A):**
- **MySQL installation** and configuration
- **Client-server database architecture**
- **SQL syntax** and table structure
- **Database relationships** (foreign keys)
- **Data types** and constraints
- **What happens under the hood**

### **Flask Migrations (Option B):**
- **Automated database management**
- **Version control** for database changes
- **Team collaboration** practices
- **Production deployment** workflows

## Expected Results

After successful setup, you should see:
- ✅ MySQL service running and accessible
- ✅ A `todo_app` database in MySQL
- ✅ Required tables (`users` and `todos`) created
- ✅ No more error messages when running the app
- ✅ The ability to register users and create todos
- ✅ A fully functional web application

## Troubleshooting

### Common Issues

1. **"No module named 'flask'"**
   - Solution: Run `pip install -r requirements.txt`

2. **"Error: no such table"**
   - Solution: Make sure you created the tables (either manually or via migrations)

3. **"Port already in use"**
   - Solution: Stop any other running Flask applications or change the port

4. **Permission errors on Linux/Debian**
   - Solution: Use `sudo` for system-wide installations or ensure proper file permissions

5. **"Access denied for user 'root'@'localhost'"**
   - Solution: Check your MySQL root password in `app.py`

6. **"Can't connect to MySQL server"**
   - Solution: Start MySQL service with `sudo systemctl start mysql`

7. **"mysqlclient not found"**
   - Solution: Install with `pip install mysqlclient`

8. **"externally-managed-environment" error**
   - Solution: Create and activate a virtual environment first
   - Use: `python3 -m venv venv` then `source venv/bin/activate`

### Verification Steps

1. **Check virtual environment**: Make sure `(venv)` appears in your prompt
2. Check that MySQL service is running: `sudo systemctl status mysql`
3. Verify database exists: Connect to MySQL and run `SHOW DATABASES;`
4. Verify tables exist: Use `SHOW TABLES;` in the `todo_app` database
5. Look for success messages in terminal output
6. Test the application in your web browser

## Application Features

Once the database is set up, the application provides:
- User registration and authentication
- Create, read, and delete todo items
- User-specific todo lists
- Session management

## File Structure

```
todo-list/
├── app.py                    # Main Flask application
├── models.py                 # Database models (User, Todo)
├── auth.py                   # Authentication routes
├── todo.py                   # Todo management routes
├── manage.py                 # Database management commands
├── requirements.txt          # Python dependencies
├── .env                     # Environment configuration
├── check_setup.py           # Setup verification script
├── MYSQL_SETUP_GUIDE.md     # Comprehensive MySQL setup guide
├── SQL_REFERENCE.md          # MySQL command reference
└── README.md                 # This file
```

## Learning Reflection

After completing the setup, consider:
- **If you used Option A**: What did you learn about MySQL installation, client-server architecture, and SQL syntax?
- **If you used Option B**: Why do we need migrations instead of just creating tables directly?
- What's the difference between file-based (SQLite) and client-server (MySQL) databases?
- What happens when a web app tries to access a non-existent database?
- How does the application recover from database errors?
- What would happen in a production environment?

## Next Steps

Once the basic setup is working, you could:
- **Modify the database schema** to add new fields
- **Create new migrations** for schema changes
- **Add more features** to the application
- **Explore different database backends** (PostgreSQL, MongoDB)
- **Write custom SQL queries** to interact with your data
- **Learn about MySQL optimization** and indexing
- **Practice database administration** tasks

---

**Remember**: This is a learning exercise. The errors you see initially are intentional and designed to teach you about database setup and web application architecture. Choose the method that best fits your learning goals!

