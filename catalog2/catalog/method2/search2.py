
from catalog.model.Book import Book
from catalog.serializers2.serializers import BookSerializer


def search_books2(topic):
    topic = topic.strip()  # Clean up the topic parameter
    books = Book.objects.filter(topic__icontains=topic)
    print(books)  # This will show in the Django console
    return BookSerializer(books, many=True).data


