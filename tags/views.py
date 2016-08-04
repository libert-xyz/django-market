from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Tag
from analytics.models import TagView

class TagDetailView(DetailView):
    model = Tag

    def get_context_data(self, *args, **kwargs):
        context = super(TagDetailView, self).get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated():
            tag = self.get_object()
            new_view = TagView.objects.add_count(self.request.user, tag)

            # analytic_obj, created = TagView.objects.get_or_create(
            # user = self.request.user,
            # tag = self.get_object())
            # analytic_obj.count += 1
            # analytic_obj.save()
        return context



class TagListView(ListView):
    model = Tag

    def get_queryset(self):
        return Tag.objects.all()
