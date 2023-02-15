from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User

QUANTITIES_POSTS = 10

def pag(posts, request):
    paginator = Paginator(posts, QUANTITIES_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def index(request):
    posts = Post.objects.all()
    page_obj = pag(posts, request)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)



# def index(request):
#     posts = Post.objects.all()[:QUANTITIES_POSTS]
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    page_obj = pag(posts, request)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)

"""
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:QUANTITIES_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
"""


def profile(request, username):
    author = get_object_or_404(User, username=username)
    author_posts = author.posts.all()
    posts_count = author.posts.count()
    page_obj = pag(author_posts, request)
    context = {
        'author': author,
        'posts': author_posts,
        'posts_count': posts_count,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts_count = post.author.posts.count()
    title = post.text[0:30]
    context = {
        'posts': post,
        'posts_count': posts_count,
        'title': title,
    }
    return render(request, 'posts/post_detail.html', context)
