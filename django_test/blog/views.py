from django.shortcuts import render
from .models import Post, User

# Create your views here.
def home(request, username):
    post_list = Post.objects.all()
    hot_post_list = Post.objects.all().order_by('-views')
    user = User.objects.filter(name=username).first()
    data = {
        'post_list': post_list,
        'hot_post_list': hot_post_list,
        'user': user
    }
    if request.method == 'GET':
        return render(request, 'blog/home.html', data)

def article(request):
    if request.method == 'GET':
        return render(request, 'blog/article.html')


def about(request):
    if request.method == 'GET':
        return render(request, 'blog/about.html')

def timeline(request):
    if request.method == 'GET':
        return render(request, 'blog/timeline.html')

def resource(request):
    if request.method == 'GET':
        return render(request, 'blog/resource.html')

def detail(request, pk):
    if request.method == 'GET':
        return render(request, 'blog/detail.html')
