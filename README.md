# Flask Todo App - Database Setup Lab

This is a Flask web application that demonstrates the relationship between web servers and databases. **The application will NOT work until you manually set up the database.**

## Learning Objectives

By completing this lab, you will:
- Understand how web applications interact with databases
- Learn the process of database initialization and migration
- **NEW: Manually create database tables using SQL commands**
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
- **SQLite command line tool (optional, for manual table creation)**

## Step-by-Step Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Choose Your Database Setup Method

You have **TWO OPTIONS** for setting up the database:

#### **Option A: Manual SQL Table Creation (Recommended for Learning)**

This approach teaches you exactly what's happening in the database:

```bash
# Start SQLite and create the database
sqlite3 todo_app.db

# Then manually create the tables (copy and paste these commands):
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    task VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

# Verify tables were created
.tables

# Exit SQLite
.quit
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

### 4. Run the Application

```bash
python app.py
```

## What Each Method Teaches You

### **Manual SQL Creation (Option A):**
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
- ✅ A `todo_app.db` file in your project directory
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

### Verification Steps

1. Check that `todo_app.db` file was created
2. Verify tables exist (use `sqlite3 todo_app.db .tables` if you used Option A)
3. Look for success messages in terminal output
4. Test the application in your web browser

## Application Features

Once the database is set up, the application provides:
- User registration and authentication
- Create, read, and delete todo items
- User-specific todo lists
- Session management

## File Structure

```
todo-list/
├── app.py              # Main Flask application
├── models.py           # Database models (User, Todo)
├── auth.py             # Authentication routes
├── todo.py             # Todo management routes
├── manage.py           # Database management commands
├── requirements.txt    # Python dependencies
├── .env               # Environment configuration
├── check_setup.py     # Setup verification script
└── README.md          # This file
```

## Learning Reflection

After completing the setup, consider:
- **If you used Option A**: What did you learn about SQL syntax and database structure?
- **If you used Option B**: Why do we need migrations instead of just creating tables directly?
- What happens when a web app tries to access a non-existent database?
- How does the application recover from database errors?
- What would happen in a production environment?

## Next Steps

Once the basic setup is working, you could:
- **Modify the database schema** to add new fields
- **Create new migrations** for schema changes
- **Add more features** to the application
- **Explore different database backends** (PostgreSQL, MySQL)
- **Write custom SQL queries** to interact with your data

---

**Remember**: This is a learning exercise. The errors you see initially are intentional and designed to teach you about database setup and web application architecture. Choose the method that best fits your learning goals!

