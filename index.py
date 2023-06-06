import mysql.connector as sql
con=sql.connect(host="localhost",user='root',password='ENTER YOUR DATABASE PWD',database='ENTER THE DATABASE YOU WOULD LIKE TO USE')

#functions
def select(table,column,option):
    cur.execute("select * from "+table+" where "+column+"="+option+";")
    result=cur.fetchall()
    for i in result:
        print(i)
    if len(result)==0:
        print("No record matches your conditions.")
def display(table):
    cur.execute("select * from "+table+";")
    result=cur.fetchall()
    for i in result:
        print(i)

if con.is_connected():
    pass
else:
    print("Try again")
cur=con.cursor()
print("--- Students versus Marks ---")
time=input("Is this the first time you're running this program? (yes/no): ")
if time=='yes':
    cur.execute('''create table project1 (sno int(4) primary key, name varchar(25), fname varchar(25),
number int(10), grade int(2), section varchar(1))''')
    cur.execute('''create table marks1 (sno int(4), exam varchar(25), sub1 int(3), sub2 int(3), sub3 int(3), average int(3))''')
    print("Database created successfully")
print()
print('''0. Skip inserting new records
1. Insert 'n' records into the student table
2. Insert 'n' records into the marks table''')
print()
choice=int(input("Enter choice: "))
print()
if choice==1:
    n=int(input("Enter number of records you'd like to enter: "))
    for i in range (n):
        sno=int(input("Enter SNO: "))
        name=input("Enter name: ")
        fname=input("Enter father's name: ")
        number=int(input("Enter mobile number (10 digits, first digit must be 0): "))
        grade=int(input("Enter grade: "))
        section=input("Enter class: ")
        query='''insert into project1 values({},'{}','{}',{},{},'{}')'''.format(sno,name,fname,number,grade,section)
        cur.execute(query)
        con.commit()
        print("----- This is the end of record number",i+1,"-----")
        print()
    print("Current records in the student table are as follows:")
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
            con.commit()
            print("----- This is the end of record number",j+1,"-----")
            print()
        print("Current records in the marks table are as follows:")
        cur.execute("select * from marks1;")
        result=cur.fetchall()
        for b in result:
            print(b)
print()

#first table
print("-----Student Management System Table-1-----")
print('''0. Skip Menu
1. Add a Student Record
2. Deleting a Student Record
3. Modifying Student Record
4. Searching a record on the basis of S.No
5. Searching a record on the basis of Name
6. Searching a record on the basis of Grade
7. Sorting records on the basis of Grade''')
print()

z=int(input("Enter your choice: "))
ans="yes"
while ans=="yes":
    if z==0:
        ans='no'
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
        con.commit()
        print("---- Function 1 executed successfully ----")
        print()
    elif z==2:
        sno_1=input("Enter the S.No of the record you would like to delete: ")
        cur.execute("delete from project1 where sno='"+sno_1+"';")
        print("---- Function 2 executed successfully ----")
        print()
    elif z==3:
        sno=input("Enter the S.No of the record you would like to modify: ")
        att_1=input("Enter the attribute you would like to modify (kindly only modify string type datsets): ")
        new_val=input("Enter new value for the given attribute: ")
        cur.execute("update project1 set "+att_1+"='"+new_val+"' where sno='"+sno+"';")
        print("---- Function 3 executed successfully ----")
        print()
    elif z==4:
        sno_2=input("Enter the S.No of the student you would like to search: ")
        select('project1','sno',sno_2)
        print("---- Function 4 executed successfully ----")
        print()
    elif z==5:
        name_1=input("Enter the Name of the student you would like to search: ")
        name_1="'"+name_1+"'"
        select('project1','name',name_1)
        print("---- Function 5 executed successfully ----")
        print()
    elif z==6:
        grade_1=input("Enter the Grade of the student you would like to search: ")
        select('project1','grade',grade_1)
        print("---- Function 6 executed successfully ----")
        print()
    elif z==7:
        cur.execute("select * from project1 order by grade;")
        result=cur.fetchall()
        for i in result:
            print(i)
        if len(result)==0:
            print('No record matches your conditions.')
        print("---- Function 7 executed successfully ----")
        print()
    ans=input("Do you wish to continue performing functions on the first table? (yes/no): ")
