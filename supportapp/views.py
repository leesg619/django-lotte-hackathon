from django.shortcuts import render,redirect, get_object_or_404 
from mainapp.models import *
from .models import *
from django.contrib import auth
# Create your views here.

def custom_voice(request):
    a = reversed(Qna.objects.all())
    return render(request, 'custom_voice.html', {'qna': a})

def custom_voice_new(request):
    
    if request.method == 'POST' and 'pic' in request.FILES:
        aa = Qna.objects.filter(user = request.user)
        qna = Qna()
        qnacontent = request.POST.get('q_content')
        qnatitle = request.POST.get('q_title')
        #qnatype = request.POST.get('q_type')
        qnaboxcode = request.POST.get('q_boxcode')
        qnatime = request.POST.get('q_time')
        qnapublic = request.POST.get('public')
        pic = request.FILES['pic']

        qna.q_content = qnacontent
        qna.q_title = qnatitle
        # qna.qnatype =qnatype
        qna.q_boxcode =qnaboxcode 
        qna.q_time =qnatime 
        qna.public =qnapublic
        qna.pic = pic
        qna.user = request.user
        qna.save()
        return redirect('custom_voice')

    elif request.method == 'POST':
        aa = Qna.objects.filter(user = request.user)
        qna = Qna()
        qnacontent = request.POST.get('q_content')
        qnatitle = request.POST.get('q_title')
        #qnatype = request.POST.get('q_type')
        qnaboxcode = request.POST.get('q_boxcode')
        qnatime = request.POST.get('q_time')
        qnapublic = request.POST.get('public')
        

        qna.q_content = qnacontent
        qna.q_title = qnatitle
        # qna.qnatype =qnatype
        qna.q_boxcode =qnaboxcode 
        qna.q_time =qnatime 
        qna.public =qnapublic
        
        qna.user = request.user
        qna.save()
        return redirect('custom_voice')
    return render(request, 'custom_voice_new.html')



def custom_voice_detail(request, pk):
    #if request.method == 'GET':
    aa = get_object_or_404(Qna, pk = pk)
    aa.today = aa.today +1
    aa.save()
    #post_id = request.POST.get('post_id') #히든인풋을 post_id로 저장
    #aa = Qna.objects.POST.get(id = post_id)
    return render(request, 'custom_voice_detail.html',{'aa':aa})


def deletevoice(request): 
    post_id = request.GET['post_id'] 
    post = Qna.objects.get(id = post_id)
    post.delete() #타이틀이나 컨텐츠 저장할 필요없이 삭제만 해주면됨
    return redirect( 'custom_voice')