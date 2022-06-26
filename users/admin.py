from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)

