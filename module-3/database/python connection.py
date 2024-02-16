import pymysql

mydb = pymysql.connect(host = "localhost",user = "root" ,password = "")

mycursor = mydb.cursor()

mycursor.execute("create database if not exists mydb27")

mydb = pymysql.connect(host = "localhost",user = "root" ,password = "" , database = "mydb27")

mycursor = mydb.cursor()

mycursor.execute("create table if not exists python27 (id int primary key auto_increment , name varchar(20) , subject varchar(20))")

mydb.commit()