'''
Write a Python program to combine two dictionary adding values for 
common keys.
'''

#create three dictionary
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}
new_dict = d2    #d2 assign of new_dict

for key , value in d1.items():      # for loop traverse in d1
    if key in d2:                   #condition are key is present in d2 suppose yes
        new_dict[key] = value + d2[key]     # d1 value + d2 key

    else:                            
        new_dict[key] = value               # else print value

print(new_dict)


# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).
