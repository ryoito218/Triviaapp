from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post


class HomeView(TemplateView):
    template_name = "main/home.html"

class TriviaListView(ListView):
    template_name = "main/trivia_list.html"
    model = Post

    def get_queryset(self):
        prefecture = self.kwargs['prefecture']
        trivias = Post.objects.filter(prefecture=prefecture)
        return trivias
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prefecture'] = self.kwargs['prefecture']
        return context