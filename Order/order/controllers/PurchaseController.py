
from rest_framework import viewsets
from rest_framework.response import Response
from order.method.purchase import purchase_book

class PurchaseController(viewsets.ViewSet):

    def update(self, request, pk=None):

        result, status = purchase_book(pk)
        return Response(result, status=status)