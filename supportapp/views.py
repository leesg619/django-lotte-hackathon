from django.shortcuts import render,redirect, get_object_or_404 
from mainapp.models import *
from .models import *
# Create your views here.

def custom_voice(request):
    a = reversed(Qna.objects.all())
    return render(request, 'custom_voice.html', {'qna': a})

def custom_voice_new(request):
    aa = Qna.objects.filter(user = request.user)

    if request.method == 'GET'  :
        
        qna = Qna()

        qnacontent = request.POST.get('q_content')
        qnatitle = request.POST.get('q_title')
        # qnatype = request.POST.get('q_type')
        # qnaboxcode = request.POST.get('q_boxcode')
        # qnatime = request.POST.get('q_time')
        #qnapublic = request.POST.get('public')
        #picture = request.FILES('picture')

        qna.qnacontent = qnacontent
        qna.qnatitle = qnatitle
        # qna.qnatype =qnatype
        # qna.qnaboxcode =qnaboxcode 
        # qna.qnatime =qnatime 
        #qna.qnapublic =qnapublic
        #qna.qna =qna
        qna.user = request.user

        qna.save()
        return render(request,'custom_voice_new.html', {
        'done' : '문의 등록이 완료되었습니다.',
        'qna' : aa
        })


def custom_voice_detail(request):
    return render(request, 'custom_voice_detail.html')