from django.db import models

class student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

