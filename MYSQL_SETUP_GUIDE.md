## 📋 **Prerequisites**
- Basic command line knowledge
- Understanding of SQL concepts
- Python 3.7+ and pip installed
- **Virtual environment knowledge (important!)**

## 🐍 **Python Virtual Environment Setup**

**Why Virtual Environments?**
Modern Linux distributions (like Debian/Ubuntu) use "externally managed environments" to prevent conflicts between system Python packages and user-installed packages. Virtual environments solve this by creating isolated Python environments for each project.

### **Step 1: Install Virtual Environment Support**
```bash
# Install required system packages
sudo apt update
sudo apt install python3-venv python3-pip

# Install MySQL development libraries (needed for mysqlclient)
sudo apt install python3-dev default-libmysqlclient-dev build-essential
```

### **Step 2: Create and Activate Virtual Environment**
```bash
# Navigate to your project directory
cd ~/todo-list

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Your prompt should now show (venv) at the beginning
(venv) ita@linux-srv-1:~/todo-list$
```

### **Step 3: Install Python Dependencies**
```bash
# Make sure your virtual environment is activated
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

### **Step 4: Working with Virtual Environment**
```bash
# To activate (when starting a new terminal session)
source venv/bin/activate

# To deactivate
deactivate

# To see which Python you're using
which python
which pip
```

## 🔧 **Flask App Configuration**

### **Update Database URI**
The app is already configured to use MySQL, but you need to update the password:

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

### **Install Python MySQL Connector**
```bash
# Make sure virtual environment is activated
pip install mysqlclient
```
