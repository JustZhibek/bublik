from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

#не полная инфа

def bookview(request):
    book = models.Lost.objects.all()
    return render(request, 'book.html', {'book': book})

#полная инфа

def book_detailview(request, id):
    book_id = get_object_or_404(models.Lost, id=id)
    return render(request, 'book_detail.html', {'book_id': book_id})

def create_book_view(request):
    method = request.method
    if method == 'POST':
        form = forms.LostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>книга успешно добавлена!!!</h2>')

    else:
        form = forms.LostForm()

    return render(request, 'add_book.html', {'form': form})


#изменение данных
def update_book_view(request, id):
    book_object = get_object_or_404(models.LostForm, id=id)
    if request.method == 'POST':
        form = forms.LostForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Фильм успешно обновлен!</h2>')
    else:
        form = forms.LostForm(instance=book_object)

    return render(request, 'update_book.html', {
        'form': form,
        'object': book_object
    })

    # Удаление из базы


def delete_book_view(request, id):
    book_object = get_object_or_404(models.Lost, id=id)
    book_object.delete()
    return HttpResponse('<h2>книга успешно удалена</h2>')