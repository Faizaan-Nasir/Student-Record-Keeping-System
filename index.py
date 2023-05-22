import mysql.connector as sql
con=sql.connect(host="localhost",user='root',password='Abhinav@1176',database='faizaan')
#con=sql.connect(host="localhost",user='root',password='faizaan',database='faizaan')
if con.is_connected():
    pass
else:
    print("Try again")
cur=con.cursor()
try:
    cur.execute('''create table project1 (sno int(4) primary key, name varchar(25), fname varchar(25),
number int(10), grade int(2), section varchar(1))''')
    cur.execute('''create table marks1 (sno int(4), exam varchar(25), sub1 int(3), sub2 int(3), sub3 int(3), average int(3))''')
except:
    pass
print('''1. Insert 'n' records into the student table
2. Insert 'n' records into the marks table''')
choice=int(input("Enter choice: "))
if choice==1:
    n=int(input("Enter number of records you'd like to enter: "))
    for i in range (n):
        sno=int(input("Enter SNO: "))
        name=input("Enter name: ")
        fname=input("Enter father's name: ")
        number=int(input("Enter mobile number: "))
        grade=int(input("Enter grade: "))
        section=input("Enter class: ")
        query='''insert into project1 values({},'{}','{}',{},{},'{}')'''.format(sno,name,fname,number,grade,section)
        cur.execute(query)
    cur.execute("select * from project1;")
    result=cur.fetchall()
    for a in result:
         print(a)
elif choice==2:
        n=int(input("Enter number of records you'd like to enter: "))
        for j in range (n):
            sno=int(input("Enter SNO: "))
            exam=input("Enter Exam: ")
            sub1=int(input("Enter exam percentage in sub1: "))
            sub2=int(input("Enter exam percentage in sub2: "))
            sub3=int(input("Enter exam percentage in sub3: "))
            average=(sub1+sub2+sub3)/3
            query='''insert into marks1 values({},'{}',{},{},{},{})'''.format(sno,exam,sub1,sub2,sub3,average)
            cur.execute(query)
        cur.execute("select * from marks1;")
        result=cur.fetchall()
        for b in result:
            print(b)
print("-----Student Management System-----")
print('''0. Skip Menu
1. Add a Student Record
2. Deleting a Student Record
3. Modifying Student Record
4. Searching a record on the basis of S.No
5. Searching a record on the basis of Name
6. Searching a record on the basis of Grade
7. Sorting records on the basis of Grade''')
z=int(input("Enter your choice: "))
ans="yes"
while ans=="yes":
    if z==0:
        continue
    elif z==1:
        sno=int(input("Enter SNO: "))
        name=input("Enter name: ")
        fname=input("Enter father's name: ")
        number=int(input("Enter mobile number: "))
        grade=int(input("Enter grade: "))
        section=input("Enter class: ")
        query='''insert into project1 values({},'{}','{}',{},{},'{}')'''.format(sno,name,fname,number,grade,section)
        cur.execute(query)
        print("Option 1 executed successfully.")
    elif z==2:
        sno_1=int(input("Enter the S.No of the record you would like to delete: "))
        cur.execute("delete from project1 where sno='"+sno_1+"';")
        print("Option 2 executed successfully.")  
    elif z==3:
        rec_1=input("Enter the S.No of the record you would like to modify: ")
        att_1=input("Enter the attribute you would like to modify: ")
        cur.execute("update project1 set",att_1,"='"+att_1+"'where sno='"+sno+"';")
        print("Option 3 executed successfully.")
    elif z==4:
        sno_2=int(input("Enter the S.No of the student you would like to search"))
        try:
            cur.execute("select * from project1 where sno= '"+sno_2+"';")
            result=cur.fetchall
            if result==1:
                raise Exception("not allowed")
        except:
            for i in result:
                print(i)
        print("Option 4 executed successfully.")
    elif z==5:
        name_1=input("Enter the Name of the student you would like to search")
        try:
            cur.execute("select * from project1 where name= '"+name_1+"';")
            result=cur.fetchall
            if result!=null:
                raise Exception("not allowed")
        except:
            for i in result:
                print(i)
        print("Option 5 executed successfully.")
    elif z==6:
        grade_1=input("Enter the Grade of the student you would like to search")
        try:
            cur.execute("select * from project1 where grade= '"+grade_1+"';")
            result=cur.fetchall
            if result!=null:
                raise Exception("not allowed")
        except:
            for i in result:
                print(i)
        print("Option 6 executed successfully.")
    elif z==7:
        cur.execute("select * from project1 group by grade;")
        result=cur.fetchall()
        for i in result:
            print(i)
        print("Option 7 executed successfully.")
    ans=input("Do you wish to continue? Yes/No: ")
cur.execute("select * from project1;")
cur.execute("select * from marks1;")
print("Thank you for using this software!")
print("- Abhinav & Faizaan")
con.commit()
con.close()