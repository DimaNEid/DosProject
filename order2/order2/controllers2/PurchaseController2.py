
from rest_framework import viewsets
from rest_framework.response import Response
from order2.method2.purchase2 import purchase_book2


class PurchaseController2(viewsets.ViewSet):
    def update(self, request, pk=None):
        result, status = purchase_book2(pk)
        return Response(result, status=status)


