from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="products"),
    path("products/<int:id>/", views.ProductDetailView.as_view(), name="detail"),
    path("add-order/", views.OrderCreateView.as_view(), name="add"),
]
