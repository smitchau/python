'''
list.append(x) :  Add an item to the end of the list.

list.extend(L) : Appends the contents of L to list
'''

list = ['python','java','c++','c','html']
list2 = []

print('before list : ',list)

list.append('smit')

print('after list using append : ',list)

list2.extend(list)

print('after list2 extend list : ',list2)
