from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,"index.html")

def about(request):
	return render(request,"about.html")

def signup(request):
	return render(request,"signup.html")

def signin(request):
	return render(request,"signin.html")

def blog(request):
	return render(request,"blog.html")

def contact(request):
	return render(request,"contact.html")

def price(request):
	return render(request,"price.html")

def service(request):
	return render(request,"service.html")

def single(request):
	return render(request,"single.html")