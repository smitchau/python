import pymysql

mydb = pymysql.connect(host='localhost',user='root',password='',database='topspython')
mycursor = mydb.cursor()

menu = """

                press 1 for add student
                press 2 for update student
                press 3 for search student
                press 4 for delete student
                press 5 for display student

"""

def addoperations():
    print("-------------------- ADD STUDENT ------------------------")
    name = input("Enter Name : ")
    subject = input("Enter Subject : ")

    args = (name,subject)
    query = "insert into student (name,subject) values ('%s','%s') "

    mycursor.execute(query % args)

    mydb.commit()

def updateoperations():
    print("-------------------- UPDATE STUDENT ------------------------")
    id = int(input("Which student do you want update enter id :"))
    name = input("Enter Update Name : ")
    subject = input("Enter Update Subject : ")

    query ="update student set name = '%s' , subject = '%s' where id = %s "
    args = (name,subject,id)
    mycursor.execute(query % args )
    mydb.commit()

def searchoperations():
    name = input("Enter Your Name :")
    query="select * from student where name='%s' "
    args = (name)

    mycursor.execute(query % args)
    res = mycursor.fetchone()
    print(res[0])
    print(res[1])
    print(res[2])

def deleteoperations():
    print("-------------------- DELETE STUDENT ------------------------")
    id = int(input("Which student do you want update enter id :"))
    query = "delete from student where id = %s "
    args = (id)
    mycursor.execute(query % args)
    mydb.commit()

def displayoperations():
    print("-------------------- DISPLAY STUDENT ------------------------")
    mycursor.execute("select * from student")
    res = mycursor.fetchall()
    for x in res:
        print(x)
    mydb.commit()
  
status = True

while status:
    print(menu)
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        addoperations()
        
    elif choice == 2:
        updateoperations()
        
   
    elif choice == 3:
        searchoperations()

    elif choice == 4:
        deleteoperations()

    elif choice == 5:
        displayoperations()

    user_choice = input("do you more operations perform 'y' or 'n' :")
    if user_choice == 'y':
        status = True
    else:
        status = False
