from typing import Optional, Type
from apiclient import (
    APIClient,
    endpoint,
    paginated,
    retry_request,
    HeaderAuthentication,
    JsonResponseHandler,
    JsonRequestFormatter,
)
from apiclient.error_handlers import BaseErrorHandler, ErrorHandler
from apiclient.exceptions import APIClientError
from apiclient.request_strategies import BaseRequestStrategy

# Define endpoints, using the provided decorator.
@endpoint(base_url="https://api.salla.dev/admin/v2")
class Endpoint:
    products = "products"
    product = "products/{id}"


def next_page_url(response, previous_page_params):
    ...
    links = response.get("pagination", {}).get("links", [])
    if type(links) == type({}):
        next = links.get("next", None)
        if next:
            return next    

# TODO:
    # override UrlPaginatedRequestStrategy to yield pages
from apiclient.exceptions import UnexpectedError
class ProductAPIClient(APIClient):
    @classmethod
    def client(cls, token) -> Type[APIClient]:
        return cls(
            authentication_method=HeaderAuthentication(token=token),
            response_handler=JsonResponseHandler,
            request_formatter=JsonRequestFormatter,
        )

    @paginated(by_url=next_page_url)
    def get_all_products_pages(self) -> list[dict]:
        return self.get(Endpoint.products, params={'per_page':65})

    
    def get_all_products(self) -> list[dict]:
        all_products_pages = self.get_all_products_pages()
        for products_page in all_products_pages:
            yield products_page['data']

    @retry_request
    def get_product(self, todo_id: int) -> dict:
        url = Endpoint.product.format(id=todo_id)
        return self.get(url, )

   



# client = ProductAPIClient.client()

# print(
#     client.get_all_products_pages()
# )