from .models import Movie
from rest_framework import serializers

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"