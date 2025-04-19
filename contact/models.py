# contact/models.py
from django.db import models
from gallery.models import ProductLine

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    hear_about_us = models.CharField(max_length=255, blank=True)
    product_interest = models.ManyToManyField(ProductLine)
    message = models.TextField()
    captcha = models.CharField(max_length=10)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
