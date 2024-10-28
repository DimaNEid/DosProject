import requests
from fe.services_urls_config import  URL_CATALOG_SEARCH

def search_books(topic):

    search_url = f"{URL_CATALOG_SEARCH}?topic={topic}"
    response = requests.get(search_url)
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": "Failed to fetch search results from Catalog service"}, response.status_code


# import requests
#
# def search_books(topic):
#     """Sends a GET request to the Catalog service to search for books."""
#     catalog_url = f"http://127.0.0.1:8000/catalog/search/?topic={topic}"
#     response = requests.get(catalog_url)
#     if response.status_code == 200:
#         return response.json()
#     return {"error": "Failed to fetch search results from Catalog service"}, response.status_code

