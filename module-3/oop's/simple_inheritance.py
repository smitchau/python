#simple inheritance

#create first class
class parent:

    def __init__(self,x,y):
        self.n1 = x
        self.n2 = y

    def sum(self):
        print("sum is : ",self.n1+self.n2)

#create second class
class child(parent):

    def display(self):
        print("child class")

#create obj of second class
obj = child(12,23)

obj.sum() #function call of first class use second class obj
obj.display() #function call of second class
