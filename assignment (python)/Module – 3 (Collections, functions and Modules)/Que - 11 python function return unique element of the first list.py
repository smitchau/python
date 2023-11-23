''' Write a Python function that takes a list and returns a new list with unique 
elements of the first list. '''

def unique():
    li = [1,1,2,3,3,3,3,4,4,5,6,7,5,8]
    unique_list = []
    for i in li:
       if i not in unique_list:
            unique_list.append(i)
    print('new list :',unique_list)
unique()
