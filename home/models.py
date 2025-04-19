# home/models.py

from django.db import models
import uuid

class ProductLine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover_photo = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name


from django.utils import timezone

class Enquiry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    enquiry_for = models.ForeignKey('ProductLine', on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)  # Set default value here

    def __str__(self):
        return f'{self.name} - {self.enquiry_for.name}'

