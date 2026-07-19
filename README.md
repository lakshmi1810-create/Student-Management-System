#  Student Management System

A **Student Management System** developed using **Python** and **MySQL** that allows users to efficiently manage student records through a menu-driven command-line interface.

The application supports complete **CRUD (Create, Read, Update, Delete)** operations, automatically calculates **Total Marks** and **Percentage**, and displays the **Topper Student(s)** based on the highest total marks.

This project demonstrates the fundamentals of Python programming, SQL, database connectivity, and exception handling.

---

##  Features

-  Add a new student
-  View all student records
-  Search student by Student ID
-  Update student information
  - Name
  - Age
  - Gender
  - Course
  - Python Marks
  - SQL Marks
-  Delete student records
-  Display topper student(s)
-  Automatic Total Marks calculation
-  Automatic Percentage calculation
-  Duplicate Student ID validation
-  Student existence check before update/delete
-  Input validation using exception handling

---

##  Tech Stack

| Technology | Description |
|------------|-------------|
| Python 3 | Programming Language |
| MySQL | Database |
| mysql-connector-python | Python-MySQL Connector |
| SQL | Database Queries |

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── student_management.py
├── README.md
├── requirements.txt
├── menu.png
├── add_student.png
├── view_students.png
├── search_student.png
├── update_student.png
├── delete_student.png
└── topper_student.png
```

---

##  Prerequisites

Make sure the following are installed on your system:

- Python 3.x
- MySQL Server
- MySQL Workbench (Optional)
- mysql-connector-python

Install the required package:

```bash
pip install mysql-connector-python
```

Or using the requirements file:

```bash
pip install -r requirements.txt
```

---

##  Database Setup

### Step 1: Create Database

```sql
CREATE DATABASE khushi_db;
USE khushi_db;
```

### Step 2: Create Students Table

```sql
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(20),
    Course VARCHAR(100),
    Python_Marks INT,
    SQL_Marks INT,
    Total_Marks INT,
    Percentage FLOAT
);
```

---

##  Configure Database

Update your MySQL credentials inside **student_management.py**.

```python
mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="YOUR_PASSWORD",
    database="khushi_db",
    use_pure=True
)
```

---

##  How to Run

Clone the repository:

```bash
git clone https://github.com/lakshmi1810-create/student-management-system.git
```

Navigate to the project directory:

```bash
cd student-management-system
```

Run the application:

```bash
python student_management.py
```

---

##  Screenshots

###  Main Menu

![Main Menu](menu.png)

---

###  Add Student

![Add Student](add_student.png)

---

###  View Students

![View Students](view_students.png)

---

###  Search Student

![Search Student](search_student.png)

---

###  Update Student

![Update Student](update_student.png)

---

###  Delete Student

![Delete Student](delete_student.png)

---

###  Topper Student

![Topper Student](topper_student.png)

---

##  Sample Menu

```text
=======================================
        STUDENT MANAGEMENT SYSTEM
=======================================
1. Add Student
2. View Student
3. Search Student
4. Update Student
5. Delete Student
6. Topper Student
7. Exit
=======================================
```

---

##  Concepts Used

- Python Functions
- Modular Programming
- MySQL Database Connectivity
- CRUD Operations
- SQL Queries
- Parameterized Queries
- Aggregate Functions (`MAX()`)
- Exception Handling (`try` / `except`)
- Conditional Statements
- Loops
- Input Validation

---

##  Future Improvements

-  User Login Authentication
-  GUI using Tkinter or CustomTkinter
-  Grade Calculation (A, B, C, etc.)
-  Attendance Management
-  Export Student Records to Excel/PDF
-  Search Students by Name
-  Sorting and Filtering
-  Student Report Card Generation

---

##  Author

**Lakshmi Chauhan**

If you enjoyed this project, feel free to fork it, suggest improvements, or connect with me on GitHub.

---

##  Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates me to keep building and sharing more projects.

Happy Coding! 🚀
