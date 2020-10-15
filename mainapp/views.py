from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,"main.html")

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request, 'signup.html')