'''

    There are 2 types of exception

    1) built - in exception
    2) user defined or custome exceptions :

        which is create by user and we can call as per requirment 
        
'''

class MyException(Exception):
    pass

try:
    num = int(input('Enter num : '))
    if num < 0:
        raise MyException
    
except MyException:
    print('number must be positive')