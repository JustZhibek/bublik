from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ProductListView(ListView):
    # queryset = models.Product.objects.filter().order_by('-id')
    queryset = models.Product.objects.filter(tags__name="Рубашка")

    template_name = "cloth_list.html"

    def get_queryset(self):
        return models.Product.objects.filter(tags__name="Рубашка")


class ProductDetailView(DetailView):
    template_name = "cloth_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product_id)


class OrderCreateView(CreateView):
    template_name = "add-order.html"
    form_class = forms.OrderForm
    success_url = "/cloth/"
    queryset = models.Order.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)

