# gallery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('products/<uuid:product_line_id>/', views.get_products, name='get_products'),
]
