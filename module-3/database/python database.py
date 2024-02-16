import pymysql

mydb = pymysql.connect(host = "localhost",user = "root" ,password = "" , database = "mydb27")
mycursor = mydb.cursor()

while True:
    data = '''
        1)insert operations
        2)view operations
        3)update operations
        4)delete operations
    '''
    print(data)

    choice = int(input('Enter your choice : '))

    if choice==1:
        name = input('Enter name :')
        subject = input('Enter Subject : ')

        query = "insert into python27(name,subject) values('%s','%s')"
        args = (name,subject)

        mycursor.execute(query%args)
        mydb.commit()
    
    elif choice==2:
        query = "select * from python27"
        mycursor.execute(query)

        mycursor.execute(query)
        mydb.commit()
    
    elif choice==3:
        id = int(input("enter the id number of record you want to update"))
        name = input("Enter name : ")
        subject = input("Enter subject : ")

        query = "alter table python27 set  name='%s' , subject='%S' where id='%s'"
        args = (name,subject,id)
        mycursor.execute(query%args)
        mydb.commit()

    elif choice==4:
        id = int(input("Enter the id number of the record you want to delete"))
        query = "delete from  python27 where id='%s'"
        args = (id)
        mycursor.execute(query % args)
        mydb.commit()

    lchoice = "do you perform more operations 'y' for yes or 'n' for no:"
    if lchoice == 'y':
        pass
    else:
        break
