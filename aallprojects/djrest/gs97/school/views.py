from django.shortcuts import render

# Create your views here.
from .models import Student, Teacher
from django.db.models import Q
from datetime import date, time

def home(request):
    # qs1 = Student.objects.values("id", "name")
    # qs2 = Teacher.objects.values("id", "name")
    # student_data = qs2.union(qs1, all=True)
    # student_data = qs2.intersection(qs1)
    # student_data = qs2.difference(qs1)
    # student_data = qs1.difference(qs2)

    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll = 107)
    # student_data = Student.objects.filter(id=6, roll=106)
    # student_data = Student.objects.filter(Q(id=6)& Q(roll=106))
    # student_data = Student.objects.filter(Q(id=7)|Q(roll=106))
    # student_data = Student.objects.filter(id=6) |    Student.objects.filter(roll = 107)

    student = Student.objects.get(name="manju")
    student = Student.objects.first()
    student = Student.objects.order_by("city").first()
    student = Student.objects.last()
    student = Student.objects.latest('pass_date')
    student = Student.objects.earliest("pass_date")
    students = Student.objects.all()
    student = Student.objects.last()
    # Student.objects.create(name="chaman", roll=113, city="haveri", marks=89, pass_date="2022-12-12")
    # student, created = Student.objects.get_or_create(name="anisa", roll=114, city="bengaluru", marks=89, pass_date="2022-12-12")
    
    # student = Student.objects.filter(id=2).update(name="jiya", marks=80)
    # student = Student.objects.filter(city="mumbai").update(city="new mumbai")

    # student, created = Student.objects.update_or_create(id=3,roll=103, name="vishwa", defaults={'name': "kohali", 'roll': 115})
    # objs = [
    # Student(name="vishwa", roll=115, city="hubballi", marks=80, pass_date="2022-12-12"),
    # Student(name="noor", roll=116, city="bengaluru", marks=87, pass_date="2022-12-17"),
    # Student(name="nazeer", roll=117, city="mumbai", marks=88, pass_date="2022-12-15"),]

    # Student.objects.bulk_create(objs=objs)
    # all_student_data = Student.objects.filter(city="bengaluru")
    # print("-------------", all_student_data)

    # for data in all_student_data:
    #     data.city = "banglore"
    # print("-------------", all_student_data)

    # student_data = Student.objects.bulk_update(all_student_data, ['city'])
    # print("-------------", student_data)

    # student_data = Student.objects.in_bulk([1,2])
    # print(student_data)

    # students = Student.objects.filter(name__exact ="vishwa")
    # students = Student.objects.filter(name__contains ="r")
    # students = Student.objects.filter(id__in =[1,5,7])
    # students = Student.objects.filter(marks__in =[100])
    # students = Student.objects.filter(marks__range = (80, 90))
    # students = Student.objects.filter(marks__lte=95)
    # students = Student.objects.filter(name__startswith = "k") 
    # students = Student.objects.filter(name__endswith = "a")
    # students = Student.objects.filter(pass_date__range = ("2022-12-01", "2022-12-12"))
    # students = Student.objects.filter(pass_date__year =2022)
    # students = Student.objects.filter(pass_date__range = ("2022-12-01", "2022-12-12"))

    # students = Student.objects.all()[5:10]




    return render(request, "school/home.html", {'students': students})