import pymysql

#____________________________________________ connection class ____________________________________________________

class connection:
    mydb = pymysql.connect(host = 'localhost',user = 'root',password='')

    mycursor = mydb.cursor()

    mucursor.execute('create database if not exists banking')

    mydb = pymysql.connect(host = "localhost",user = "root" ,password = "" , database = "banking")
    
    mycursor = mydb.cursor()

    mycursor.execute('create table if not exists banker (ac_no int primary key , name varchar(20) , balance int')

    mydb.commit()

#____________________________________________bank class____________________________________________________________

class banker:
