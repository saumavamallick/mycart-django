from django.shortcuts import render
from .models import Product
# Create your views here.
def store(request, category_slug=None):
    if category_slug is not None:
        products = Product.objects.all().filter(category__slug=category_slug).order_by('-modified_date')
    else: products = Product.objects.all().filter(is_available=True).order_by('-modified_date')
    return render(request, 'store/store.html', {'products':products})

def product_detail(request,category_slug,product_slug):
    product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    return render(request, 'store/product-detail.html', {'product':product})

#this function is taken care in function store alresdy
def product_category(request, category_slug):  #not in use
    #category is a foreign key inside product, so category__slug represents category.slug
    products = Product.objects.all().filter(category__slug=category_slug)
    return render(request, 'store/store.html', {'products':products})
