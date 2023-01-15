from django.shortcuts import render
from django.template.backends.django import DjangoTemplates
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from myapp.forms import MyadminForm

from django.views.generic import TemplateView, FormView
from django.contrib.admin.sites import AdminSite


def home(request):
    form = AdminSite()
    # form = AuthenticationForm()
    print(1222222222222222222)
    print(form)
    return render(request, "myapp/home.html", {'form':form})
    