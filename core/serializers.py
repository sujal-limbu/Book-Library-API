from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):

    def validate_price(self,value):
        if value < 0 :
            raise serializers.ValidationError("Price must be greater than zero")
        return value
    
    def validate_published_year(self,value):
        if value > 2026:
            raise serializers.ValidationError("Book Published Year Should not be greater than present year")
        return value
    
    class Meta:
        model = Book
        fields = '__all__'