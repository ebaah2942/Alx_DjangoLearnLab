from django.db import models

# Create your models here.
# Author class which takes only name field
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book class to represent a book with a title, author, and publication year fields
# Where the author is a foreign key to the Author class
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} published in {self.publication_year}"