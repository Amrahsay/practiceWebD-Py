from django.http import HttpResponse
from .models import Product
from django.shortcuts import render


# /products->index
# Uniform Resource Locator (Address)
def index(request):
    products = Product.objects.all()
    # return HttpResponse('Hello World')
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')


