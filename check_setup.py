#!/usr/bin/env python3
"""
Database Setup Verification Script

Run this script to check if your database is properly set up.
This will help you verify that all the migration steps were completed correctly.
"""

import os
import sys

def check_dependencies():
    """Check if all required packages are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'flask', 'flask_sqlalchemy', 'flask_login', 
        'flask_migrate', 'python-dotenv', 'werkzeug'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed!")
    return True

def check_migrations_directory():
    """Check if migrations directory exists"""
    print("\n🔍 Checking migrations directory...")
    
    if os.path.exists("migrations"):
        print("  ✅ migrations/ directory exists")
        
        # Check for key files
        alembic_ini = os.path.join("migrations", "alembic.ini")
        versions_dir = os.path.join("migrations", "versions")
        
        if os.path.exists(alembic_ini):
            print("  ✅ alembic.ini configuration file exists")
        else:
            print("  ❌ alembic.ini missing")
            return False
            
        if os.path.exists(versions_dir):
            version_files = [f for f in os.listdir(versions_dir) if f.endswith('.py')]
            print(f"  ✅ Found {len(version_files)} migration version(s)")
        else:
            print("  ❌ versions/ directory missing")
            return False
            
        return True
    else:
        print("  ❌ migrations/ directory does not exist")
        print("  Run: python manage.py db init")
        return False

def check_database_file():
    """Check if database file exists"""
    print("\n🔍 Checking database file...")
    
    db_file = "todo_app.db"
    if os.path.exists(db_file):
        file_size = os.path.getsize(db_file)
        print(f"  ✅ {db_file} exists ({file_size} bytes)")
        return True
    else:
        print(f"  ❌ {db_file} does not exist")
        print("  Run: python manage.py db upgrade")
        return False

def check_database_tables():
    """Check if database tables can be accessed"""
    print("\n🔍 Checking database tables...")
    
    try:
        from app import app, db
        from models import User, Todo
        
        with app.app_context():
            # Try to query tables
            user_count = User.query.count()
            todo_count = Todo.query.count()
            
            print(f"  ✅ Users table accessible ({user_count} users)")
            print(f"  ✅ Todos table accessible ({todo_count} todos)")
            return True
            
    except Exception as e:
        print(f"  ❌ Error accessing database tables: {e}")
        print("  Make sure you ran: python manage.py db upgrade")
        return False

def main():
    """Main verification function"""
    print("🚀 Flask Todo App - Database Setup Verification")
    print("=" * 50)
    
    checks = [
        check_dependencies,
        check_migrations_directory,
        check_database_file,
        check_database_tables
    ]
    
    all_passed = True
    for check in checks:
        if not check():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All checks passed! Your database is properly set up.")
        print("You can now run: python app.py")
    else:
        print("❌ Some checks failed. Please follow the instructions above.")
        print("\nQuick setup commands:")
        print("  python manage.py db init")
        print("  python manage.py db migrate -m 'Initial migration'")
        print("  python manage.py db upgrade")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
