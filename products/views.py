from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product


def detail(request,slug=None):
    print request

    product = get_object_or_404(Product,slug=slug)
    context = {'product':product}
    template = 'detail.html'
    return render(request,template,context)
