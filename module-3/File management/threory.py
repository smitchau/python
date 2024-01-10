'''
    r : read
    w : write
    a : append

    x: create blank file

'''
#==================Write the file ============================

f = open('Myfile.txt','w')
f.write('hello smit')
f.close()

#===============Read the file ===========================

f = open("Myfile.txt",'r')
print(f.read())




