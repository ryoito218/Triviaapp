from django.urls import path
from .views import HomeView, TriviaListView, TriviaDetailView, MyPageView, TriviaCreateView, TriviaUpdateView, TriviaDeleteView, TriviaLikeView

app_name = "main"

urlpatterns = [
    path("create/", TriviaCreateView.as_view(), name="trivia-create"),
    path("update/<int:pk>/", TriviaUpdateView.as_view(), name="trivia-update"),
    path("delete/<int:pk>", TriviaDeleteView.as_view(), name="trivia-delete"),
    path("mypage/", MyPageView.as_view(), name="mypage"),
    path("detail/<int:pk>/", TriviaDetailView.as_view(), name="trivia-detail"),
    path("list/<str:prefecture>/", TriviaListView.as_view(), name="trivia-list"),
    path("like/", TriviaLikeView.as_view(), name="trivia-like"),
    path("", HomeView.as_view(), name="home"),
]