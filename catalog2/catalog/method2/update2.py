from django.db import transaction

from catalog.model.Book import Book
from django.shortcuts import get_object_or_404
from catalog.serializers2.serializers import BookSerializer

def update_book_info2(book_id, data):
    # Retrieve the book object from the 'default' database
    book = get_object_or_404(Book.objects.using('default'), pk=book_id)

    # Serialize the data
    serializer = BookSerializer(book, data=data, partial=True)

    # If valid, update both databases
    if serializer.is_valid():
        with transaction.atomic(using='default'):
            serializer.save(using='default')  # Save to 'default' database

        # Update the replica
        # Fetch a fresh instance from the replica database, to update it independently
        book_replica = Book.objects.using('replica').get(pk=book_id)
        serializer_replica = BookSerializer(book_replica, data=data, partial=True)

        if serializer_replica.is_valid():
            with transaction.atomic(using='replica'):
                serializer_replica.save(using='replica')  # Save to 'replica' database
            return serializer.data

    return serializer.errors

