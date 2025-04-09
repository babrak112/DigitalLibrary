from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm


class SubmittableLoginView(LoginView):
    template_name = "form.html"


def logout_view(request):
    logout(request)
    return redirect("home")


class SingUpView(CreateView):
    template_name = "form.html"
    form_class = CustomUserCreationForm #UserCreationForm
    success_url = reverse_lazy("home")

