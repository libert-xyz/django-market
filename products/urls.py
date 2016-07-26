from django.conf.urls import include, url
from django.contrib import admin
from .views import ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDownloadView

urlpatterns = [

    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^add/$', ProductCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='detail_slug'),
    url(r'^(?P<pk>\d+)/download/$', ProductDownloadView.as_view(), name='download'),
    url(r'^(?P<slug>[\w-]+)/download/$', ProductDownloadView.as_view(), name='download_slug'),
    url(r'^(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name='update_slug'),

    # url(r'^create/$', 'products.views.create_product', name='create_product'),
    # url(r'^detail/(?P<object_id>\d+)/$', 'products.views.detail', name='detail'),
    # url(r'^detail/(?P<slug>[\w-]+)/$', 'products.views.detail_slug', name='detail_slug'),
    # url(r'^detail/(?P<object_id>\d+)/edit/$', 'products.views.update', name='update'),

]
