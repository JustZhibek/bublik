from django.http import HttpResponse
from django.shortcuts import render

def hello_view(request):
    return HttpResponse('<h1>Hello,u are cute</h1>')


def blog_viev(reguest):
    blog = models.Post.objects.all()
    return render(reguest, 'blog.html', {'blog': blog})