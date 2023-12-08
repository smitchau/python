#multilevel inheritance

#create first class (parent1)
class parent:

    def __init__(self,x,y):
        self.n1 = x
        self.n2 = y

    def sum(self):
        print("sum is : ",self.n1+self.n2)

#create second class (child)
class child(parent):

    def mul(self):
        print("mul is : ",self.n1*self.n2)

#create third class (sub_child)
class sub_child(child):

    def display(self):
        print("child class")
    
obj = sub_child(12,23) #create object of third class (sub_child)

obj.sum()    #first class function call use obj
obj.mul()   #second class function call use obj
obj.display()   #third class function call use obj
