from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0.00) #100.00
    slug = models.SlugField(unique=True)
    description = models.TextField(default='Product Description')

    def __unicode__(self):
        return self.title

def product_pre_save(sender,instance,*args,**kargs):

    instance.slug = slugify(instance.title)



pre_save.connect(product_pre_save, sender=Product)
