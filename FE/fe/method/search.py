import requests
from fe.services_urls_config import  URL_CATALOG_SEARCH

def search_books(topic):

    search_url = f"{URL_CATALOG_SEARCH}?topic={topic}"
    response = requests.get(search_url)
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": f"Failed to fetch search results from Catalog service, error code {response.status_code}"}, response.status_code


