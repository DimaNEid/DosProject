
import requests

from order.services_urls_config import URL_CATALOG_INFO, URL_CATALOG_UPDATE

def purchase_book(pk):

    try:
        # Step 1: Get book info using Catalog's info API
        response = requests.get(f"{URL_CATALOG_INFO}/{pk}")
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

                    return {"message": f"Purchased book {book_data['id']}", "new_count": new_count}, 200
                else:
                    return {"error": "Failed to update count in catalog service"}, 500
            else:
                return {"error": "Book is out of stock"}, 400
        else:
            return {"error": "Invalid book ID","data":response.json()}, 404
    except requests.RequestException as e:
        return {"error": f"Error communicating with Catalog Service: {str(e)}"}, 500

# import requests
#
# from order.services_urls_config import URL_CATALOG_INFO, URL_CATALOG_UPDATE
#
#
# def purchase_book(pk):
#     try:
#         # Step 1: Get book info using Catalog's info API
#         response = requests.get(f"{URL_CATALOG_INFO}/{pk}")
#
#         # Handle if Catalog Service responds with an error
#         if response.status_code != 200:
#             return {
#                 "error": "Invalid book ID or failed to fetch book data",
#                 "book_id": pk,
#                 "status_code": response.status_code,
#                 "response_text": response.text
#             }, 404
#
#         # Parse response data
#         book_data = response.json()
#
#         # Step 2: Check if the book is in stock
#         if book_data['count'] > 0:
#             # Step 3: Update the count in the Catalog Service
#             new_count = book_data['count'] - 1
#             update_payload = {
#                 "cost": book_data["cost"],  # Assuming cost remains the same
#                 "count": new_count
#             }
#             update_response = requests.put(f"{URL_CATALOG_UPDATE}/{pk}", json=update_payload)
#
#             if update_response.status_code == 200:
#                 return {"message": f"Purchased book {book_data['id']}", "new_count": new_count}, 200
#             else:
#                 return {
#                     "error": "Failed to update purchase in Order service",
#                     "status_code": update_response.status_code,
#                     "response_text": update_response.text
#                 }, 500
#
#         else:
#             # Book is out of stock
#             return {
#                 "error": "No books available in stock",
#                 "book_id": pk,
#                 "available_count": book_data['count']
#             }, 400
#
#     except requests.RequestException as e:
#         return {
#             "error": f"Error communicating with Catalog Service: {str(e)}"
#         }, 500
