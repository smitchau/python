# Write a Python program to count the occurrences of each word in a given sentence


str = "i have a 5 pen and i have a one book"

counts = {}

words = str.split()

for i in words:
     if i in counts:
          counts[i] += 1
     else:
         counts[i] = 1
print(counts)


    
