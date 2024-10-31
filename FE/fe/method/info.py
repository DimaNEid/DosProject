import requests

from fe.services_urls_config import URL_CATALOG_INFO
def get_info(pk):
    response = requests.get(URL_CATALOG_INFO + str(pk))
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": f"Failed to fetch book info from Catalog service, error code {response.status_code}, response: {response.text}"}, response.status_code

