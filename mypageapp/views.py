from django.shortcuts import render, redirect
from django.contrib import auth
from mainapp.models import *
from .models import *
# Create your views here.
def post_search(request): 
    return render(request, 'post_search.html')

def post_search_detail(request):
    code = request.POST["code"]
    box = Box.objects.filter(code = code)
    if not box:
        return render(request,'post_search.html',{'error':'존재하지 않는 송장번호입니다.'})
    else :
        state = reversed(State.objects.filter(box = box[0]))
        return render(request,'post_search_detail.html',{'box':box,'state': state})
    
def timeline(request):
    mybox = Box.objects.filter(receiver = request.user.username)|Box.objects.filter(sender = request.user.username)
    state = State.objects.all()
    return render(request, 'timeline.html',{'mybox':mybox,'state':state,})  

def mypage(request):
    return render(request,'mypage.html')

def post_reservation(request):
    return render(request,'post_reservation.html')

def post_reserve_look(request):
    return render(request,'post_reserve_look.html')

def post_reserve_look_detail(request):
    return render(request,'post_reserve_look_detail.html')
