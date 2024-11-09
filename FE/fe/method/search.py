import requests
from fe.services_urls_config import URL_CATALOG_SEARCH, URL_CATALOG_SEARCH2


def search_books(topic, replica_num):
    if replica_num == 1 :
        search_url = f"{URL_CATALOG_SEARCH}?topic={topic}"
    else :
        search_url = f"{URL_CATALOG_SEARCH2}?topic={topic}"
    response = requests.get(search_url)
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": "Failed to fetch search results from Catalog service"}, response.status_code


