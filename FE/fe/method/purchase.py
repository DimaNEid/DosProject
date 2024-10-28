import requests
from fe.services_urls_config import URL_ORDER_PURCHASE

def make_purchase(data):

    response = requests.post(URL_ORDER_PURCHASE, json=data)
    if response.status_code == 200:
        return response.json(), response.status_code
    return {"error": "Failed to process purchase in Order service"}, response.status_code


# import requests
#
# def make_purchase(data):
#     """Sends a POST request to the Order service to process the purchase."""
#     order_url = "http://127.0.0.1:8002/order/purchase/"
#     response = requests.post(order_url, json=data)
#     if response.status_code == 200:
#         return response.json()
#     return {"error": "Failed to process purchase in Order service"}, response.status_code
