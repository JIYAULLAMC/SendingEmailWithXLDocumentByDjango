from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView, ListView
from .models import Student, Teacher, Contractor

class Home(ListView):
    template_name = "school/home.html"
    queryset = Student.objects.all()

print(Home.queryset)
