from django.urls import path
from .views import HomeView, TriviaListView, TriviaDetailView

app_name = "main"

urlpatterns = [
    path('detail/<int:pk>/', TriviaDetailView.as_view(), name="trivia-detail"),
    path('<str:prefecture>/', TriviaListView.as_view(), name="trivia-list"),
    path('', HomeView.as_view(), name="home"),
]