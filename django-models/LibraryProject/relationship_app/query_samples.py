from relationship_app.models import *

def query():
    
    author = Author.objects.get(name="J.K. Rowling")


def list_books():
    books = Book.objects.all()
    return books


def retrieve_librarian():
    librarian = Librarian.objects.get(name="Enoch Baah")
    return librarian
    
