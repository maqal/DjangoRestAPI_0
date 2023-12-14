from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    regNo = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)