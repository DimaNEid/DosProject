
from rest_framework import viewsets
from rest_framework.response import Response
from catalog.method.update import update_book_info
import requests
class updateController(viewsets.ViewSet):
        def update(self, request, pk=None):
            result = update_book_info(pk, request.data)
            if isinstance(result, dict) and 'errors' in result:
                return Response(result, status=400)
            frontend_url = f"http://127.0.0.1:8001/FrontEnd_service/invalidateCache/{pk}"
            try:
                requests.get(frontend_url)
            except requests.RequestException as e:
                print(f"Failed to invalidate cache: {e}")

            return Response(result)
