import os

if os.path.exists('Myforder'):          #curent path in curent forder exist condition check
    print("Already exists")
    os.rmdir('Myforder')             #remove forder
else:
    os.mkdir('Myforder')      #create new forder
    print("created")