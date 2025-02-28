from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    pic=models.ImageField(upload_to='pic/')
    doc=models.FileField(upload_to='file/')

    def __str__(self):
        return self.name