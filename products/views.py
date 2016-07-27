import os
from mimetypes import guess_type
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.servers.basehttp import FileWrapper
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import Http404, HttpResponse
from digitalmarket.mixins import StaffRequiredMixin, LoginRequiredMixin
from .mixins import ProductManagerMixin
from .models import Product
from .forms import ProductModelForm



class ProductListView(ListView):
    model = Product
    #template_name = 'list_products.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     print context
    #     #context["product"] = Product.objects.all()
    #     context['product'] = self.get_queryset()
    #     return context

    def get_queryset(self, *args,**kwargs):
        qs = super(ProductListView, self).get_queryset(**kwargs)
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(title__icontains=query)|
                Q(description__icontains=query)
                ).order_by('-pk')
            print qs
        return qs

def list(request):
    product = Product.objects.all()
    context= {'product':product}
    template = 'list_products.html'
    return render(request,template,context)

class ProductDetailView(DetailView):
    model = Product

class ProductDownloadView(DetailView):
    model = Product

    def get(self,request,*args,**kwargs):
        obj = self.get_object()

        try:
            my_products = request.user.myproducts
        except:
            my_products = None

        if my_products and obj in my_products.products.all():
            filepath = os.path.join(settings.PROTECTED_ROOT, obj.media.path)
            #Wrapper big files
            wrapper = FileWrapper(file(filepath))
            mimetype = 'application/force-download'
            if guess_type:
                mimetype = guess_type
            response = HttpResponse(wrapper, content_type=mimetype)

            if request.GET.get('preview'):
                #Create Headers so the browser can understand
                response['Content-Disposition'] = 'attachement; filename=%s' %(obj.media.name)
            response['X-Sendfile'] = str(obj.media.name)
            #return HttpResponse('%s' %(obj))
            return response
        else:
            raise Http404


def detail(request,object_id=None):

    product = get_object_or_404(Product,id=object_id)
    context = {'product':product}
    template = 'detail.html'
    return render(request,template,context)

def detail_slug(request,slug=None):

    product = get_object_or_404(Product,slug=slug)
    context = {'product':product}
    template = 'detail.html'
    return render(request,template,context)


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    template_name = 'create_product.html'
    form_class = ProductModelForm
    #success_url = '/products/add'

    def form_valid(self,form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(ProductCreateView, self).form_valid(form)
        form.instance.managers.add(user)
        return valid_data

    # def get_success_url(self):
    #     return '/users/%s' %(self.request.user)



def create_product(request):

    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    # if form.is_valid():
    #     data = form.cleaned_data
    #     title = data.get('title')
    #     description = data.get('description')
    #     price = data.get('price')
    #     new_obj = Product.objects.create(title=title,description=description,price=price)
    #     new_obj.save()

    context = {'form':form}
    template = 'create_product.html'
    return render(request,template,context)

class ProductUpdateView(ProductManagerMixin, UpdateView, LoginRequiredMixin):
    model = Product
    template_name = 'update.html'
    form_class = ProductModelForm
    #success_url = '/products/'

    # def get_object(self,*args,**kargs):
    #     user = self.request.user
    #     obj = super(ProductUpdateView, self).get_object(*args,**kargs)
    #     if obj.user == user or user in obj.managers.all():
    #         return obj
    #     else:
    #         raise Http404


def update(request,object_id=None):

    product = get_object_or_404(Product,id=object_id)
    form = ProductModelForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
    context = {'product':product, 'form':form,}
    template = 'update.html'
    return render(request,template,context)
