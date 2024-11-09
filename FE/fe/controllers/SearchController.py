from rest_framework import viewsets
from rest_framework.response import Response
from fe.method.search import search_books
from django.core.cache import caches
import itertools

class SearchController(viewsets.ViewSet):
    # Define a list of backend replicas
    BACKEND_REPLICAS = [1, 2]

    # Create a round-robin iterator for replicas
    replica_cycle = itertools.cycle(BACKEND_REPLICAS)

    def list(self, request):
        topic = request.query_params.get('topic')

        if not topic:
            return Response({"error": "Book Topic parameter is required"}, status=400)

        # Create a unique cache key for the topic
        cache_key = f"search_{topic}"
        search_data = caches['local'].get(cache_key)

        if search_data is None:
            # Cache miss: Fetch fresh data using round-robin load balancing
            replica_num = next(self.replica_cycle)  # Get the next replica in round-robin order
            print(f"Forwarding request to replica: {replica_num}")
            # Modify search_books to accept the replica URL if needed
            search_data, status = search_books(topic, replica_num)
            # Cache the fetched data for 5 minutes
            caches['local'].set(cache_key, search_data)
        else:
            # Cache hit, set the status to 200 (OK)
            print("Data retrieved from cache")
            status = 200

        return Response(search_data, status=status)




