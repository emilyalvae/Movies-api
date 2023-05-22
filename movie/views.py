from .models import Movie
from .serializer import MovieSerializers
from rest_framework import viewsets

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    

