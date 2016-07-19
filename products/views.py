from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import Http404
from .models import Product
from .forms import ProductAddForm, ProductModelForm



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
        #qs = qs.filter(title__icontains='Fender')
        print qs
        return qs

def list(request):
    product = Product.objects.all()
    context= {'product':product}
    template = 'list_products.html'
    return render(request,template,context)

class ProductDetailView(DetailView):
    model = Product


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


class ProductCreateView(CreateView):
    model = Product
    template_name = 'create_product.html'
    form_class = ProductModelForm
    success_url = '/products/add'



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

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update.html'
    form_class = ProductModelForm
    success_url = '/products/'


def update(request,object_id=None):

    product = get_object_or_404(Product,id=object_id)
    form = ProductModelForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
    context = {'product':product, 'form':form,}
    template = 'update.html'
    return render(request,template,context)
