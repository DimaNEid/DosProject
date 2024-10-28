# from http.client import responses
#
# import requests
#
# from urllib3 import request
#
# from order.services_urls_config import URL_CATALOG_INFO
# from order.services_urls_config import URL_CATALOG_UPDATE
#
#
# def get_book_info(pk):
#     response = requests.get(f"{URL_CATALOG_INFO}{pk}/")
#     if response.status_code == 200:
#         return response.json(), response.status_code
#     return {"error": "Failed to fetch book info from Catalog service"}, response.status_code
#
# def update_book_count(pk, updated_count):
#     response = requests.put(f"{URL_CATALOG_UPDATE}{pk}/",json={"updated_count": updated_count})
#     if response.status_code == 200:
#         return response.json(), response.status_code
#     return{"error": "Failed to update book count from Catalog service"}, response.status_code
#
# def handle_purchase(pk,quantity):
#     book_info, status_code = get_book_info(pk)
#     if status_code == 200:
#         return book_info, status_code
#
#     if book_info["count"]<quantity:
#         return {"error":"purchase process can't be completed, Not enough books in stock"},400
#
#     update_count = book_info["count"] - quantity
#
#     return update_book_count(pk,update_count)


from http.client import responses
import requests
from order.services_urls_config import URL_CATALOG_INFO, URL_CATALOG_UPDATE


# def get_book_info(pk):
#     print("h")
#
#     try:
#         response = requests.get(f"{URL_CATALOG_INFO}{pk}")
#         if response.status_code == 200:
#             return response.json(), response.status_code
#         return {"error": "Failed to fetch book info from Catalog service"}, response.status_code
#     except requests.RequestException as e:
#         return {"error": f"Request to Catalog service failed: {str(e)}"}, 500

def get_book_info(pk):
    """Test fetching book information with a simple request."""
    url = f"http://127.0.0.1:8000/catalog/info/{pk}"
    print(f"Debug: Fetching book info from URL: {url}")

    try:
        response = requests.get(url)
        print(f"Debug: Response Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Debug: Response Data: {response.json()}")
            return response.json(), response.status_code

        print(f"Error: Failed to fetch book info, Response: {response.text}")
        return {"error": "Failed to fetch book info from Catalog service"}, response.status_code
    except requests.RequestException as e:
        print(f"Exception: Request failed: {str(e)}")
        return {"error": f"Request failed: {str(e)}"}, 500


def update_book_count(pk, updated_count):

    try:
        response = requests.put(f"{URL_CATALOG_UPDATE}{pk}/", json={"count": updated_count})
        if response.status_code == 200:
            return response.json(), response.status_code
        return {"error": "Failed to update book count in Catalog service"}, response.status_code
    except requests.RequestException as e:
        return {"error": f"Request to Catalog service failed: {str(e)}"}, 500


def handle_purchase(pk, quantity):

    # Step 1: Get the current book information from the Catalog service
    book_info, status_code = get_book_info(pk)

    # Check if the request was successful and the "count" key is present in the response
    if status_code != 200:
        return {"error": "Failed to fetch book information"}, status_code

    if "count" not in book_info:
        return {"error": "Book information does not contain 'count'"}, 400

    # Step 2: Check if there are enough books in stock
    if book_info["count"] < quantity:
        return {"error": "Purchase process can't be completed, not enough books in stock"}, 400

    # Step 3: Calculate the new count and update the Catalog service
    updated_count = book_info["count"] - quantity

    # Step 4: Send the updated count to the Catalog service
    return update_book_count(pk, updated_count)
