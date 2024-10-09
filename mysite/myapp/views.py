from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    context = {'items': Product.objects.all()}
    return render(request, 'index.html', context = context)

def index_item(request, id):
    product_name = Product.objects.get(id=id)
    context = {'item':product_name}
    return render(request, 'detail.html', context = context)

