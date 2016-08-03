from django.db import models
from products.models import Product
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


class TagManager(models.Manager):
    def all(self,*args,**kwargs):
        return super(TagManager,self).all(*args,**kwargs).filter(active=True)


class Tag(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)
    products = models.ManyToManyField(Product, blank=True)
    active = models.BooleanField(default=True)

    objects = TagManager()

    def __unicode__(self):
        return str(self.title)

    def get_absolute_url(self):
        view_name = 'tags:detail_slug'
        return reverse(view_name, kwargs={'slug':self.slug})


def tag_pre_save(sender,instance,*args,**kwargs):

    if not instance.slug:
        instance.title = instance.title.lower()
        if not instance.slug:
            instance.slug = slugify(instance.title)

pre_save.connect(tag_pre_save, sender=Tag)
