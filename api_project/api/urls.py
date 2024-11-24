from django.urls import path, include
from .views import BookList
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


# A default router is created to generate URL patterns for the BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Maps to the BookList view and the BookViewSet
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('token/', obtain_auth_token, name='obtain_token'),
]