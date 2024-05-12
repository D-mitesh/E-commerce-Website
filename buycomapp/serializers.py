from .models import *
from rest_framework import serializers

class productserializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'