from django.db import models
class courses(models.Model):
    coursename=models.CharField(max_length=40)
    courseid=models.IntegerField(default=6,primary_key=True)
    coursefee=models.IntegerField(default=6)
    courseduration=models.IntegerField(default=4)

class student(models.Model):
    name=models.CharField(max_length=40)
    contect=models.IntegerField(default=10,primary_key=True)
    gender=models.CharField(max_length=6)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=15)
    email=models.EmailField()

class StudentAddDetails(models.Model):
    name = models.CharField(max_length=40)
    contect = models.IntegerField(default=10, primary_key=True)
    qualification=models.CharField(max_length=40)
    course=models.CharField(max_length=40)
    timmeing=models.TimeField()


class faculty(models.Model):
    id=models.AutoField(default=5,primary_key=True)
    name=models.CharField(max_length=40)
    contact=models.IntegerField(default=10)
    gender=models.CharField(max_length=5)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    course=models.CharField(max_length=10)

