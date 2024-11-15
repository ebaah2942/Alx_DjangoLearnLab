I created instance to the Book table with the folowing command:
b1 = Book.objects.create(title="1984, author="George Orwell", publication_year=1949)
b1.save()