from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Tag

class TagDetailView(DetailView):
    model = Tag


class TagListView(ListView):
    model = Tag

    # def get_queryset(self):
    #     return Tag.objects.filter(active=True)
