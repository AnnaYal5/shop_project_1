from django.shortcuts import render
from .models import Product

def index_view(request):

    new_arrivals = Product.objects.filter(category='New Arrivals').order_by('-id')
    best_sellers = Product.objects.filter(category='Best Sellers')

    context = {
        'new_arrivals': new_arrivals,
        'best_sellers': best_sellers,
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')