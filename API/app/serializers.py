from rest_framework import serializers
from .models import product

class productserializer(serializers.modelserializer):
    class Meta:
        model=product
        fields='__all__'