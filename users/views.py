from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import CustomUser

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    template_name = "signup.html"
    success_url = reverse_lazy("login")
