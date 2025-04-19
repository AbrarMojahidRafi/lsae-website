# gallery/models.py
from django.db import models
import uuid
from home.models import ProductLine

class Product(models.Model):
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE, related_name='products', default=1)  # Replace 1 with the actual default ProductLine ID
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available")
    details = models.TextField(default="No details available")
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
