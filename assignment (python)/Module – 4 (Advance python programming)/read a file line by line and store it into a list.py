#Write a Python program to read a file line by line and store it into a list

try:
    # Display the list of lines read from the file
    file = open('studentinfo.txt','r')

    lines = file.readlines()

    print(lines)

    file.close()
    
except FileNotFoundError:
    print("File not found. Please provide the correct file.")
    
except Exception as e:
    print("An error occurred:", e)

