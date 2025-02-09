from django.shortcuts import render
from blogs.models import Blog

# Create your views here.
def blog_list(request):
    blogs=Blog.objects.all()
    return render (request, "blogs.html", {"blogs":blogs})

def blog_detail(request, id):
    blog=Blog.objects.get(id=id)
    return render (request, "blog_detail.html", {"blog":blog})