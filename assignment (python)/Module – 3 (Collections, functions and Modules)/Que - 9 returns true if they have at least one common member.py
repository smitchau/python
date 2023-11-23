'''
 Write a Python function that takes two lists and returns true if they have 
at least one common member.
'''
def lists(l1,l2):
    result = False
    for i in l1:
        for j in l2:
            if i == j:
                result = True
                return result
            return result

l1 = [1,2,3,4,5]
l2 = [5,6,7,8]
print(lists(l1,l2))
