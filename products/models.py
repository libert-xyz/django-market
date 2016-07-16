from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0.00) #100.00
    description = models.TextField(default='Product Description')

    def __str__(self):
        self.title
