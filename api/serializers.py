from rest_framework import serializers
from api.models import Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'