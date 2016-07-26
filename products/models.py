from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


def download_media_location(instance,filename):
    return "%s/%s" %(instance.id,filename)


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='managers')

    media = models.FileField(blank=True,null=True, upload_to=download_media_location,
            storage=FileSystemStorage(location=settings.PROTECTED_ROOT))

    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0.00) #100.00
    slug = models.SlugField(unique=True)
    description = models.TextField(default='Product Description')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        view_name = 'products:detail_slug'
        #return '/products/%s' %(self.slug)
        return reverse(view_name, kwargs={'slug':self.slug})

    def get_download(self):

        view_name = 'products:download_slug'
        url = reverse(view_name, kwargs={'slug':self.slug})

        return url



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



class MyProducts(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    products = models.ManyToManyField(Product,blank=True)


    def __uniode__(self):
        return '%s' %(self.products.count())

    class Meta:
        verbose_name = 'My Products'
        verbose_name_plural = 'My Products'
