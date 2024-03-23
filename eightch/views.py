from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from .forms import toukouForm, threadForm, otoiawaseForm
from django.views.generic import FormView, ListView
from django.views.generic.list import ListView
from .models import Toukou, Thread, Otoiawase
from django.urls import reverse
from django.core.mail import EmailMessage

def otoiawasepost(request):
    if request.POST:
        title = request.POST['title']
        time = request.POST['time']
        username = request.POST['username']
        mailadd = request.POST['mailadd']
        text = request.POST['text']
        
    emailMessage = EmailMessage(
        to=[mailadd],
        subject=('自動返信メール:' + title),
        body=('内容：\n' + text + '\n承りました。\n返信はこのメールアドレスで行われますので、\nこのメールは大事に保管してください。'),
    )
    # send 関数を呼び出してメールを送信する
    emailMessage.send()

    otoiawase = Otoiawase(time=time, username=username, text=text, mailadd=mailadd, title=title)
    otoiawase.save()
    return HttpResponseRedirect(reverse('eightch:otoiawase'))

def threadpost(request):
    if request.POST:
        title = request.POST['title']
        time = request.POST['time']
        username = request.POST['username']

    thread = Thread(title=title, time=time, username=username)
    thread.save()
    return HttpResponseRedirect(reverse('eightch:threadtoukouview'))

def toukoupost(request, threadid):
    if request.method == 'POST':
        username = request.POST['username']
        time = request.POST['time']
        text = request.POST['text']
        threadid = request.POST['threadid']
        image = request.FILES.get('image')

        qs = Toukou.objects.filter(thread_id = threadid).count()

        thread_id = threadid

        if qs is None:
            toukou_id = int(1)
        else:
            toukou_id = int(qs + 1)
            
    elif request.method != 'POST':
        return HttpResponseRedirect('/')

    toukou = Toukou(username=username, time=time, text=text, thread_id=thread_id, toukou_id=toukou_id, image=image)
    toukou.save()
    return HttpResponseRedirect(reverse('eightch:threadtextview', kwargs={'threadid': threadid}))

def threadListView(request):
    template_name = "thread_list.html"
    ctx = {}
    qs = Thread.objects.all()
    ctx['object_list'] = qs
    return render(request, template_name, ctx)

def threadTextView(request):
    template_name = "base.html"
    ctx = {}
    qs = Thread.objects.all()
    ctx['object_list'] = qs
    return render(request, template_name, ctx)

class ThreadToukouView(ListView, FormView):
    template_name = 'thread_toukou.html'
    model = Thread
    form_class = threadForm
    #success_url = 'toukou_ok/'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,'送信しました！')
        title = form.cleaned_data['title']
        username = form.cleaned_data['username']
        time = form.cleaned_data['time']
        # メール送信などを行う
        print(title, username, time)
        return super().form_valid(form)
    
    def threadListView(request):
        template_name = "thread_list.html"
        ctx2 = {}
        qs2 = Thread.objects.all()
        ctx2['object_list2'] = qs2
        return render(request, template_name, ctx2)

class ThreadTextView(ListView, FormView):
    template_name = 'thread_text.html'
    model = Thread
    context_object_name = 'threadtext'
    form_class = toukouForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,'送信しました！')
        username = form.cleaned_data['username']
        time = form.cleaned_data['time']
        text = form.cleaned_data['text']
        thread_id = form.cleaned_data['thread_id']
        toukou_id = form.cleaned_data['toukou_id']
        # メール送信などを行う
        print(username, time, text, thread_id, toukou_id)
        return super().form_valid(form)

    def threadListView(request):
        template_name = "thread_text.html"
        ctx = {}
        qs = Toukou.objects.all()
        ctx['object_list'] = qs
        return render(request, template_name, ctx)

    def get_context_data(self,**kwargs):
        context = super(ThreadTextView, self).get_context_data(**kwargs)
        context.update({
            'object_list2': Toukou.objects.all(),
            'object' : Thread.objects.get(id=self.kwargs['threadid']),
            'threadid' : self.kwargs['threadid']
        })
        return context

    def get_success_url(self):
        return reverse('eightch:threadtextview', kwargs={'threadid': self.kwargs['threadid']})
    
class ThreadView(ListView):
    template_name = 'home.html'
    model = Thread
    context_object_name = "threades"
    form_class = threadForm
    success_url = '/home'

    def threadListView(request):
        template_name = "home.html"
        ctx = {}
        qs = Thread.objects.all()
        ctx['object_list'] = qs
        return render(request, template_name, ctx)
    
class OtoiawaseView(ListView, FormView):
    template_name = 'otoiawase.html'
    model = Otoiawase
    form_class = otoiawaseForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS,'送信しました！')
        title = form.cleaned_data['title']
        username = form.cleaned_data['username']
        mailadd = form.cleaned_data['mailadd']
        time = form.cleaned_data['time']
        text = form.cleaned_data['text']
        # メール送信などを行う
        print(title, username, time, text, mailadd)
        return super().form_valid(form)