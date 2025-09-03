# SQL Reference Card for Flask Todo App Lab

## Quick SQL Commands for Manual Table Creation

### Start SQLite and Create Database
```bash
sqlite3 todo_app.db
```

### Create Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
```

### Create Todos Table
```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    task VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### Verify Tables Created
```sql
.tables
```

### View Table Structure
```sql
.schema users
.schema todos
```

### Exit SQLite
```sql
.quit
```

## What Each SQL Keyword Means

### **Data Types:**
- `INTEGER`: Whole numbers (1, 2, 3, -1, -2, etc.)
- `VARCHAR(50)`: Text up to 50 characters
- `PRIMARY KEY`: Unique identifier for each row
- `AUTOINCREMENT`: Automatically increases for each new row

### **Constraints:**
- `NOT NULL`: Field must have a value (cannot be empty)
- `UNIQUE`: No two rows can have the same value
- `FOREIGN KEY`: Links this table to another table
- `ON DELETE CASCADE`: If user is deleted, their todos are also deleted

### **Table Relationships:**
- `users` table: Stores user accounts
- `todos` table: Stores todo items
- `user_id` in todos links to `id` in users
- This creates a "one-to-many" relationship (one user can have many todos)

## Common SQLite Commands

### **Database Management:**
```sql
.databases          -- Show all databases
.tables             -- Show all tables in current database
.schema table_name  -- Show table structure
.indexes table_name -- Show table indexes
```

### **Data Operations:**
```sql
SELECT * FROM users;           -- View all users
SELECT * FROM todos;           -- View all todos
INSERT INTO users (username, password_hash) VALUES ('test', 'hash');
UPDATE users SET username = 'new_name' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

### **Help and Exit:**
```sql
.help              -- Show all available commands
.quit              -- Exit SQLite
.exit              -- Alternative exit command
```

## Troubleshooting

### **"Table already exists" error:**
```sql
DROP TABLE users;    -- Remove existing table
DROP TABLE todos;    -- Remove existing table
```
Then recreate with CREATE TABLE commands.

### **"Database is locked" error:**
- Make sure no other process is using the database
- Exit SQLite and restart
- Check if Flask app is running

### **"No such table" error:**
- Make sure you're in the right database
- Use `.tables` to verify tables exist
- Check for typos in table names

## Tips for Success

1. **Copy and paste** the exact SQL commands above
2. **Include semicolons** at the end of each command
3. **Check for typos** - SQL is case-sensitive
4. **Use `.tables`** to verify tables were created
5. **Use `.schema`** to check table structure

## Next Steps After Creating Tables

1. **Exit SQLite** with `.quit`
2. **Run verification script**: `python check_setup.py`
3. **Start Flask app**: `python app.py`
4. **Test the application** in your browser

---

**Remember**: This is a learning exercise! Take your time to understand what each SQL command does. The more you understand now, the better you'll be at working with databases in the future.
