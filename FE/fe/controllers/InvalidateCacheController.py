from rest_framework import viewsets
from rest_framework.response import Response
from fe.method.invalidate import invalidate

class InvalidateCacheController(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        if not pk:
            return Response({"error": "PK is required for updating"}, status=400)
        # Forward the request to update the purchase in the Order service
        response = invalidate(pk)
        return Response(response, status=200)









