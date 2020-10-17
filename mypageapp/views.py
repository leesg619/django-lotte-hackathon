from django.shortcuts import render
from django.contrib import auth
from mainapp.models import *
from .models import *
# Create your views here.
def post_search(request):
    return render(request, 'post_search.html')

def post_search_detail(request):
    return render(request, 'post_search_detail.html')
    
def timeline(request):
    mybox = Box.objects.filter(receiver = request.user.username)|Box.objects.filter(sender = request.user.username)
    state = State.objects.all()
    return render(request, 'timeline.html',{'mybox':mybox,'state':state,})  