import requests
from fe.services_urls_config import URL_ORDER_PURCHASE, URL_ORDER_PURCHASE2
from django.core.cache import caches, cache


def invalidate(pk):
    """Invalidates the cache entry for the given key if it exists."""
    print("invalidate")
    print(pk)
    key = "info_" + pk
    # Check if the cache key exists
    if caches['local'].get(key) is not None:
        caches['local'].delete(key)
        return f"Cache entry for {key} invalidated."
    else:
        return f"No cache entry found for {key}."






