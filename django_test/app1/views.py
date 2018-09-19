import time
from app1.models import Test, User
from app1.forms import LoginForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView


# Create your views here.
def home(request):
    return redirect('https://www.baidu.com')


def test1(request):
    return HttpResponse('hello world')


def test2(request):
    now = time.ctime()
    login_form = LoginForm()
    method = request.method
    if method == 'GET':
        return render(request, 'test/test.html', {'time':now, 'form':login_form})
    else:
        # name = request.POST['name']
        # password = request.POST['password']
        params = request.POST.dict()
        form = LoginForm(params)
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse('登录成功')
        return HttpResponse('请重新输入')


def test3(request, num):
    id = num
    data = User.objects.filter(id=id)
    return render(request, 'test/Test2.html', {'data': data})


# 类视图
class Test1(TemplateView):
    template_name = 'test/Test1.html'


class Test2(ListView):
    model = User
    template_name = 'test/Test2.html'
    context_object_name = 'data'


class Test3(DetailView):
    model = User
    template_name = 'test/Test3.html'
    context_object_name = 'data'


class Test4(CreateView):
    model = User
    template_name = 'test/Test4.html'
    context_object_name = 'form'
    fields = '__all__'
    success_url = 'http://127.0.0.1:8000/Test4/?'
