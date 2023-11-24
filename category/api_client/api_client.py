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
from .serializers import CategorySeedSerializer

# Define endpoints, using the provided decorator.
@endpoint(base_url="https://api.salla.dev/admin/v2")
class Endpoint:
    categories = "categories"
    category = "categories/{id}"


def next_page_url(response, previous_page_params):
    ...
    links = response.get("pagination", {}).get("links", [])
    if type(links) == type({}):
        next = links.get("next", None)
        if next:
            return next    


class CategoryAPIClient(APIClient):
    @classmethod
    def client(cls, token) -> Type[APIClient]:
        return cls(
            authentication_method=HeaderAuthentication(token=token),
            response_handler=JsonResponseHandler,
            request_formatter=JsonRequestFormatter,
        )

    @paginated(by_url=next_page_url)
    def get_all_categories_pages(self) -> list[dict]:
        return self.get(Endpoint.categories, params={'per_page':65})

    
    def get_all_categories(self) -> list[dict]:
        all_categories_pages = self.get_all_categories_pages()

        for categories_page in all_categories_pages:
            ser = CategorySeedSerializer(data=categories_page['data'], many=True)
            ser.is_valid(raise_exception=True)
            mapped_data = ser.validated_data
            yield mapped_data


 