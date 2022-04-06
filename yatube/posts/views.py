from django.shortcuts import render, get_object_or_404
from .models import Post, Group


POSTS_LIMIT: int = 10


def index(request):
    posts = (
        Post.objects
        .select_related('group', 'author')
        .all()[:POSTS_LIMIT])

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = (
        Post.objects
        .select_related('author')
        .filter(group=group)
        .all()[:POSTS_LIMIT])

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
