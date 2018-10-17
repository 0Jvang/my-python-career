import markdown, datetime
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post, Category

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    dayMax = 30
    months = [1, 3, 5, 7, 8, 10, 12]
    if int(month) in months:
        dayMax = 31
    post_list = Post.objects.filter(
        created_time__range=(
            datetime.date(int(year), int(month), 1),
            datetime.date(int(year), int(month), dayMax)
            ))
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})
