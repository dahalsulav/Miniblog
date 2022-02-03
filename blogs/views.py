from django.shortcuts import render
from blogs.models import Post


def bloglist(request):
    post = Post.objects.all()
    context = {
        'bloglist':post
    }
    return render(request, "blogs/bloglist.html",context)

def blogdetails(request,id):
    singlepost = Post.objects.get(id = id)
    context = {
        'blogdetails':singlepost
    }
    return render(request, "blogs/blogdetails.html",context)
