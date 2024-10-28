# from django.db.models.expressions import result
# from rest_framework import viewsets, status
# from rest_framework.response import Response
#
# from order.method.order import handle_purchase
#
#
# class orderController(viewsets.ViewSet):
#     def update(self, request, pk=None):
#         quantity = request.data['quantity',None]
#
#         if quantity is None:
#             return Response({'error':'Quantity parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
#
#         result, status_code = handle_purchase(pk, quantity)
#         return Response(result, status=status_code)


# class purchaseController(viewsets.ViewSet):
#     def update(self, request, pk=None):
#         """Handle the purchase process using primary key (pk)."""
#         # Using .get to safely access 'count' from request data
#         count = request.data.get('count', None)
#
#         if not count:
#             return Response({"error": "Count parameter is required"}, status=400)
#
#         # Call the purchase handling method
#         result, status_code = handle_purchase(pk, int(count))
#         return Response(result, status=status_code)


from rest_framework import viewsets
from rest_framework.response import Response

from order.method.purchase import purchase_book


class PurchaseController(viewsets.ViewSet):


    def update(self, request, pk=None):

        result, status = purchase_book(pk)
        return Response(result, status=status)