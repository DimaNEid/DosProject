from rest_framework import viewsets
from rest_framework.response import Response
from catalog.method2.search2 import search_books2

class searchController2(viewsets.ViewSet):
    def list(self, request):
        print("Search endpoint reached")  # Debugging line
        topic = request.query_params.get('topic', None)
        if not topic:
            return Response(data={"error": "Topic parameter is required"}, status=400)
        result = search_books2(topic)
        return Response(result)
