import requests

from fe.services_urls_config import URL_CATALOG_INFO
def get_info(pk):
    response = requests.get(URL_CATALOG_INFO + str(pk))
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": "Failed to fetch info from Catalog service"}, response.status_code

# import requests
#
# def get_info():
#     """Fetches information from the Catalog service."""
#     catalog_url = "http://127.0.0.1:8000/catalog/info/"
#     response = requests.get(catalog_url)
#     if response.status_code == 200:
#         return response.json()
#     return {"error": "Failed to fetch info from Catalog service"}, response.status_code

