
from rest_framework import viewsets
from rest_framework.response import Response
from catalog.method.update import update_book_info

class updateController(viewsets.ViewSet):
    def update(self, request, pk=None):
        result = update_book_info(pk, request.data)
        if isinstance(result, dict) and 'errors' in result:
            return Response(result, status=400)
        return Response(result)
