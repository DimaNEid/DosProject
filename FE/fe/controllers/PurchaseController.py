from rest_framework import viewsets
from rest_framework.response import Response
from fe.method.purchase import make_purchase

class PurchaseController(viewsets.ViewSet):

    def update(self, request, pk=None):

        if not pk:
            return Response({"error": "Book ID is required for updating"}, status=400)

        # Forward the request to update the purchase in the Order service
        update_data, status = make_purchase(pk, request.data)
        return Response(update_data, status=status)

