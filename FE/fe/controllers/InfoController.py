from rest_framework import viewsets
from rest_framework.response import Response
from fe.method.info import get_info
from django.core.cache import caches
import itertools

class InfoController(viewsets.ViewSet):
    # Define a list of backend replicas
    BACKEND_REPLICAS = [1, 2]

    # Create a round-robin iterator for replicas
    replica_cycle = itertools.cycle(BACKEND_REPLICAS)
    def retrieve(self, request, pk=None):
        # Try to get data from the cache
        cache_key = "info_" + pk
        info_data = caches['local'].get(cache_key)
        if not info_data:
            # If cache miss, fetch data and store it in the cache
            replica_num = next(self.replica_cycle)
            print(f"Forwarding request to replica: {replica_num}")
            info_data, status = get_info(pk, replica_num)
            print("data is not cached")
            caches['local'].set(cache_key, info_data)  # Cache data for 5 minutes
        else:
            # If data is cached, set the status to 200 (OK)
            print("data is cached")
            status = 200
        return Response(info_data, status=status)