print("END OF FUNCTIONS ON FIRST TABLE")
print()
print("----- Student Table Records -----")
display('project1')
print()

#second table
print("-----Marks Management System Table-2-----")
print('''0. Skip Menu
1. Add a Student Record
2. Deleting a Student Mark Record
3. Modifying Student's Marks Record
4. Searching a record on the basis of S.No
5. Searching records on the basis of Average Marks
6. Searching records on the basis of Exam
7. Sorting records on the basis of Score''')
print()

ans2='yes'
while ans2=='yes':
    choice=int(input("Enter your choice: "))
    if choice==0:
        ans2='no'
        continue
    elif choice==1:            
        sno=int(input("Enter SNO: "))
        exam=input("Enter Exam: ")
        sub1=int(input("Enter exam percentage in sub1: "))
        sub2=int(input("Enter exam percentage in sub2: "))
        sub3=int(input("Enter exam percentage in sub3: "))
        average=(sub1+sub2+sub3)/3
        query='''insert into marks1 values({},'{}',{},{},{},{})'''.format(sno,exam,sub1,sub2,sub3,average)
        cur.execute(query)
        cur.commit()
        print("---- Function",choice,"executed successfully ----")
        print()
    elif choice==2:
        sno=input("Enter the student number of student whose record you'd like to delete: ")
        cur.execute("delete from marks1 where sno="+sno)
        display('marks1')
        print("---- Function",choice,"executed successfully ----")
        print()
    elif choice==3:
        sno=input("Enter the sno that you would like to change marks for: ")
        exam=input("Enter the exam you'd like to change marks for: ")
        sub=input("Enter the subject you'd like to change marks for: ")
        val=input("Enter the new value you'd like to set: ")
        query='''update marks1 set '{}'={} where sno={} and exam='{}';'''.format(sub,val,sno,exam)
        cur.execute(query)
        display('marks1')
        print("---- Function",choice,"executed successfully ----")
        print()
    elif choice==4:
        sno=input("Enter the student number of the student's mark record you'd like to search: ")
        select('marks1','sno',sno)
        print("---- Function",choice,"executed successfully ----")
        print()
    elif choice==5:
        avg=input("Enter the average marks of student you'd like to search for: ")
        select('marks1','average',avg)
        print("---- Function",choice,"executed successfully ----")
        print()
    elif choice==6:
        exam=input("Enter the exam you'd like to filter the data for: ")
        select('marks1','exam',exam)
        print("---- Function",choice,"executed successfully ----")
        print()
    elif choice==7:
        exam=input("Enter the exam on basis of which you'd like to order the data: ")
        cur.execute("select * from marks1 where exam='"+exam+"' order by exam;")
        print("---- Function",choice,"executed successfully ----")
        print()
    ans2=input("Would you like to continue performing functions on the second table (yes/no): ")
print("END OF FUNCTIONS ON SECOND TABLE")
print()
print("----- Marks Table -----")
display('marks1')
print()
print("The information of all the students along with their score is displayed below:")
cur.execute("select p.sno,p.name,p.fname,p.number,p.grade,p.section,m.exam,m.sub1,m.sub2,m.sub3,m.average from project1 p, marks1 m where p.sno=m.sno;")
result=cur.fetchall()
column=['Sno','Name',"Father's Name","Number","Grade","Section","Exam","Marks in Subject 1","Marks in Subject 2","Marks in Subject 3","Average"]
for i in result:
    for j in range(len(i)):
        print(column[j]+':',i[j])
    print('----- End of Record -----')
print()
print()
print("Thank you for using this software!")
print("- Abhinav & Faizaan")
con.commit()
con.close()