import mysql.connector as sql
con=sql.connect(host="localhost",user='root',password='faizaan',database='faizaan')
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
con.commit()
con.close()