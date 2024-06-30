import mysql.connector as a
con= a.connect(host="localhost",user="root",password='manjima12',database="Library")

def addbook():
    bn=input("Enter the name of the book")
    c=input("Enter the code of the book")
    s=input("Enter the subject of the book")
    t=int(input("Enter total num of books"))
    data=(bn,c,s,t)
    sql='insert into books values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit
    print(">...........................<")
    print("Data entered Successfully")
    main()
def issueb():
    n=input("Enter for whom it is issued")
    r=int(input("Enter registration number"))
    c=input("Enter the code of the book")
    s=input("Enter the subject of the book")
    d=input("Enter the date of issue")
    a='insert into issue values(%s,%s,%s,%s,%s)'
    data=(n,r,c,s,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit
    print(">...........................<")
    print("Book issued to:",n)
    bookup(co,-1)
def submit():
    n=input("Enter submitted by")
    r=int(input("Enter registration number"))
    c=input("Enter the code of the book")
    s=input("Enter the subject of the book")
    d=input("Enter the date of submission")
    a='insert into Submit values(%s,%s,%s,%s,%s)'
    data=(n,r,c,s,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit
    print(">...........................<")
    print("Book submitted from:",n)
    bookup(co,-1)
def bookup(co,u):
    a="select Total from books where CODE=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL=%s where CODE=%s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()
def dbook():
    ac=input("Enter Book Code")
    a="delete from books where CODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("Successfully Deleted")
    main()
def displaybook():
    a="select * from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name",i[0])
        print("Book Code",i[1])
        print("Total",i[3])
        print(">.....................<")
        main()
def main():
    print("Library Manager, 1 for Add Book,2 for Issue Book, 3 for Submit book, 4 for delete books and 5 for display book")
    ch=int(input("Enter your choice"))
    if(ch==1):
        addbook()
    elif(ch==2):
        issueb()
    elif(ch==3):
        submit()
    elif(ch==4):
        dbook()
    elif(ch==5):
        displaybook()
    else:
        print("wrong choice")
pw=input("enterpassword")
if pw=='manjima12':
    main()
else:
    print("wrong password")
   
