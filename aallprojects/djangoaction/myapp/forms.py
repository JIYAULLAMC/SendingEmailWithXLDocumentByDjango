from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, AdminPasswordChangeForm, UserCreationForm,PasswordChangeForm, SetPasswordForm, PasswordResetForm

from django.contrib.admin.sites import AdminSite


class MyadminForm(AdminSite):
    pass
