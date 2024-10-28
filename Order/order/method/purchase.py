#
# from http.client import responses
# import requests
# from purchase.services_urls_config import URL_CATALOG_INFO, URL_CATALOG_UPDATE
#
#
# # def get_book_info(pk):
# #     print("h")
# #
# #     try:
# #         response = requests.get(f"{URL_CATALOG_INFO}{pk}")
# #         if response.status_code == 200:
# #             return response.json(), response.status_code
# #         return {"error": "Failed to fetch book info from Catalog service"}, response.status_code
# #     except requests.RequestException as e:
# #         return {"error": f"Request to Catalog service failed: {str(e)}"}, 500
#
# def get_book_info(pk):
#     """Test fetching book information with a simple request."""
#     url = f"http://127.0.0.1:8000/catalog/info/{pk}"
#     print(f"Debug: Fetching book info from URL: {url}")
#
#     try:
#         response = requests.get(url)
#         print(f"Debug: Response Status Code: {response.status_code}")
#         if response.status_code == 200:
#             print(f"Debug: Response Data: {response.json()}")
#             return response.json(), response.status_code
#
#         print(f"Error: Failed to fetch book info, Response: {response.text}")
#         return {"error": "Failed to fetch book info from Catalog service"}, response.status_code
#     except requests.RequestException as e:
#         print(f"Exception: Request failed: {str(e)}")
#         return {"error": f"Request failed: {str(e)}"}, 500
#
#
# def update_book_count(pk, updated_count):
#
#     try:
#         response = requests.put(f"{URL_CATALOG_UPDATE}{pk}/", json={"count": updated_count})
#         if response.status_code == 200:
#             return response.json(), response.status_code
#         return {"error": "Failed to update book count in Catalog service"}, response.status_code
#     except requests.RequestException as e:
#         return {"error": f"Request to Catalog service failed: {str(e)}"}, 500
#
#
# def handle_purchase(pk, quantity):
#
#     # Step 1: Get the current book information from the Catalog service
#     book_info, status_code = get_book_info(pk)
#
#     # Check if the request was successful and the "count" key is present in the response
#     if status_code != 200:
#         return {"error": "Failed to fetch book information"}, status_code
#
#     if "count" not in book_info:
#         return {"error": "Book information does not contain 'count'"}, 400
#
#     # Step 2: Check if there are enough books in stock
#     if book_info["count"] < quantity:
#         return {"error": "Purchase process can't be completed, not enough books in stock"}, 400
#
#     # Step 3: Calculate the new count and update the Catalog service
#     updated_count = book_info["count"] - quantity
#
#     # Step 4: Send the updated count to the Catalog service
#     return update_book_count(pk, updated_count)

import requests

from order.services_urls_config import URL_CATALOG_INFO, URL_CATALOG_UPDATE


def purchase_book(pk):
    """Handles the logic of purchasing a book."""
    try:
        # Step 1: Get book info using Catalog's info API
        response = requests.get(f"{URL_CATALOG_INFO}{pk}")
        if response.status_code == 200:
            book_data = response.json()

            # Step 2: Check if the book is in stock
            if book_data['count'] > 0:
                # Step 3: Update the count in the Catalog Service
                new_count = book_data['count'] - 1
                update_payload = {
                    "cost": book_data["cost"],  # Assuming cost remains the same
                    "count": new_count
                }
                update_response = requests.put(f"{URL_CATALOG_UPDATE}{pk}", json=update_payload)

                if update_response.status_code == 200:
                    # Successfully purchased
                    return {"message": f"Purchased book {book_data['id']}", "new_count": new_count}, 200
                else:
                    return {"error": "Failed to update count in catalog service"}, 500
            else:
                return {"error": "Book is out of stock"}, 400
        else:
            return {"error": "Invalid book ID"}, 404
    except requests.RequestException as e:
        return {"error": f"Error communicating with Catalog Service: {str(e)}"}, 500