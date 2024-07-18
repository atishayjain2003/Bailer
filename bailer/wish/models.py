from django.db import models

class Member(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    DOB=models.DateField()
