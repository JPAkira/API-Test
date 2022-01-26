from django.db import models

class Employee(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    email = models.EmailField(max_length=255)
    department = models.CharField(verbose_name="Department", max_length=50)

