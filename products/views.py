from django.shortcuts import render
from products.models import ProductCategory,Product

# Create your views here.
def index(request):
    contex = {'title': 'Store',
              }
    return render(request, 'products/index.html', contex)


def products(request):
    contex = {'title': 'Store - Каталог',
              'products': Product.objects.all(),
              'categories': ProductCategory.objects.all()
              }
    return render(request, 'products/products.html', contex)
