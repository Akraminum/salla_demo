from django.db import models
from django.utils.translation import gettext_lazy as _
from merchants.models import Merchant
 

class Product(models.Model):

    id = models.PositiveIntegerField(_("ID"), primary_key=True)
    merchant = models.ForeignKey(
        Merchant,
        verbose_name=_("Merchant"),
        related_name="products",
        on_delete=models.CASCADE,
    )

    # General
    name = models.TextField(_("Name"))
    description = models.TextField(_("Description"), blank=True, null=True)

    # price_amount = models.DecimalField(_("Price Amount"), default=0)
    # currency_currency = models.CharField(_("Currency"), max_length=255)

    # Quantity
    unlimited_quantity = models.BooleanField(_("Unlimited Quantity"), default=False)
    hide_quantity = models.BooleanField(_("Hide Quantity"), default=False)
    quantity = models.PositiveIntegerField(_("Quantity"), default=0)
    sold_quantity = models.PositiveIntegerField(_("Sold Quantity"), default=0)
    maximum_quantity_per_order = models.PositiveIntegerField(_("Maximum Quantity Per Order"), default=0)
 
 
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

    # Tags
    tags = models.ManyToManyField(
        "product.ProductTag",
        verbose_name=_("Tags"),
        related_name="products",
        blank=True,
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["-id"]

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



class ProductPrice(models.Model):
    """
    Product price model.
    """

    product = models.OneToOneField(
        "product.Product",
        verbose_name=_("Product"),
        related_name="price",
        on_delete=models.CASCADE,
    )

    amount = models.PositiveBigIntegerField(_("Amount"))
    currency = models.CharField(_("Currency"), max_length=5)

    class Meta:
        verbose_name = _("Product Price")
        verbose_name_plural = _("Product Prices")

    def __str__(self):
        return f"{self.product.name} - {self.amount} {self.currency}"


class ProductRegularPrice(models.Model):
    """
    Product regular price model.
    """

    product = models.OneToOneField(
        "product.Product",
        verbose_name=_("Product"),
        related_name="regular_price",
        on_delete=models.CASCADE,
    )

    amount = models.PositiveBigIntegerField(_("Amount"))
    currency = models.CharField(_("Currency"), max_length=5)

    class Meta:
        verbose_name = _("Product Regular Price")
        verbose_name_plural = _("Product Regular Prices")

    def __str__(self):
        return f"{self.product.name} - {self.amount} {self.currency}"


class ProductOption(models.Model):
    """
    Product option model.
    """

    id = models.PositiveBigIntegerField(_("ID"), primary_key=True)
    product = models.ForeignKey(
        "product.Product",
        verbose_name=_("Product"),
        related_name="options",
        on_delete=models.CASCADE,
    )

    # General
    name = models.TextField(_("Name"))
    description = models.TextField(_("Description"), null=True, blank=True)

    # Display Options
    type = models.CharField(_("Type"), max_length=20, choices=[("radio", "Radio"), ("checkbox", "Checkbox")])
    required = models.BooleanField(_("Required"), default=False)
    sort = models.PositiveIntegerField(_("Sort"), null=True, blank=True)
    display_type = models.CharField(
        _("Display Type"),
        max_length=20,
        choices=[("text", "Text"), ("image", "Image"), ("color", "Color")],
    )

    # Visibility
    visibility = models.CharField(
        _("Visibility"),
        max_length=20,
        choices=[("always", "Always"), ("on_condition", "On Condition")],
    )
    visibility_condition_type = models.CharField(
        _("Visibility Condition Type"),
        max_length=5,
        choices=[(">", ">"), ("<", "<"), ("=", "="), ("!=", "!=")],
        null=True,
        blank=True,
    )
    visibility_condition_option = models.ForeignKey(
        "product.ProductOption",
        verbose_name=_("Visibility Condition Option"),
        related_name="visibility_condition_options",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    visibility_condition_value = models.ForeignKey(
        "product.ProductOptionValue",
        verbose_name=_("Visibility Condition Value"),
        related_name="visibility_condition_values",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # Fields in `Salla` API, but not needed in `SallaMobile` API
    # associated_with_order_time = models.BooleanField(_("Associated With Order Time"), default=False)

    class Meta:
        verbose_name = _("Product Option")
        verbose_name_plural = _("Product Options")
        ordering = ["sort"]

    def __str__(self):
        return self.name


class ProductOptionValue(models.Model):
    """
    Product option value model.
    """

    id = models.PositiveBigIntegerField(_("ID"), primary_key=True)
    option = models.ForeignKey(
        "product.ProductOption",
        verbose_name=_("Option"),
        related_name="values",
        on_delete=models.CASCADE,
    )

    name = models.TextField(_("Name"))
    display_value = models.TextField(_("Display Value"), null=True, blank=True)
    image_url = models.URLField(_("Image URL"), null=True, blank=True)
    is_default = models.BooleanField(_("Is Default"), default=False)

    # Fields in `Salla` API, but not needed in `SallaMobile` API
    # hashed_display_value = models.TextField(_("Hashed Display Value"), null=True, blank=True)

    class Meta:
        verbose_name = _("Product Option Value")
        verbose_name_plural = _("Product Option Values")

    def __str__(self):
        return self.name


class ProductOptionValuePrice(models.Model):
    """
    Product option value price model.
    """

    product_option_value = models.OneToOneField(
        "product.ProductOptionValue",
        verbose_name=_("Product Option Value"),
        related_name="price",
        on_delete=models.CASCADE,
    )

    amount = models.PositiveBigIntegerField(_("Amount"))
    currency = models.CharField(_("Currency"), max_length=5)

    class Meta:
        verbose_name = _("Product Option Value Price")
        verbose_name_plural = _("Product Option Value Prices")

    def __str__(self):
        return f"{self.product_option_value.name} - {self.amount} {self.currency}"


class ProductTag(models.Model):
    """
    Product tag model.
    """

    id = models.PositiveBigIntegerField(_("ID"), primary_key=True)

    name = models.TextField(_("Name"))

    class Meta:
        verbose_name = _("Product Tag")
        verbose_name_plural = _("Product Tags")

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """
    Product image model.
    """

    id = models.PositiveBigIntegerField(_("ID"), primary_key=True)
    product = models.ForeignKey(
        "product.Product",
        verbose_name=_("Product"),
        related_name="images",
        on_delete=models.CASCADE,
    )

    url = models.URLField(_("URL"))
    main = models.BooleanField(_("Main"), default=False)
    three_d_image_url = models.URLField(_("3D Image URL"), null=True, blank=True)
    alt = models.TextField(_("Alt"), null=True, blank=True)
    video_url = models.URLField(_("Video URL"), null=True, blank=True)
    type = models.CharField(_("Type"), max_length=20, choices=[("image", "Image"), ("video", "Video")])
    sort = models.PositiveIntegerField(_("Sort"), null=True, blank=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        ordering = ["sort"]

    def __str__(self):
        return self.url

