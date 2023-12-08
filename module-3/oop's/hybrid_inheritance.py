#hybrid inheritance

#create first class (parent)
class parent:

    def __init__(self,x,y):
        self.n1 = x
        self.n2 = y

    def sum(self):
        print("sum is : ",self.n1+self.n2)

#create second class (child1)
class child1(parent):

    def mul(self):
        print("mul is : ",self.n1*self.n2)
        
#create third class (child2)
class child2(parent):

    def display(self):
        print("child2 class")

#create four class (child3)
class child3(child1,child2):

    def ditails(self):
        print("sub child 3 class")

obj = child3(20,30)  #create obj of four class
obj.ditails()           #four class ditail function call
obj.mul()               #second class mul function call
obj.display()           #third class display function call
obj.sum()               #first class sum fuction call
