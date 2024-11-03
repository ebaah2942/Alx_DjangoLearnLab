Create:
b1 = Book(title="1984, author="George Orwell", publication_year=1949)
b1.save


Retrieve:
b2 = Book.objects.get(title="1984")
print(b2)
<!-- Book object (1) -->

Update:
b1.title = "Nineteen Eighty-Four"
b1.save()


Delete:
b1.delete()
<!-- (1, {'bookshelf.Book': 1}) -->

print(b1)
<!-- Book object (none) -->