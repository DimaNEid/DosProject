import requests
from fe.services_urls_config import URL_ORDER_PURCHASE

# def make_purchase(data):
#
#     response = requests.post(URL_ORDER_PURCHASE, json=data)
#     if response.status_code == 200:
#         return response.json(), response.status_code
#     return {"error": "Failed to process purchase in Order service"}, response.status_code
#
#

# fe/method/purchase.py

import requests
from fe.services_urls_config import URL_ORDER_PURCHASE

# fe/method/purchase.py

import requests
from fe.services_urls_config import URL_ORDER_PURCHASE

def make_purchase(pk, data):

    # Send the update request to the Order service's specific endpoint
    response = requests.put(f"{URL_ORDER_PURCHASE}{pk}", json=data)
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": "Failed to update purchase in Order service"}, response.status_code
