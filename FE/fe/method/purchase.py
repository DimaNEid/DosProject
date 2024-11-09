import requests
from fe.services_urls_config import URL_ORDER_PURCHASE, URL_ORDER_PURCHASE2


def make_purchase(pk, data, replica_num):
    if replica_num == 1 :
        response = requests.put(f"{URL_ORDER_PURCHASE}{pk}", json=data)
    else :
        response = requests.put(f"{URL_ORDER_PURCHASE2}{pk}", json=data)
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": "Failed to update purchase in Order service"}, response.status_code


