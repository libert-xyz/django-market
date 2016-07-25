"""digitalmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include('products.urls',namespace='products')),

    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product_detail_slug'),
    # url(r'^products/add$', ProductCreateView.as_view(), name='product_create'),
    # url(r'^products/(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='product_update'),
    # url(r'^products/(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name='product_update'),

]
