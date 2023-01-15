from django.contrib import admin
from myapp.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', "stu_code", 'stu_name', 'stu_email','stu_money']


admin.site.register(Student, StudentAdmin)