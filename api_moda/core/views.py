from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hola, API funcionando"})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]  # Permite lectura sin autenticación
    permission_classes = [AllowAny]  # Desactiva la autenticación
    
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    #  permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AllowAny]  # Desactiva la autenticación