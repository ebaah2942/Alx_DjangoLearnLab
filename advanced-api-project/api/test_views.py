from .models import Book
from .models import Author
from .serializers import BookSerializer
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class BookAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for authentication
        cls.user = User.objects.create_user(username='Enoch', password='Heal.1234')
        # Create a book a post
        author = Author.objects.get(id=1)
        cls.book1 = Book.objects.create(title='In the chest of a woman', author=author, publication_year=2020)
        cls.book2 = Book.objects.create(title='Things we do for love', author='Ohene Pozo', publication_year=2003)

    def setUp(self):
        # Log in the user before each test
        self.client.login(username='Enoch', password='Heal.1234')

    
    # CRUD operations
    # Creating new book   
    def test_create_book(self):
       data = {
           'title': 'The Angel of Death',
           'author': 'Peggy Lamptey',
           'publication_year': 2020
       }
       response = self.client.post('/api/books/', data, format='json')
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #    Increase the number of books by 2
       self.assertEqual(Book.objects.count(), 2)
       # Get the last book
       self.assertEqual(Book.objects.last().title, 'The Angel of Death')


    # Retrieving all books
    def test_list_books(self):
       response = self.client.get('/api/books/')
         #   Increase the number of books by 2
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(len(response.data), 2)


    def test_retrieve_book(self):
       response = self.client.get(f'/api/books/{self.book1.id}/')
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(response.data["title"], 'In the chest of a woman')


    def test_update_book(self):
       data = {
           'title': 'Had I know',
           'author': 'Stephen Newman',
           'publication_year': 1996
       }
       response = self.client.put(f'/api/books/{self.book1.id}/', data, format='json')
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(Book.objects.count(), 2)
       self.assertEqual(Book.objects.last().title, 'Had I know')


    def test_delete_book(self):
       response = self.client.delete(f'/api/books/{self.book1.id}/')
       self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #    Decrease the number of books by 1
       self.assertEqual(Book.objects.count(), 1)



    def test_ordering_books(self):
        # Test ordering books by price.
        response = self.client.get("/api/books/?ordering=price")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")  # Cheapest book first

    def test_filtering_books(self):
        # Test filtering books by author.
        response = self.client.get("/api/books/?author=Author A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author A")

    def test_searching_books(self):
        # Test searching books by title.
        response = self.client.get("/api/books/?search=Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)



    # Permissions and Authentication 

    def test_unauthenticated_create(self):
        # Test unauthenticated user cannot create a book.
        self.client.logout()  # Ensure the user is logged out
        data = {"title": "Unauthorized Book", "author": "Author D", "price": 25.00}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Or 401, depending on settings

    def test_authenticated_create(self):
        # Test authenticated user can create a book.
        data = {"title": "Authenticated Book", "author": "Author E", "price": 30.00}
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.last().title, "Authenticated Book")

    # Utility Testing

    def test_invalid_data_create(self):
        # Test creating a book with invalid data.
        data = {"title": "", "author": "", "price": -5.00}  # Invalid price
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Validation should fail
