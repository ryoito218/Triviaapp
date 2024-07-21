from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostCreateForm


class HomeView(TemplateView):
    template_name = "main/home.html"

class TriviaListView(ListView):
    template_name = "main/trivia_list.html"

    def get_queryset(self):
        prefecture = self.kwargs["prefecture"]
        trivias = Post.objects.filter(prefecture=prefecture)
        return trivias
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prefecture"] = self.kwargs["prefecture"]
        return context
    
class TriviaDetailView(DetailView):
    template_name = "main/trivia_detail.html"
    model = Post

class MyPageView(LoginRequiredMixin, ListView):
    template_name = "main/mypage.html"
    model = Post

    def get_queryset(self):
        user = self.request.user
        user_posts = Post.objects.filter(user=user)
        return user_posts
    
class TriviaCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "main/create.html"
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('main:mypage')