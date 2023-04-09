from rest_framework import viewsets 
from books.api import serializer 
from books import models 

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.booksSerializer
    queryset = models.books.objects.all()