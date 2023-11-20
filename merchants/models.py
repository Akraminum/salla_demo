from django.conf import settings
from django.db import models
from django.utils.timezone import datetime, timedelta
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel


class Merchant(TimeStampedModel):
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        verbose_name = "Merchant"
        verbose_name_plural = "Merchants"


class MerchantToken(TimeStampedModel):
    merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE, related_name="token")
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    expires = models.DateField()

    class Meta:
        verbose_name = "Merchant Token"
        verbose_name_plural = "Merchant Tokens"

    def is_expired(self):
        """
        Check if the token is expired. access token duration is 10 day.
        """
        current_date = datetime.now().date()
        if settings.DEBUG:
            max_date = self.expires + timedelta(days=1)
        else:
            max_date = self.expires + timedelta(days=10)
        if isinstance(max_date, datetime):
            max_date = max_date.date()
        return current_date > max_date


class UserInfo(TimeStampedModel):
    merchant = models.OneToOneField(Merchant, on_delete=models.CASCADE, related_name="info")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=255)

    class Meta:
        verbose_name = "User Info"
        verbose_name_plural = "User Info"


class MerchantBanner(TimeStampedModel):
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        related_name="banners",
    )
    image = models.ImageField(upload_to="merchant/banners")

    class Meta:
        verbose_name = "Merchant Banner"
        verbose_name_plural = "Merchant Banners"

    def __str__(self):
        # TODO: change `self.merchant` to be `self.merchant.name`
        return f"{self.merchant} - {self.image.name}"


class MerchantSpecialOffer(TimeStampedModel):
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        related_name="special_offers",
    )

    id = models.PositiveBigIntegerField(_("ID"), primary_key=True)
    message = models.TextField(_("Special Offer Message"))

    class Meta:
        verbose_name = "Merchant Special Offer"
        verbose_name_plural = "Merchant Special Offers"

    def __str__(self):
        return f"{self.merchant} - {self.message}"
    

    