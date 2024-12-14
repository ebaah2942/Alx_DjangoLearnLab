from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter



# register the viewset to the router
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


# add the router to the urlpatterns
urlpatterns = [
    path('', include(router.urls))
]


