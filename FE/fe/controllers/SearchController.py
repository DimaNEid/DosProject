from rest_framework import viewsets
from rest_framework.response import Response
from fe.method.search import search_books

class SearchController(viewsets.ViewSet):
    def list(self, request):
        """Handles the search request and delegates to the method file."""
        topic = request.query_params.get('topic', None)
        if not topic:
            return Response({"error": "Topic parameter is required"}, status=400)

        search_data, status = search_books(topic)
        return Response(search_data, status=status)

# from rest_framework import viewsets
# from rest_framework.response import Response
# from fe.method.search import search_books
#
# class SearchController(viewsets.ViewSet):
#     def list(self, request):
#         """Handles the search request and delegates to the method file."""
#         topic = request.query_params.get('topic', None)
#         if not topic:
#             return Response({"error": "Topic parameter is required"}, status=400)
#
#         search_data, status = search_books(topic)
#         return Response(search_data, status=status)

import requests
