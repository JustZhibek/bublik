from django.urls import path
from . import views

urlpatterns = [
    path("clothes/", views.ProductListView.as_view(), name="clothes"),
    path("clothes/<int:id>/", views.ProductDetailView.as_view(), name="detail"),
    path("add-order/", views.OrderCreateView.as_view(), name="add"),
]