
from catalog.model.Book import Book
from django.shortcuts import get_object_or_404
from catalog.serializers.serializers import BookSerializer


def update_book_info(book_id, data):
    book = get_object_or_404(Book, pk=book_id)
    serializer = BookSerializer(book, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors