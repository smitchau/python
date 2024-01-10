import sys

try:
    print(a)
except:
    print('something went wrong')
    print(sys.exc_info())
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])