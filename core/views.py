from django.shortcuts import render, redirect
from blog.models import Post
import requests
title = ''
# Create your views here.

def frontpage(request):
    title = 'Home'
    post = Post.objects.all().order_by('-created_at').filter(status=Post.ACTIVE)
    context = {'title':title, 'posts':post}
    return render(request, 'core/frontpage.html', context)


def about(request):
    response = requests.get('https://api.github.com/users/azzam911/repos')
    if response.status_code == 200:
        repos = response.json()
    title = 'about'
    context = {'title' : title, 'repos': repos}
    return render(request, 'core/about.html', context)



def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")