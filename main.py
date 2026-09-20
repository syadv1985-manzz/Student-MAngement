data=[]
def addstudent():
    a=[]
    name=input("Enter student name:")
    try:
        rollno=int(input("Enter Roll Number"))
        marks=float(input("Enter Marks of the Student"))
        if marks < 0 or marks > 100:
            print("ERROR: Marks must be between 0 and 100")
            return
    except ValueError:
        print("Enter Numeric Values only")
        return 
    print(f"STUDENT NAME={name}")
    print(f"ROLL NUMBER={rollno}")
    print(f"MARKS={marks}")
    a.append(name)
    a.append(rollno)
    a.append(marks)
    for i in data:
        if i[1] == rollno:
            print("ERROR: Roll Number already exists")
            return
    data.append(a)
    file=open("student.txt","a")
    file.write(f"{name},{rollno},{marks}\n")    
    file.close()
def viewstudent():
    x=1
    for i in data:
        print(f"Student {x}")
        print(f"STUDENT NAME={i[0]}")
        print(f"ROLL NUMBER={i[1]}")
        print(f"Marks={i[2]}")
        x=x+1
        
def searchstudent():
    f=False
    try:
        x=int(input("Enter Roll Number to Search"))
    except ValueError:
        print("Enter Numeric Values only")
        return
    for i in data:
        if i[1]==x:
            f=True
            print(f"STUDENT NAME={i[0]}")
            print(f"ROLL NUMBER={i[1]}")
            print(f"Marks={i[2]}")
    if f==False:
        print("STUDENT NOT FOUND")
def updatestudent():
    f=False
    try:
        x=int(input("Enter Roll Number to update"))
    except ValueError:
        print("Enter only Numeric Values")
        return
    for i in data:
        if i[1]==x:
            f=True
            break
    if not f:
        print("Student Not Found")
    else:
        i[0]=input("Enter Student Name")
        try:
            marks=float(input("Enter Marks of the Student"))
            if marks < 0 or marks > 100:
                print("ERROR: Marks must be between 0 and 100")
                return
            i[2]=marks
        except ValueError:
            print("Enter only Numeric values")
            return
        file=open("student.txt","w")
        for i in data:
            file.write(f"{i[0]},{i[1]},{i[2]}\n")
        file.close()
            
def deletestudent():
    f=False
    try:
        x=int(input("Enter Roll NUmber to Delete Student"))
    except ValueError:
        print("Enter only Numeric values")
        return
    for i in data:
        if i[1]==x:
            f=True
            break
    if not f:
        print("Student Not Found")
    else:
        data.remove(i)
        print("Student Deleted Successfully")
        file=open("student.txt","w")
        for i in data:
            file.write(f"{i[0]},{i[1]},{i[2]}\n")
        file.close()
def loadstudent():
    try:
        file=open("student.txt","r")
        for line in file:
            line=line.strip()
            values=line.split(",")
            name=values[0]
            rollno=int(values[1])
            marks=float(values[2])
            a=[name,rollno,marks]
            data.append(a)
        file.close()
    except FileNotFoundError:
        print("FILE NOT FOUND")
loadstudent()
n=0

while n!=6:
     try:
         print("\nSTUDENT MANAGEMENT SYSTEM\n")
         print("1.Add Student")
         print("2.View Students")
         print("3.Search Student")
         print("4.Update Student")
         print("5.Delete Student")
         print("6.Exit")
         n=int(input("select an option"))
         if n==1:
             addstudent()
         elif n==2:
             viewstudent()
         elif n==3:
             searchstudent()
         elif n==4:
             updatestudent()
         elif n==5:
             deletestudent()
         elif n==6:
             print("Program Exited")
         else:
             print("invalid operation")
     except ValueError:
         print("ERROR:ENTER ONLY NUMERIC VALUES")
        