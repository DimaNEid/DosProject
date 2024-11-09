from catalog.model.Book import Book
from django.shortcuts import get_object_or_404
from catalog.serializers2.serializers import BookSerializer


def get_book_info2(book_id):
    book = get_object_or_404(Book, pk=book_id)
    return BookSerializer(book).data

