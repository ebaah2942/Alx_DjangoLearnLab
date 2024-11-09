from relationship_app.models import *

def query(author_name):
    
    author = Author.objects.get(name=author_name)
    author_books = Book.objects.filter(author=author)
    return author_books


# def list_books(libray_name):

#     library = Library.objects.get(name=libray_name)
#     books = library.book.all()
#     return books
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()  
    return books_in_library

def retrieve_librarian(librarian_name):
    library = Library.objects.get(name=librarian_name)

    librarian = Librarian.objects.get(library=library)
    return librarian