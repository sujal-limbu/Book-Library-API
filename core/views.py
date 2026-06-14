from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['get', 'post'])
    def favourite(self, request, pk=None):
        book = self.get_object()
        if request.method == 'POST':
         book.is_favourite = not book.is_favourite
         book.save()
        return Response({
        "is_favourite": book.is_favourite,
        "message": "Added to favorites" if book.is_favourite else "Removed from favorites"
    })

