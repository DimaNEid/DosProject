from rest_framework import viewsets
from rest_framework.response import Response
from fe.method.purchase import make_purchase
from django.core.cache import caches
import itertools

class PurchaseController(viewsets.ViewSet):
    # Define a list of backend replicas
    BACKEND_REPLICAS = [1, 2]
    # Create a round-robin iterator for replicas
    replica_cycle = itertools.cycle(BACKEND_REPLICAS)
    def update(self, request, pk=None):
        if not pk:
            return Response({"error": "Book ID is required for updating"}, status=400)
        # Forward the request to update the purchase in the Order service
        replica_num = next(self.replica_cycle)
        print(f"Forwarding request to replica: {replica_num}")
        update_data, status = make_purchase(pk, request.data, replica_num)
        """Invalidates the cache entry for the given key."""
        key = "info_" + pk
        # Properly delete the cache key
        caches['local'].delete(key)
        return Response(update_data, status=status)

