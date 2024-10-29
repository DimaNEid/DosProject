
from catalog.model.Book import Book
from catalog.serializers.serializers import BookSerializer


def search_books(topic):
    # topic = topic.strip()
    books = Book.objects.filter(topic__icontains=topic)
    print(books)
    return BookSerializer(books, many=True).data
