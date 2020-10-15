from django.shortcuts import render

# Create your views here.
def post_search(request):
    return render(request, 'post_search.html')

def post_search_detail(request):
    return render(request, 'post_search_detail.html')
    
def timeline(request):
    return render(request, 'timeline.html')