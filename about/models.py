# about/models.py

from django.db import models


class SpecialMachinery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='machinery_images/')

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='certification_images/')
    provider = models.CharField(max_length=255)

    def __str__(self):
        return self.name
