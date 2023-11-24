from datetime import date

from django.utils.timezone import datetime
from rest_framework import exceptions

from category.utilities import CategoryUtility

from .models import Merchant as MerchantModel
from .models import MerchantToken as MerchantTokensModel
from .models import UserInfo as UserInfoModel

from product.utilities import ProductUtility


class InvalidExpiresDate(exceptions.APIException):
    status_code = 400
    default_detail = "Invalid expires date."
    default_code = "invalid_expires_date"


class MerchantUtility:
    """
    A class for handling merchants.
    """

    @staticmethod
    def _get_expires_date(expires):
        """
        Get the expires date.
        """
        if isinstance(expires, int):
            return datetime.fromtimestamp(expires)
        elif isinstance(expires, float):
            return datetime.fromtimestamp(int(expires))
        elif isinstance(expires, str):
            return datetime.fromisoformat(expires)
        elif isinstance(expires, date):
            return expires
        else:
            raise InvalidExpiresDate(expires.__class__.__name__)

    @staticmethod
    def get_or_create_merchant(merchant_id):
        """
        Get or create a merchant.
        """
        try:
            merchant = MerchantModel.objects.get(id=merchant_id)
        except MerchantModel.DoesNotExist:
            merchant = MerchantModel.objects.create(id=merchant_id)

        return merchant

    @staticmethod
    def update_or_create_tokens(merchant, access_token, refresh_token, expires):
        """
        Get or create merchant tokens.
        """
        try:
            tokens = MerchantTokensModel.objects.get(merchant=merchant)
            tokens.access_token = access_token
            tokens.refresh_token = refresh_token
            tokens.expires = MerchantUtility._get_expires_date(expires)
            tokens.save()
        except MerchantTokensModel.DoesNotExist:
            tokens = MerchantTokensModel.objects.create(
                merchant=merchant,
                access_token=access_token,
                refresh_token=refresh_token,
                expires=MerchantUtility._get_expires_date(expires),
            )

        return tokens
    
    @staticmethod
    def update_user_info(merchant, data):
        """
        Update the merchant info.
        """
        user_info, _ = UserInfoModel.objects.get_or_create(merchant=merchant)
        user_info.name = data["name"]
        user_info.email = data["email"]
        user_info.mobile = data["mobile"]
        user_info.save()
        return True

    @staticmethod
    def update_products(merchant, products):
        """
        Update the merchant products.
        """
        merchant.products.all().delete()
        for product in products:
            merchant.products.create(
                id=product["id"],
                name=product["name"],
            )

        return


    @staticmethod
    def get_merchant_token(merchant_id):
        try:
            token = MerchantTokensModel.objects.get(merchant=merchant_id)
            return token
        except MerchantTokensModel.DoesNotExist:
            return None

    @staticmethod
    def populate_database(merchant_id, access_token):
        ...
        # ProductUtility.populate_database(merchant_id, access_token)
        CategoryUtility.populate_database(merchant_id, access_token)
    