import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="khushi_db",
    use_pure=True,
)

mycursor = mydb.cursor()

def add_student():
    try:
        student_id = int(input("Student ID : "))
        data = "SELECT * FROM Students WHERE Student_ID = %s"
        values = (student_id,)
        mycursor.execute(data, values)
        result = mycursor.fetchone()
        if result:
            print("Student ID Already Exists")
        else:
            name = input("Name : ")
            age = int(input("Age : "))
            gender = input("Gender : ")
            course = input("Course : ")
            python = int(input("Python Marks : "))
            sql = int(input("SQL Marks : "))
            total = python + sql
            print("Total Marks : ", total)
            percentage = total / 2
            print("Percentage : ", percentage)

            data = "INSERT INTO Students (Student_ID, Name, Age, Gender, Course, Python_Marks, SQL_Marks, Total_Marks, Percentage) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (student_id, name, age, gender, course, python, sql, total, percentage)
            mycursor.execute(data, values)
            mydb.commit()

            print("Student Added Successfully")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def view_students():
    data = "SELECT * FROM Students"
    mycursor.execute(data)

    result = mycursor.fetchall()
    for x in result:
        print(x)

def search_students():
    try:
        num = int(input("Enter Student ID you want to search details about : "))
        data = "SELECT * FROM Students WHERE Student_ID = %s"
        values = (num,)
        mycursor.execute(data, values)
        result = mycursor.fetchone()
        if result:
            print(result)
        else:
            print("Student Not Found")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def update_students():
    try:
        num = int(input("Enter Student ID in which you want to make changes : "))
        query = "SELECT * FROM Students WHERE Student_ID = %s"
        values = (num,)
        mycursor.execute(query,values)
        result = mycursor.fetchone()
        if result:
            print("1. Name \n2. Age \n3. Gender \n4. Course \n5. Python Marks \n6. SQL Marks")
            update = int(input("In which Column you want to make changes : "))
            if update == 1:
                new_name = input("Enter New Name : ")
                data = "UPDATE Students SET Name = %s WHERE Student_ID = %s"
                values = (new_name, num)
                mycursor.execute(data, values)
                mydb.commit()
                print("Name Updated Successfully!")
            elif update == 2:
                new_age = int(input("Enter New Age : "))
                data = "UPDATE Students SET Age = %s WHERE Student_ID = %s"
                values = (new_age,num)
                mycursor.execute(data, values)
                mydb.commit()
                print("Age Updated Successfully!")
            elif update == 3:
                new_gender = input("Enter New Gender : ")
                data = "UPDATE Students SET Gender = %s WHERE Student_ID = %s"
                values = (new_gender, num)
                mycursor.execute(data, values)
                mydb.commit()
                print("Gender Updated Successfully!")
            elif update == 4:
                new_course = input("Enter New Course : ")
                data = "UPDATE Students SET Course = %s WHERE Student_ID = %s"
                values = (new_course, num)
                mycursor.execute(data, values)
                mydb.commit()
                print("Course Updated Sucessfully!")
            elif update == 5:
                sql_marks = "SELECT SQL_Marks FROM Students WHERE Student_ID = %s"
                mycursor.execute(sql_marks, (num,))
                result = mycursor.fetchone()
                if result:
                    sql_marks = result[0]
                    new_python_marks = int(input("Enter New Python Marks : "))
                    total = new_python_marks + sql_marks
                    percentage = total/2
                    data = "UPDATE Students SET Python_Marks = %s, Total_Marks = %s, Percentage = %s WHERE Student_ID = %s"
                    values = (new_python_marks, total, percentage, num)
                    mycursor.execute(data, values)
                    mydb.commit()
                    print("Python Marks Updated Successfully")
                else:
                    print("Student Not Found")
            elif update == 6:
                python_marks = "SELECT Python_Marks FROM Students WHERE Student_ID = %s"
                mycursor.execute(python_marks, (num,))
                result = mycursor.fetchone()
                if result:
                    python_marks = result[0]
                    new_sql_marks = int(input("Enter New SQL Marks : "))
                    total = new_sql_marks + python_marks
                    percentage = total/2
                    data = "UPDATE Students SET SQL_Marks = %s, Total_Marks = %s, Percentage = %s WHERE Student_ID = %s"
                    values = (new_sql_marks, total, percentage, num)
                    mycursor.execute(data, values)
                    mydb.commit()
                    print("SQL Marks Updated Successfully")
                else:
                    print("Student Not Found")
            else:
                print("Invalid Choice")
        else:
            print("Student ID not found!")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    

def delete_student():
    try:
        num = int(input("Enter Student ID : "))
        data = "SELECT * FROM Students WHERE Student_ID = %s"
        values = (num,)
        mycursor.execute(data, values)
        result = mycursor.fetchone()
        if result:
            data = "DELETE FROM Students WHERE Student_ID = %s"
            values = (num,)
            mycursor.execute(data,values)
            mydb.commit()
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def topper_students():
    query = "SELECT MAX(Total_Marks) FROM Students"
    mycursor.execute(query,)
    result = mycursor.fetchone()
    if result:
        max_marks = result[0]
        data = "SELECT Student_ID, Name, Course, Total_Marks, Percentage FROM Students WHERE Total_Marks = %s"
        mycursor.execute(data, (max_marks,))
        result1 = mycursor.fetchall()
        print("\n===================================")
        print("           TOPPER STUDENT")
        print("===================================")

        for x in result1:
            print("Student ID  : ", x[0])
            print("Name        : ", x[1])
            print("Course      : ", x[2])
            print("Total Marks : ", x[3])
            print("Percentage  : ", x[4])
        print("===================================")
    else:
        print("Nothing Found!")
    

def menu():
    while True:
        print("\n=======================================")
        print("        STUDENT MANAGEMENT SYSTEM")
        print("=======================================")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Topper Student")
        print("7. Exit")
        print("\n=======================================")
        try:
            choice = int(input("Enter Your Choice : "))
            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                search_students()
            elif choice == 4:
                update_students()
            elif choice == 5:
                delete_student()
            elif choice == 6:
                topper_students()
            elif choice == 7:
                print("Thank You")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
menu()       
    
        
            



    








