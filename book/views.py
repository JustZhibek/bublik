from django.shortcuts import render, get_object_or_404
from . import models

#не полная инфа

def bookview(request):
    book = models.Lost.objects.all()
    return render(request, 'book.html', {'book': book})

#полная инфа

def book_detailview(request, id):
    book_id = get_object_or_404(models.Lost, id=id)
    return render(request, 'book_detail.html', {'book_id': book_id})