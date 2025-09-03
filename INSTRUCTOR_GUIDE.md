# Flask Todo App - Instructor Guide

## Overview

This lab is designed to teach students about the relationship between web applications and databases. Students will experience what happens when a web app tries to access a non-existent database and learn how to properly set up a database using **TWO different approaches**.

## Learning Objectives

- Understand database migrations and their purpose
- **NEW: Manually create database tables using SQL commands**
- Experience database errors in a controlled environment
- Learn the proper sequence for database setup
- See the difference between a broken and working application
- Compare manual vs. automated database management

## Lab Setup (For Instructors)

### Prerequisites
- Python 3.7+ installed on student machines
- pip package manager
- Web browser for testing
- **SQLite command line tool (for manual table creation option)**

### Files Provided
- `app.py` - Main Flask application (starts in setup mode)
- `models.py` - Database models
- `auth.py` - Authentication routes
- `todo.py` - Todo management routes
- `manage.py` - Database management commands
- `requirements.txt` - Python dependencies
- `.env` - Environment configuration
- `check_setup.py` - Verification script
- `LAB_WORKSHEET.md` - Student worksheet with SQL instructions
- `README.md` - Student instructions with both methods
- `INSTRUCTOR_GUIDE.md` - This guide

## Expected Student Experience

### Phase 1: Broken Application
1. Students run `python app.py`
2. Application starts but shows setup instructions
3. Any attempt to use features results in database errors
4. Students see clear error messages with setup instructions

### Phase 2: Database Setup (Two Options)

#### **Option A: Manual SQL Table Creation (Recommended for Learning)**
1. Students use `sqlite3 todo_app.db` to start SQLite
2. Students manually type SQL commands to create tables:
   ```sql
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
   ```
3. Students verify tables with `.tables` command
4. Students exit SQLite with `.quit`

#### **Option B: Flask Migrations (Production Approach)**
1. Students run `python manage.py db init`
2. Students run `python manage.py db migrate -m "Initial migration"`
3. Students run `python manage.py db upgrade`
4. Students verify setup with `python check_setup.py`

### Phase 3: Working Application
1. Students restart the application
2. Application works normally
3. Students can register, login, and manage todos

## Why Offer Two Options?

### **Option A (Manual SQL) Benefits:**
- **Deep learning**: Students understand exactly what's happening
- **SQL skills**: Students learn actual database syntax
- **Table relationships**: Students see foreign keys and constraints
- **Data types**: Students understand VARCHAR, INTEGER, etc.
- **Hands-on**: Students type every command themselves

### **Option B (Migrations) Benefits:**
- **Production skills**: Students learn industry-standard practices
- **Version control**: Students understand database change management
- **Team collaboration**: Students see how teams work with databases
- **Automation**: Students understand CI/CD workflows

## Common Student Issues & Solutions

### Issue: "No module named 'flask'"
**Solution:** Run `pip install -r requirements.txt`

### Issue: "Error: No such table"
**Solution:** Ensure tables were created (either manually or via migrations)

### Issue: "Port already in use"
**Solution:** Stop other Flask applications or change port in app.py

### Issue: Permission errors on Linux/Debian
**Solution:** Use `sudo` for system-wide installations or ensure proper file permissions

### Issue: SQLite command not found
**Solution:** Install SQLite command line tools or use the migration approach instead

### Issue: SQL syntax errors
**Solution:** Check for typos, ensure semicolons are included, verify table names

## Assessment Criteria

### Excellent (A)
- **Option A**: All SQL commands executed correctly, tables created properly
- **Option B**: All setup commands executed correctly on first attempt
- Application works immediately after setup
- All worksheet questions answered correctly
- Demonstrates understanding of chosen method

### Good (B)
- Setup completed with minor issues
- Application works after troubleshooting
- Most worksheet questions answered correctly
- Basic understanding of chosen method

### Satisfactory (C)
- Setup completed with instructor assistance
- Application works after multiple attempts
- Some worksheet questions answered correctly
- Limited understanding of chosen method

### Needs Improvement (D/F)
- Unable to complete setup without significant help
- Application does not work
- Few worksheet questions answered correctly
- Little understanding of chosen method

## Discussion Points

### During the Lab
1. **Why do we need migrations?**
   - Version control for database changes
   - Team collaboration
   - Production deployment safety

2. **What happens when database setup fails?**
   - Application shows user-friendly errors
   - Graceful degradation
   - Clear guidance for resolution

3. **How is this different from production?**
   - Automated deployment
   - Database administrators
   - Backup and recovery procedures

4. **If using Option A: What did you learn about SQL?**
   - Table structure and relationships
   - Data types and constraints
   - Foreign key relationships

### After the Lab
1. **Real-world applications**
   - How companies handle database changes
   - CI/CD pipelines
   - Rollback strategies

2. **Alternative approaches**
   - Direct table creation
   - ORM auto-migration
   - Database-first design

3. **Comparing the two methods**
   - When to use manual SQL vs. migrations
   - Pros and cons of each approach
   - Learning vs. production considerations

## Troubleshooting for Instructors

### If Students Can't Access the App
1. Check if port 5000 is available
2. Verify firewall settings
3. Ensure Python environment is correct

### If Database Setup Fails
1. Check file permissions
2. Verify SQLite is working
3. Look for error messages in terminal

### If Verification Script Fails
1. Check Python path
2. Verify all dependencies installed
3. Look for import errors

### If Students Struggle with SQL
1. Provide the exact SQL commands to copy/paste
2. Explain each part of the CREATE TABLE statement
3. Use visual aids to show table relationships

## Extension Activities

### For Advanced Students
1. **Modify the database schema**
   - Add new fields to models
   - Create new migrations
   - Test the changes

2. **Switch database backends**
   - PostgreSQL instead of SQLite
   - MySQL instead of SQLite
   - Compare performance

3. **Add new features**
   - Todo categories
   - Due dates
   - Priority levels

4. **Write custom SQL queries**
   - JOIN operations
   - Complex WHERE clauses
   - Data aggregation

### For Struggling Students
1. **Step-by-step guidance**
   - Run commands together
   - Explain each step
   - Show expected output

2. **Visual aids**
   - Screenshots of each step
   - Video walkthrough
   - Diagram of the process

3. **SQL assistance**
   - Provide exact commands to copy
   - Explain each SQL keyword
   - Show table structure diagrams

## Lab Timing

- **Setup Phase (Broken App):** 10-15 minutes
- **Database Setup (Option A - Manual SQL):** 25-35 minutes
- **Database Setup (Option B - Migrations):** 20-30 minutes
- **Testing & Verification:** 15-20 minutes
- **Discussion & Reflection:** 10-15 minutes
- **Total Estimated Time:** 60-95 minutes

## Safety Notes

- Students should not share database files
- Each student should work in their own directory
- No sensitive data should be stored in the lab database
- Remind students this is a learning environment
- SQLite databases are safe to experiment with

## Post-Lab Follow-up

### Homework Assignment
- Research real-world migration strategies
- Compare different database backends
- Document a database schema change
- **Write SQL queries to interact with the created tables**

### Next Lab
- Database relationships and joins
- User authentication security
- API development
- Frontend integration

---

**Note**: This lab is designed to be educational and safe. Students should understand that the initial "broken" state is intentional and part of the learning process. Offering two methods allows students to choose their learning path while covering both theoretical and practical aspects of database management.
