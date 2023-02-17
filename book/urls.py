from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.bookview, name='book'),
    path('book/<int:id>', views.book_detailview, name='details'),
]

