from django.urls import path
from .views import HomeView, TriviaListView

app_name = "main"

urlpatterns = [
    path('<str:prefecture>/', TriviaListView.as_view(), name="trivia-list"),
    path('', HomeView.as_view(), name="home"),
]