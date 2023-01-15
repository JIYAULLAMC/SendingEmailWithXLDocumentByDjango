from django.contrib import admin

# Register your models here.

from .models import Student, Teacher, Contractor


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "fees"]

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "date", "salary"]


@admin.register(Contractor)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "date", "payment"]