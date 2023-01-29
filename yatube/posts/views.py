from django.shortcuts import render, get_object_or_404
from .models import Post, Group

LAST_TEN = 10


def index(request):
    posts = Post.objects.all()[:LAST_TEN]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,

    }
    return render(request, template, context)"""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:LAST_TEN]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
