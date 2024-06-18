from django.shortcuts import render
from .models import *
from django.http import HttpRequest

# Create your views here.

def main(request: HttpRequest):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'book/main.html', context)

def catalog(request: HttpRequest, category_id: int):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category = category)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'book/main.html', context)

def catalog_tag(request: HttpRequest, tag_id: int):
    tag = Tag.objects.get(id=tag_id)
    products = tag.products.all()
    
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'book/main.html', context)