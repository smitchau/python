from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.urls import reverse
"""
    Django ORM(object relational method)

    get() : data retrive karna ho to get method aati hai , fetch data from model and return object but only single records
        if there are multiple record found with given condition it will thrown an exception

"""

# Create your views here.
def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairmen.objects.get(userid = uid)
        context = {
                'uid' : uid,
                'cid' : cid, 
            }
        return render(request,'myapp/index.html',context)
    else:
        return render(request,'myapp/login.html')

def login(request):
    if "email" in request.session:
        return HttpResponseRedirect(reverse("home"))
        """uid = User.objects.get(email = request.session['email'])
        cid = Chairmen.objects.get(userid = uid)
        context = {
                'uid' : uid,
                'cid' : cid, 
            }
        return render(request,'myapp/index.html',context)"""
    else:
        if request.POST:
            try:
                print("------------ page loaded")
                p_email = request.POST["email"]
                print("------------>> email ",p_email)
                p_password = request.POST["password"]
                print("-----> password",p_password)
                uid = User.objects.get(email = p_email ,password = p_password)
                print("=============================>>> object ",uid)
                print("---------->",uid.role)
                cid = Chairmen.objects.get(userid = uid)
                print("------------->firstname",cid.firstname)

                request.session['email'] = uid.email
                return HttpResponseRedirect(reverse("home"))
                #return render(request,"myapp/login.html")
                #context = {
                #    'uid' : uid,
                #    'cid' : cid, 
                #}
                #return render(request,"myapp/index.html",context)
            except Exception as e:
                print("----------------------------->Email",e)
                msg = "Invalid Email or password"
                return render(request,"myapp/login.html",{'e_msg':msg})
                pass
        else:
            print("----> page loaded")
            return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        #return render(request,"myapp/login.html")
        return HttpResponseRedirect(reverse("login"))
    else:
        #return render(request,"myapp/login.html") 
        return HttpResponseRedirect(reverse("login"))   
            
