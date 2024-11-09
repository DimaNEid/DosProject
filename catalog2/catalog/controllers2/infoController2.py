from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from catalog.method2.info2 import get_book_info2

class infoController2(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        result = get_book_info2(pk)
        return Response(result)
