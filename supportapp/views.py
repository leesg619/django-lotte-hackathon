from django.shortcuts import render

# Create your views here.

def custom_voice(request):
    return render(request, 'custom_voice.html')

def custom_voice_new(request):
    return render(request, 'custom_voice_new.html')

def custom_voice_detail(request):
    return render(request, 'custom_voice_detail.html')