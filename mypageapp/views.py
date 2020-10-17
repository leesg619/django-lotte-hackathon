from django.shortcuts import render

# Create your views here.
def post_search(request):
    return render(request, 'post_search.html')

def post_search_detail(request):
    return render(request, 'post_search_detail.html')
    
def timeline(request):
    return render(request, 'timeline.html')

def mypage(request):
    return render(request,'mypage.html')

def post_reservation(request):
    return render(request,'post_reservation.html')

def post_reserve_look(request):
    return render(request,'post_reserve_look.html')

def post_reserve_look_detail(request):
    return render(request,'post_reserve_look_detail.html')