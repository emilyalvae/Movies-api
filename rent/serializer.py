from .models import Rent
from rest_framework import serializers

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = "__all__"