#Write a Python script to sort (ascending and descending) a dictionary by value. 

dict = {1:'python',5:'java',2:'c++'}   #create a dictionary

dict_sorted = sorted(dict.items())

print("Before shorting a ascending dictionary by value :\n",dict)

print("\nafter shorting a ascending dictionary by value:\n",dict_sorted)

print("\nafter shorting a descending dictionary by value:\n",dict_sorted[::-1])

'''
li1 = []  #create a list

for i in dictionary.values():    #insert dictionary values in list 
    li1.append(i)
  
print("after shorting a ascending dictionary by value:",li1)

for i in range(len(li1)):                #sorting perform
    for j in range(i+1,len(li1)):

        if li1[i] > li1[j]:

            li1[i],li1[j] = li1[j],li1[i]

print("after shorting a ascending dictionary by value: ",li1)

for i in range(len(li1)):
    for j in range(i+1,len(li1)):

        if li1[i] < li1[j]:

            li1[i],li1[j] = li1[j],li1[i]

print("after shorting a descending dictionary by value: ",li1)

  '''


