
from rest_framework import viewsets
from rest_framework.response import Response
from catalog.method.info import get_book_info

class infoController(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        result = get_book_info(pk)
        return Response(result)
