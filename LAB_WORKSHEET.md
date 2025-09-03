# Flask Todo App - Database Setup Lab Worksheet

**Student Name:** _________________  
**Date:** _________________  
**Lab Session:** _________________

## Pre-Lab Questions

1. **What is a database migration?**
   - [ ] A way to move data between servers
   - [ ] A script that creates/modifies database structure
   - [ ] A backup of the database
   - [ ] A way to encrypt database data

2. **Why do we use migrations instead of directly creating tables?**
   - [ ] It's faster
   - [ ] It provides version control for database changes
   - [ ] It's required by Flask
   - [ ] It's cheaper

3. **What happens when a web application tries to access a non-existent database table?**
   - [ ] The application crashes completely
   - [ ] The application shows an error message
   - [ ] The application creates the table automatically
   - [ ] Nothing happens

4. **What is a FOREIGN KEY constraint?**
   - [ ] A way to encrypt data
   - [ ] A relationship between tables that maintains data integrity
   - [ ] A backup of the database
   - [ ] A way to speed up queries

## Lab Activities

### Activity 1: Initial Application State

1. **Run the application without setup:**
   ```bash
   python app.py
   ```

2. **What do you see in the browser?**
   - [ ] A working todo application
   - [ ] Error messages
   - [ ] Setup instructions
   - [ ] A blank page

3. **Try to register a user. What happens?**
   - [ ] User is created successfully
   - [ ] Error message appears
   - [ ] Page redirects to login
   - [ ] Nothing happens

### Activity 2: Choose Your Database Setup Method

**You have TWO OPTIONS for this lab:**

#### **Option A: Manual SQL Table Creation (Recommended for Learning)**

4. **Start SQLite and create the database:**
   ```bash
   sqlite3 todo_app.db
   ```

5. **Create the users table manually:**
   ```sql
   CREATE TABLE users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username VARCHAR(50) UNIQUE NOT NULL,
       password_hash VARCHAR(255) NOT NULL
   );
   ```
   
   **What does each part of this SQL command do?**
   - `INTEGER PRIMARY KEY AUTOINCREMENT`: _________________________
   - `VARCHAR(50) UNIQUE NOT NULL`: _________________________
   - `VARCHAR(255) NOT NULL`: _________________________

6. **Create the todos table manually:**
   ```sql
   CREATE TABLE todos (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       user_id INTEGER NOT NULL,
       task VARCHAR(255) NOT NULL,
       FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
   );
   ```
   
   **What does the FOREIGN KEY constraint do?**
   - [ ] Makes the app run faster
   - [ ] Ensures every todo belongs to a valid user
   - [ ] Encrypts the data
   - [ ] Creates a backup

7. **Verify your tables were created:**
   ```sql
   .tables
   ```
   
   **What tables do you see?**
   - [ ] users, todos
   - [ ] users only
   - [ ] todos only
   - [ ] No tables

#### **Option B: Using Flask Migrations (Production Approach)**

8. **Initialize the migration system:**
   ```bash
   python manage.py db init
   ```
   
   **What files/directories were created?**
   - [ ] `migrations/` directory
   - [ ] `todo_app.db` file
   - [ ] `config.py` file
   - [ ] All of the above

9. **Create the initial migration:**
   ```bash
   python manage.py db migrate -m "Initial migration"
   ```
   
   **What does this command do?**
   - [ ] Creates the database file
   - [ ] Creates SQL scripts for table creation
   - [ ] Connects to the database
   - [ ] Backs up existing data

10. **Apply the migration:**
    ```bash
    python manage.py db upgrade
    ```
    
    **What happens when you run this command?**
    - [ ] Nothing visible
    - [ ] Database tables are created
    - [ ] Application starts automatically
    - [ ] Error message appears

### Activity 3: Verification

11. **Run the verification script:**
    ```bash
    python check_setup.py
    ```
    
    **What was the result?**
    - [ ] All checks passed
    - [ ] Some checks failed
    - [ ] Script didn't run
    - [ ] Error occurred

12. **Check your project directory. What new files exist?**
    - [ ] `migrations/` directory (if using Option B)
    - [ ] `todo_app.db` file
    - [ ] Both of the above
    - [ ] Neither of the above

### Activity 4: Testing the Application

13. **Start the application again:**
    ```bash
    python app.py
    ```

14. **What do you see now in the browser?**
    - [ ] Setup instructions
    - [ ] Working todo application
    - [ ] Error messages
    - [ ] Login page

15. **Try to register a user now. What happens?**
    - [ ] User is created successfully
    - [ ] Error message appears
    - [ ] Page redirects to login
    - [ ] Nothing happens

16. **Try to login with the user you created. What happens?**
    - [ ] Login successful, redirected to todos
    - [ ] Invalid credentials error
    - [ ] Database error
    - [ ] Page crashes

## Post-Lab Questions

17. **What is the purpose of the `migrations/` directory?**
    - [ ] To store database backups
    - [ ] To track database schema changes over time
    - [ ] To store user data
    - [ ] To configure the web server

18. **Why do we need to run three separate commands instead of one?**
    - [ ] Because Flask requires it
    - [ ] Each command serves a different purpose in the migration process
    - [ ] It's a security requirement
    - [ ] It's just tradition

19. **What would happen if you tried to run the application without running the migration commands?**
    - [ ] The application would work normally
    - [ ] The application would show error messages
    - [ ] The application would create tables automatically
    - [ ] The application would crash completely

20. **If you used Option A (Manual SQL): What did you learn about database structure?**
    - [ ] How to write SQL commands
    - [ ] How tables relate to each other
    - [ ] How data types work
    - [ ] All of the above

## Reflection Questions

21. **What was the most challenging part of this lab?**
    
    _________________________________________________________
    _________________________________________________________

22. **What did you learn about the relationship between web applications and databases?**
    
    _________________________________________________________
    _________________________________________________________

23. **How would this process be different in a production environment?**
    
    _________________________________________________________
    _________________________________________________________

24. **If you used both methods, which did you prefer and why?**
    
    _________________________________________________________
    _________________________________________________________

## Lab Completion Checklist

- [ ] Application runs without database setup (shows errors)
- [ ] **Option A**: Tables created manually with SQL commands, OR
- [ ] **Option B**: Migration system initialized and applied
- [ ] Verification script passes all checks
- [ ] Application works properly (can register/login/create todos)
- [ ] All questions answered above
- [ ] Lab worksheet submitted

**Lab completed on:** _________________  
**Total time spent:** _________________  
**Method used:** Option A (Manual SQL) / Option B (Migrations) / Both  
**Instructor signature:** _________________
