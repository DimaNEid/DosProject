import requests

from fe.services_urls_config import URL_CATALOG_INFO, URL_CATALOG_INFO2


def get_info(pk, replica_num):
    if replica_num == 1 :
        response = requests.get(URL_CATALOG_INFO + str(pk))
    else :
        response = requests.get(URL_CATALOG_INFO2 + str(pk))
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": "Failed to fetch book info from Catalog service"}, response.status_code

