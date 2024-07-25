from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Order

# Create your views here.


class ItemListView(ListView):
    template_name = 'items_list.html'

    def get_queryset(self):
        model = self.kwargs['model']
        if model == 'products':
            return Product.objects.all()
        elif model == 'orders':
            return Order.objects.all()


class ItemDetailView(DetailView):
    template_name = 'item_detail.html'

    def get_object(self):
        model = self.kwargs['model']
        pk = self.kwargs['pk']
        if model == 'products':
            return Product.objects.get(pk=pk)
        elif model == 'orders':
            return Order.objects.get(pk=pk)
