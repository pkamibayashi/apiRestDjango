from rest_framework import serializers
from books import models 

class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.books
        fields = '__all__'