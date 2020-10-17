from django.shortcuts import render,redirect, get_object_or_404 
from mainapp.models import *
from .models import *
# Create your views here.

def custom_voice(request):
    a = reversed(Qna.objects.all())
    return render(request, 'custom_voice.html', {'qna': a})

def custom_voice_new(request):
    aa = Qna.objects.filter(user = request.user)
    if request.method == 'POST':
        qna = Qna()
        qnacontent = request.POST['q_content']
        qnatitle = request.POST['q_title']
        # qnatype = request.POST.get('q_type')
        # qnaboxcode = request.POST.get('q_boxcode')
        # qnatime = request.POST.get('q_time')
        #qnapublic = request.POST.get('public')
        #picture = request.FILES('picture')

        qna.q_content = qnacontent
        qna.q_title = qnatitle
        # qna.qnatype =qnatype
        # qna.qnaboxcode =qnaboxcode 
        # qna.qnatime =qnatime 
        #qna.qnapublic =qnapublic
        #qna.qna =qna
        qna.user = request.user
        qna.save()
        return redirect('custom_voice')
    return render(request, 'custom_voice_new.html')



def custom_voice_detail(request, pk):
    #if request.method == 'GET':
    aa = get_object_or_404(Qna, pk = pk)
    #post_id = request.POST.get('post_id') #히든인풋을 post_id로 저장
    #aa = Qna.objects.POST.get(id = post_id)
    return render(request, 'custom_voice_detail.html',{'aa':aa})