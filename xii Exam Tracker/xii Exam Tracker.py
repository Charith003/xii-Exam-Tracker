import mysql.connector

try:
    conobj = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        port=3306,
        database='exam_management'
    )
    if conobj.is_connected():
        print("Successfully Connected to MYSQL")
except mysql.connector.Error as err:
    print("Error:", err)


print("#" * 80)
print("\t \t \t Examination Management")
print("#" * 80, "\n")
print("\t \t \t Class XII Examination Data \n")

l = ["RollNo: ", "Name: ", "Exam: ", "EngMarks: ", "CompMarks: ",
     "PhyMarks: ", "ChemMarks: ", "MathsMarks: ", "Total: ", "Percentage: "]

mycur = conobj.cursor()

def Addnewmarks():
    r = int(input("Roll.No.: "))
    n = input("Name: ")
    e = int(input("Exam: "))
    eng = int(input("Eng Marks: "))
    comp = int(input("Comp Marks: "))
    phy = int(input("Phy Marks: "))
    chem = int(input("Chem Marks: "))
    mat = int(input("Maths Marks: "))
    total = eng + comp + phy + chem + mat
    print("Total: ", total)
    prcnt = round(float((total / 500) * 100), 1)
    print("Percent: ", prcnt)

    mycur.execute(
        "INSERT INTO exams (rollno, name, exam, engm, compm, phym, chemm, mathsm, total, percent) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (r, n, e, eng, comp, phy, chem, mat, total, prcnt)
    )
    conobj.commit()
    print("Data Added Successfully\n")
    print("#" * 80, "\n")
    mainfunc()

def candidatesearch():
    global l
    a = int(input("RollNo: "))
    b = int(input("Exam: "))
    if b in [1, 2, 3]:
        mycur.execute("SELECT * FROM exams WHERE rollno=%s AND exam=%s", (a, b))
        data = mycur.fetchone()
        if data:
            for i in range(0, 10):
                print(l[i], data[i])
        else:
            print("No record found.")
    else:
        print("Exam Code is Invalid. Try again!")
    print("#" * 80, "\n")
    mainfunc()

def ranklist():
    ex1 = int(input("Enter Exam Code: "))
    mycur.execute("SELECT * FROM exams WHERE exam=%s ORDER BY total DESC", (ex1,))
    data = mycur.fetchall()
    print(l)
    for i in data:
        print(i)
    print("#" * 80, "\n")
    mainfunc()

def updatemarks():
    ch1 = int(input("RollNo: "))
    ch2 = int(input("Exam: "))
    d = {1: "engm", 2: "compm", 3: "phym", 4: "chemm", 5: "mathsm"}
    print("1.Eng 2.Comp 3.Phy 4.Chem 5.Maths")
    ch3 = int(input("Enter Option to Update: "))
    ch4 = int(input("Enter Existing Marks: "))
    ch5 = int(input("Enter New Marks: "))

    mycur.execute(
        f"UPDATE exams SET {d[ch3]}=%s WHERE {d[ch3]}=%s AND exam=%s AND rollno=%s",
        (ch5, ch4, ch2, ch1)
    )
    mycur.execute(
        "UPDATE exams SET total=engm+compm+phym+chemm+mathsm WHERE rollno=%s AND exam=%s",
        (ch1, ch2)
    )
    mycur.execute(
        "UPDATE exams SET percent=(total/500)*100 WHERE rollno=%s AND exam=%s",
        (ch1, ch2)
    )
    conobj.commit()
    print("Updated Successfully")
    print("#" * 80, "\n")
    mainfunc()

def criteria():
    ex1 = int(input("Exam: "))
    req = float(input("Enter Start Percentage: "))
    req2 = float(input("Enter End Percentage: "))

    mycur.execute(
        "SELECT * FROM exams WHERE exam=%s AND percent >= %s AND percent <= %s ORDER BY total DESC",
        (ex1, req, req2)
    )
    data = mycur.fetchall()
    print(l)
    for i in data:
        print(i)
    print("#" * 80, "\n")
    mainfunc()

def displaydata():
    global l
    ex1 = int(input("Enter Exam Code (0 for all exams): "))
    if ex1 == 0:
        mycur.execute("SELECT * FROM exams ORDER BY exam, rollno")
    else:
        mycur.execute("SELECT * FROM exams WHERE exam=%s ORDER BY exam, rollno", (ex1,))
    data = mycur.fetchall()
    print(l)
    for i in data:
        print(i)
    print("#" * 80, "\n")
    mainfunc()

def absnt():
    abse = int(input("Enter RollNo.: "))
    absb = int(input("Enter Exam: "))
    print("1.Eng 2.Comp 3.Phy 4.Chem 5.Maths")
    absr = int(input("Enter Subject Code: "))
    mycur.execute(
        "INSERT INTO absentees (rollno, exam, subject) VALUES (%s, %s, %s)",
        (abse, absb, absr)
    )
    conobj.commit()
    print("Absentee Data Added Successfully\n")
    print("#" * 80, "\n")
    mainfunc()

def absnt1():
    print("R.No.:    Exam:    Subject:")
    mycur.execute("SELECT * FROM absentees ORDER BY rollno")
    data = mycur.fetchall()
    for i in data:
        print(i)
    print("#" * 80, "\n")
    mainfunc()

def mainfunc():
    print("1. Add New Marklists\n"
          "2. Get Candidate's Marks\n"
          "3. Ranklist of an Exam\n"
          "4. Update Existing Marks\n"
          "5. Search with Condition\n"
          "6. Display Data\n"
          "7. Absentees Entry\n"
          "8. Absentees Display\n"
          "0. Quit\n")
    try:
        ch = int(input("Enter Your Choice: "))
    except ValueError:
        print("Invalid input. Try again.\n")
        mainfunc()
        return

    print()
    if ch == 1:
        Addnewmarks()
    elif ch == 2:
        candidatesearch()
    elif ch == 3:
        ranklist()
    elif ch == 4:
        updatemarks()
    elif ch == 5:
        criteria()
    elif ch == 6:
        displaydata()
    elif ch == 7:
        absnt()
    elif ch == 8:
        absnt1()
    elif ch == 0:
        conobj.close()
        print("Thanking You!!! Program Terminated.")
    else:
        print("Invalid! Try Again!!\n")
        mainfunc()

mainfunc()
