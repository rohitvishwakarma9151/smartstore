from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Furniture', 'Furniture'),
        ('Electronics', 'Electronics'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
