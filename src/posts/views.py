from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def post_create(request):
    return HttpResponse("<h1>Hello from create</h1>")

def post_detail(request):
    instance = get_object_or_404(Post, id=2)
    context = {
        "instance": instance,
        "title": instance.title
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "list"
    }
    return render(request, "index.html", context)
    # return HttpResponse("<h1>Hello from list</h1>")

def post_update(request):
    return HttpResponse("<h1>Hello from update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello from delete</h1>")