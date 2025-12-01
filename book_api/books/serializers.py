from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializers):
    class Meta:
        model = Book 
        field = '__all__'