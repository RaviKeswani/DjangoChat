from django.db import models

# Create your models here.

class StudentForm(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=100,choices=(('Female','Female'),('Male','Male')))
    email=models.EmailField(max_length=100)
    city=models.CharField(max_length=100)
    picture=models.ImageField(upload_to='pictures')


    class Meta:
        db_table='student'