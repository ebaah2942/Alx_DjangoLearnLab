from django.db import models

# Create your models here.

# Book model class to create table for each fields
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title