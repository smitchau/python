#multiple inheritance

#create first class (parent1)
class parent1:

    def __init__(self,x,y):
        self.n1 = x
        self.n2 = y

    def sum(self):
        print("sum is : ",self.n1+self.n2)

#create second class (parent2)
class parent2:

    def mul(self):
        print("mul is : ",self.n1*self.n2)
        
#create third class (child)
class child(parent1,parent2):

    def display(self):
        print("child class")

#create object of third class
obj = child(12,23)

obj.sum()  #function call of first class
obj.mul()   #function call of second class
obj.display() # function call of third class
