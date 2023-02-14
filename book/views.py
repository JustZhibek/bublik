from django.http import HttpResponse
from django.shortcuts import render

def hello_view(request):
    return HttpResponse('<h1>hey, hello</h1>')


def book_viev(reguest):
    book = models.lost.objects.all()
    return render(reguest, 'book.html', {'book': book})