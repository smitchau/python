# access dictionary

d1 = {'k1':1,'k2':2,'k3':'hello'}

d2 = {'k2':67,'k5':90}

print("\nd1 dict :",d1)
print("\nd2 dict :",d2)
#return value hold by key
print("\nsingle element access use key : ",d1['k1'])

#value assignment / or can change (dicts are muteble)
d1['k4']= 78

print("new assign element : ",d1)
#update the dictionary

d1.update(d2)


print("update dict",d1)

#copy one dict to another

dx = {'k1':90,'k2':3}
dx = d2.copy()

print("copy dictionary : ",dx)

