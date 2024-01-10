import os 
import datetime

current_datetime = datetime.datetime.now()   
    
formatted_date = current_datetime.strftime("%d-%m-%Y")
formatted_time = current_datetime.strftime("%H-%M-%S")

filename = f"{formatted_date}__{formatted_time}.txt"

name = input("Enter your Name:- ")
age = int(input("Enter your Age:- "))
mo = int(input("Enter your Contect no:- "))
vacine = input("Enter your vacine Name:- ")
doze = int(input("Enter your vacine doze:- "))

with open(f"vaccination/{filename}",'w') as data:
        data.write("\n\t\tVaccination Report")
        data.write("\n==============================================")
        data.write(f"\nName is :- {name}")
        data.write(f"\nAge is :- {str(age)}")
        data.write(f"\nAge is :- {str(mo)}")
        data.write(f"\nvacine Name is:- {vacine}")
        data.write(f"\nvacine Doze is:- {str(doze)}")
        
print(f"File '{filename}' created with the vaccine data.")
