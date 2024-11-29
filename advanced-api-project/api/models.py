from django.db import models

# Create your models here.
# Author model with name field
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name





# Book model with title, author and publication year that reference the Author model
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,max_length=100)
    publication_year = models.IntegerField()


    def __str__(self):
        return f"{self.title} by {self.author} published in {self.publication_year}"