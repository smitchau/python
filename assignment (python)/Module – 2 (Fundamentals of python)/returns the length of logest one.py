'''
Write a Python function that takes a list of words and returns the length 
of the longest one

'''
# create a list
l1 = ['one','two','three','four','five','six','chauhan','seven','eight']

# variable to store the longest word
logest_word = ''

# use loop to find the longest word
for word in l1:
    if len(word) > len(logest_word):
        logest_word = word
  
print(logest_word)
