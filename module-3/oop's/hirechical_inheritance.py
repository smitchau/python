#hirechical inheritance

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
        print("child class")
    
obj = child1(12,23) #create obj of second class (child1)
obj.sum()           #sum function call in use second class obj
obj.mul()           #mul function call in use second class obj   

obj = child2(20,30) #create obj of third class (child2)
obj.sum()           #sum function call in use third class obj
obj.display()       #display function call in use third class obj
