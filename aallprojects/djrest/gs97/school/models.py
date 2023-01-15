from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=20)
    marks = models.IntegerField()
    pass_date = models.DateField()


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=20)
    salary = models.IntegerField()
    join_date = models.DateField()


# Create your models here.
