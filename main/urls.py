from django.urls import path
from .views import HomeView, TriviaListView, TriviaDetailView, MyPageView, TriviaCreateView, TriviaUpdateView

app_name = "main"

urlpatterns = [
    path("create/", TriviaCreateView.as_view(), name="trivia-create"),
    path("update/<int:pk>/", TriviaUpdateView.as_view(), name="trivia-update"),
    path("mypage/", MyPageView.as_view(), name="mypage"),
    path("detail/<int:pk>/", TriviaDetailView.as_view(), name="trivia-detail"),
    path("list/<str:prefecture>/", TriviaListView.as_view(), name="trivia-list"),
    path("", HomeView.as_view(), name="home"),
]