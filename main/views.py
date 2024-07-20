from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

class HomeView(TemplateView):
    template_name = "main/home.html"

class TriviaListView(ListView):
    template_name = "trivia_list.html"

    def get_queryset(self):
        prefecture = self.kwargs['prefecture']
        trivias = Post.objects.filter(prefecture=prefecture)
        return trivias