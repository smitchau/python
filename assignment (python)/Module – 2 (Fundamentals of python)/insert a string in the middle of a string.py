str1 = "hello world"

str2 = "good"

half = int(len(str1)/2)

new = str1[0:half]+" "+str2+str1[half:len(str1)]

print(new)
