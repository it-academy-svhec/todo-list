# MySQL Reference Card for Flask Todo App Lab

## Quick MySQL Commands for Manual Table Creation

### Start MySQL and Create Database
```bash
# Connect to MySQL as root
sudo mysql -u root -p

# Create the database
CREATE DATABASE todo_app;
USE todo_app;
```

### Create Users Table
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
```

### Create Todos Table
```sql
CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    task VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

### Verify Tables Created
```sql
SHOW TABLES;
```

### View Table Structure
```sql
DESCRIBE users;
DESCRIBE todos;
```

### Exit MySQL
```sql
EXIT;
```

## What Each MySQL Keyword Means

### **Data Types:**
- `INT`: Whole numbers (1, 2, 3, -1, -2, etc.)
- `VARCHAR(50)`: Text up to 50 characters
- `PRIMARY KEY`: Unique identifier for each row
- `AUTO_INCREMENT`: Automatically increases for each new row

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

## Common MySQL Commands

### **Database Management:**
```sql
SHOW DATABASES;           -- Show all databases
USE database_name;         -- Switch to database
CREATE DATABASE name;      -- Create new database
DROP DATABASE name;        -- Delete database
```

### **Table Management:**
```sql
SHOW TABLES;              -- Show all tables in current database
DESCRIBE table_name;      -- Show table structure
CREATE TABLE name (...);   -- Create table
DROP TABLE name;           -- Delete table
ALTER TABLE name ADD column_name type;  -- Add column
```

### **Data Operations:**
```sql
SELECT * FROM users;           -- View all users
SELECT * FROM todos;           -- View all todos
INSERT INTO users (username, password_hash) VALUES ('test', 'hash');
UPDATE users SET username = 'new_name' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

### **User Management:**
```sql
-- Create new user
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

-- Grant privileges
GRANT ALL PRIVILEGES ON todo_app.* TO 'username'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
```

### **Help and Exit:**
```sql
HELP;                 -- Show help topics
HELP 'command';       -- Get help for specific command
EXIT;                 -- Exit MySQL
QUIT;                 -- Alternative exit command
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
- Check if Flask app is running
- Restart MySQL service if needed

### **"No such table" error:**
- Make sure you're in the right database: `USE todo_app;`
- Use `SHOW TABLES;` to verify tables exist
- Check for typos in table names

### **"Access denied" error:**
```sql
-- Reset root password
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_password';
FLUSH PRIVILEGES;
```

## Tips for Success

1. **Copy and paste** the exact MySQL commands above
2. **Include semicolons** at the end of each command
3. **Check for typos** - MySQL is case-sensitive
4. **Use `SHOW TABLES;`** to verify tables were created
5. **Use `DESCRIBE table_name;`** to check table structure
6. **Always use `USE todo_app;`** before creating tables

## Next Steps After Creating Tables

1. **Exit MySQL** with `EXIT;`
2. **Update app.py** with your MySQL password
3. **Run verification script**: `python check_setup.py`
4. **Start Flask app**: `python app.py`
5. **Test the application** in your browser

## MySQL vs SQLite Differences

| Feature | MySQL | SQLite |
|---------|-------|--------|
| **Type** | Client-Server | File-based |
| **Installation** | System package | Built into Python |
| **Data Types** | `INT`, `VARCHAR` | `INTEGER`, `TEXT` |
| **Auto-increment** | `AUTO_INCREMENT` | `AUTOINCREMENT` |
| **Commands** | `SHOW TABLES;` | `.tables` |
| **Exit** | `EXIT;` | `.quit` |

---

**Remember**: This is a learning exercise! Take your time to understand what each MySQL command does. The more you understand now, the better you'll be at working with production databases in the future.
