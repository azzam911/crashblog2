from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
title = ''
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    title = slug
    return render(request, 'blog/detail.html', {'post':post, 'title': title})

def category(request, slug):
    title = slug
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status= Post.ACTIVE)
    return render(request, 'blog/category.html', {'posts':posts, 'title': title})


def search(request):
    title = 'search'
    query = ''
    if request.method == 'GET':
        query = request.GET['query']
    query = query.strip()
    posts = Post.objects.filter(Q(title_ar__icontains=query) | Q(title__icontains=query) , status= Post.ACTIVE)
    return render(request, 'blog/search.html', {'posts': posts,'query':query, 'title': title})