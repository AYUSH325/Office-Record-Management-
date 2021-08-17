def addrecord():
    empid=int(input("Enter the employee Id:"))
    First_Name=input("Enter the first name of the employee:")
    Last_Name=input("Enter the last name of the employee:")
    Salary=int(input("Enter the Salary of the employee:"))
    Designation=input("Enter the designation post of the employee:")
    DOJ=input("Enter the date the employee joined the office in year-month-day format:")
    mycursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s)",(empid,First_Name,Last_Name,Salary,Designation,DOJ))
    mydb.commit()
    print("Record added")

def delrecord():
    EMPIN=int(input("Enter the employee Id to be deleted:"))
    try:
        mycursor.execute("delete from employee where EMPID=%s",(EMPIN,))
        mydb.commit()
        print("Record Deleted")
    except:
        print("Record not found")

def updatesal():
    EMPIN=int(input("Enter the employee Id whose salary you want to update:"))
    Amount=int(input("Enter the amount by which the salary should increase:"))
    try:
        mycursor.execute("update employee set salary = salary + %s where EMPID=%s",(Amount,EMPIN,))
        mydb.commit()
        print("Record Updated")
    except:
        print("Record not found")

def updatepos():
    EMPIN=int(input("Enter the employee Id who you want to promote:"))
    NewPos=input("Enter the the new designation of the employee:")
    try:
        mycursor.execute("update employee set Designation = %s where EMPID=%s",(NewPos,EMPIN,))
        mydb.commit()
        print("Record Updated")
    except:
        print("Record not found")

def fetchrecord():
    EMPIN=int(input("Enter the employee Id whose record you want to see:"))
    try:
        mycursor.execute("Select * from employee where EMPID = %s",(EMPIN,))
        Record=mycursor.fetchall()
        print(Record)
    except:
        print("Record not found")
        

import sys
import mysql.connector

print("Enter the password for entering the office database")
n=3
for I in range(n):
    passwd=input()
    if passwd=="CS":
        print("Correct password")
        print("Greetings")
        print("\n")
        break
    else:
        print("Wrong password,")
        n=n-1
        print(n,"Chance remaining")
else:
    print("\n")
    print("Security alert!")
    print("Database closed")
    sys.exit()

mydb=mysql.connector.connect(host="localhost",user="root",passwd="isgsql")
mycursor=mydb.cursor()
mycursor.execute("use office")
print("The details of the employees in this office are:")
mycursor.execute("select * from employee")
for I in mycursor.fetchall():
    print(I)

print("\n")
print("\n")
print("1: Add the details of a new employee who joined the office")
print("2: Remove the details of the employee who resigned the office")
print("3: Update the salary of the the employee who recieved promotion")
print("4: Update the title of the employe who recieved promotion")
print("5: Display the details of all the employees")
print("6: Process finished for now")
print("\n")
print("\n")

while True:
    try:
        ch=int(input("What is your choice from the above:"))
        if ch==1:
            addrecord()
            print("\n")
        elif ch==2:
            delrecord()
            print("\n")
        elif ch==3:
            updatesal()
            print("\n")
        elif ch==4:
            updatepos()
            print("\n")
        elif ch==5:
            fetchrecord()
            print("\n")
        elif ch==6:
            print("Have a great day!")
            sys.exit()
        else:
            print("Wrong choice")
            print("\n")
    except:
        if ch==6:
            break
        else:
            print("Wrong input! Please try again")
            continue

    



