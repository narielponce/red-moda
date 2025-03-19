from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import hello_world, PostViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)  # Endpoint /api/posts/
router.register(r'votes', VoteViewSet)  # Endpoint /api/votes/

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('', include(router.urls)),  # Incluye las rutas del router
]
