from django.contrib.postgres import validators
from django.db import models


# Create your models here.


class Task(models.Model):
    task_name = models.CharField(unique=True, max_length=20)
    task_desc = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, upload_to='images')

    def __str__(self):
        return self.task_name
