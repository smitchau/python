
li1 = ['fruit','color']
li2 = []

print('ENTER any 5 FRUITS AND COLOR')

for i in range(1,6):
   items = input('Enter fruit or color :')
   li2.append(items)

fruits = ['melon', 'apple', 'orange', 'banana', 'citrus', 'plum', 'mandarin']
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange','black','white']

fruits_list = []
color_list = []

dic1 = {}

for i in li2:
   if i in fruits:
      fruits_list.append(i)
   else:
      color_list.append(i)

for i in li1:
   if i == 'fruit':
      dic1[i] = fruits_list
   elif i == 'color':
      dic1[i] = color_list

print(dic1)
      
