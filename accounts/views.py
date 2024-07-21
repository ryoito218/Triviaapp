from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import EditProfileForm

class OwnProfileOnly(UserPassesTestMixin):
    def test_func(self):
        profile_obj = self.get_object()
        try:
            return profile_obj == self.request.user.profile
        except:
            return False

class EditProfileView(LoginRequiredMixin, OwnProfileOnly, SuccessMessageMixin, UpdateView):
    template_name = "accounts/update.html"
    model = Profile
    form_class = EditProfileForm
    success_message = "アカウントを更新しました"

    def get_success_url(self):
        return reverse_lazy("main:mypage")