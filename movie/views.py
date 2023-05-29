from .models import Movie
from .serializer import MovieSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    permission_classes = [IsAuthenticated]
    