from django.urls import path, include
from .views import PostViewSet, CommentViewSet, user_feed, like_post, unlike_post 
from rest_framework.routers import DefaultRouter



# register the viewset to the router
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


# add the router to the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('feed/', user_feed, name='user_feed'),
    path('<int:pk>/like/', like_post, name='like_post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike_post'),

]


