from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
