from django.db import models
from django.utils.translation import gettext_lazy as _
from merchants.models import Merchant
 

  
class Product(models.Model):
    id = models.PositiveIntegerField(_("ID"), primary_key=True)
    #region General
    name = models.TextField(_("Name"))
    description = models.TextField(_("Description"), blank=True, null=True)
    #endregion

    #region Prices
    price_amount = models.DecimalField(_("Price"), max_digits=8, decimal_places=2, default=0)
    taxed_price_amount = models.DecimalField(_("taxed_price_amount"), max_digits=8, decimal_places=2, default=0)
    pre_tax_price_amount = models.DecimalField(_("pre_tax_price_amount"), max_digits=8, decimal_places=2, default=0)
    tax_amount = models.DecimalField(_("tax_amount"), max_digits=8, decimal_places=2, default=0)
    cost_price = models.DecimalField(_("cost_price"), max_digits=8, decimal_places=2, default=0)
    regular_price_amount = models.DecimalField(_("regular_price_amount"), max_digits=8, decimal_places=2, default=0)
    price_currency = models.CharField(_("Price Currency"), max_length=3, default="SAR")
    #endregion

    #region commented

    # type = models.CharField(_("Type"), max_length=255) # max_length=255, choices=Product.TYPE_CHOICES, default=Product.TYPE_PRODUCT)
    # status = models.CharField(_("Status"), max_length=255) # max_length=255, choices=Product.STATUS_CHOICES, default=Product.STATUS_ACTIVE)
    # is_available = models.BooleanField(_("Is Available"), default=True)
    # views = models.PositiveIntegerField(_("Views"), default=0)
    # require_shipping = models.BooleanField(_("Require Shipping"), default=False)
    # cost_price = models.CharField(_("Cost Price"), blank=True, max_length=255)
    # weight = models.PositiveIntegerField(_("Weight"), default=0)
    # weight_type = models.CharField(_("Weight Type"), max_length=255, blank=True)
    # with_tax = models.BooleanField(_("With Tax"), default=True)
    # url = models.URLField(_("URL"))
    # main_image = models.URLField(_("Main Image"))
    # short_link_code = models.CharField(_("Short Link Code"), max_length=255, blank=True)
    # calories = models.PositiveIntegerField(_("Calories"), default=0)

    #endregion


    #region Relations
    merchant = models.ForeignKey(
        Merchant,
        verbose_name=_("Merchant"),
        related_name="products",
        on_delete=models.CASCADE,
    )

    tags = models.ManyToManyField(
        "product.ProductTag",
        verbose_name=_("Tags"),
        related_name="products",
        blank=True,
    )

    categories  = models.ManyToManyField(
        "category.category",
        verbose_name=_("Categories"),
        related_name="products",
        blank=True,
    )
    #endregion

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["-id"]

    #region Methods
    def __str__(self):
        return self.name

    def get_product_quantity(self):
        """
        Get product quantity.
        """
        if self.hide_quantity:
            return "Hidden"
        if self.unlimited_quantity:
            return "Unlimited"
        return self.quantity

    def get_product_sold_quantity(self):
        """
        Get product sold quantity.
        """
        if self.hide_quantity:
            return "Hidden"
        return self.sold_quantity

    def get_rating_total(self):
        """
        Get total rating.
        """
        return sum([rating.rate for rating in self.ratings.all()])

    def get_rating_count(self):
        """
        Get total rating.
        """
        return self.ratings.count()

    def get_rating_avg(self):
        """
        Get average rating.
        """
        rating_count = self.get_rating_count()
        if rating_count == 0:
            return 0
        return self.get_rating_total() / rating_count
    
    #endregion
