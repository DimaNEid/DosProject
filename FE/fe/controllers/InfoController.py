from rest_framework import viewsets
from rest_framework.response import Response
from fe.method.info import get_info

class InfoController(viewsets.ViewSet):
    def retrieve(self, request, pk=None):

        info_data, status = get_info(pk)
        return Response(info_data, status=status)


