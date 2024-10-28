from rest_framework import viewsets
from rest_framework.response import Response
from fe.method.info import get_info

class InfoController(viewsets.ViewSet):
    def retrieve(self, request, pk=None):

        info_data, status = get_info(pk)
        return Response(info_data, status=status)



# from rest_framework import viewsets
# from rest_framework.response import Response
# from fe.method.info import get_info
#
# class InfoController(viewsets.ViewSet):
#     def list(self, request):
#         """Handles the request to get info by delegating to the method file."""
#         info_data, status = get_info()
#         return Response(info_data, status=status)

import requests
