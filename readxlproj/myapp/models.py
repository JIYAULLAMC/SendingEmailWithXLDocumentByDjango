from django.db import models

# Create your models here.


class Student(models.Model):
    stu_code = models.IntegerField()
    stu_name = models.CharField(max_length=20)
    stu_email = models.EmailField(max_length=30)
    stu_money = models.IntegerField()