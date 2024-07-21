from django.urls import path
from .views import EditProfileView

app_name = "accounts"

urlpatterns = [
    path("update/<int:pk>/", EditProfileView.as_view(), name="update"),
]