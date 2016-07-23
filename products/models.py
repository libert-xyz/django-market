from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='managers')
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0.00) #100.00
    slug = models.SlugField(unique=True)
    description = models.TextField(default='Product Description')

    def __unicode__(self):
        return self.title

def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def product_pre_save(sender,instance,*args,**kargs):

    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(product_pre_save, sender=Product)
