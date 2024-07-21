from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostCreateForm, PostUpdateForm, CommentForm


class HomeView(TemplateView):
    template_name = "main/home.html"

class TriviaListView(ListView):
    model = Post
    template_name = "main/list.html"

    def get_queryset(self):
        query = super().get_queryset()

        keyword = self.request.GET.get("keyword", None)
        category = self.request.GET.get("category", None)
        prefecture = self.kwargs["prefecture"]

        query = query.filter(prefecture=prefecture)
        
        if keyword:
            query = query.filter(title__icontains=keyword)
        
        if category == "未選択":
            pass
        elif category:
            query = query.filter(category=category)
        
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["prefecture"] = self.kwargs["prefecture"]
        context["keyword"] = self.request.GET.get("keyword", "")

        category = self.request.GET.get("category", "")

        if category == "地理":
            context["geography"] = True
        elif category == "歴史":
            context["history"] = True
        elif category == "人物":
            context["person"] = True
        elif category == "自然":
            context["nature"] = True
        elif category == "伝統":
            context["tradition"] = True
        elif category == "スポーツ":
            context["sport"] = True
        elif category == "食":
            context["food"] = True
        elif category == "文化":
            context["culture"] = True
        elif category == "芸能":
            context["entertainment"] = True
        elif category == "特産品":
            context["goods"] = True
        elif category == "方言":
            context["dialect"] = True
        elif category == "未選択":
            context["none"] = True

        return context
    
class TriviaDetailView(DetailView):
    template_name = "main/detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect("main:trivia-detail", pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))


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

class TriviaUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    template_name = "main/update.html"
    form_class = PostUpdateForm
    success_message = "投稿を更新しました"

    def get_success_url(self):
        return reverse_lazy('main:trivia-detail', kwargs={'pk': self.object.id})
    
    def get_success_message(self, cleaned_data):
        return f"{cleaned_data.get('title')}を更新しました"
    
    def test_func(self, **kwargs):
        id = self.kwargs["pk"]
        post = Post.objects.get(id=id)
        return (post.user == self.request.user)
    
class TriviaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "main/delete.html"

    def test_func(self):
        id = self.kwargs["pk"]
        post = Post.objects.get(id=id)
        return (post.user == self.request.user)
    
    def get_success_url(self):
        return reverse_lazy("main:mypage")

class TriviaLikeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return redirect("main:home")
    
    def post(self, request, *args, **kwargs):
        id = request.POST.get("id")
        related_post = Post.objects.get(id=id)
        if self.request.user in related_post.like.all():
            related_post.like.remove(self.request.user)
        else:
            related_post.like.add(self.request.user)
        return redirect("main:trivia-detail", related_post.pk)

class TriviaLikeListView(LoginRequiredMixin, ListView):
    template_name = "main/like-list.html"
    model = Post

    def get_queryset(self):
        query = super().get_queryset()

        query = query.filter(like=self.request.user)

        keyword = self.request.GET.get("keyword", None)
        category = self.request.GET.get("category", None)
        
        if keyword:
            query = query.filter(title__icontains=keyword)
        
        if category == "未選択":
            pass
        elif category:
            query = query.filter(category=category)
        
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["keyword"] = self.request.GET.get("keyword", "")

        category = self.request.GET.get("category", "")

        if category == "地理":
            context["geography"] = True
        elif category == "歴史":
            context["history"] = True
        elif category == "人物":
            context["person"] = True
        elif category == "自然":
            context["nature"] = True
        elif category == "伝統":
            context["tradition"] = True
        elif category == "スポーツ":
            context["sport"] = True
        elif category == "食":
            context["food"] = True
        elif category == "文化":
            context["culture"] = True
        elif category == "芸能":
            context["entertainment"] = True
        elif category == "特産品":
            context["goods"] = True
        elif category == "方言":
            context["dialect"] = True
        elif category == "未選択":
            context["none"] = True

        return context