# gallery/views.py
from django.shortcuts import render
from django.http import JsonResponse
from home.models import ProductLine
from .models import Product

def gallery(request):
    product_lines = ProductLine.objects.all()
    return render(request, 'gallery/gallery.html', {'product_lines': product_lines})

def get_products(request, product_line_id):
    products = Product.objects.filter(product_line_id=product_line_id)
    product_data = [
        {
            'name': product.name,
            'description': product.description,
            'details': product.details,
            'image': product.image.url
        } for product in products
    ]
    return JsonResponse(product_data, safe=False)
