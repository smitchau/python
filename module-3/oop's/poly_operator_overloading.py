# operator overloading

class sample:
    
    def __init__(self,x):
        self.num = x
        
    def sub(self,new_obj):
        return self.num - new_obj.num
    
c1 = sample(24)
c2 = sample(6)

print(c1.sub(c2))
