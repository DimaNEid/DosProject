from rest_framework import serializers
from catalog.model.Book import Book
from catalog.model.Catalog import Catalog

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


