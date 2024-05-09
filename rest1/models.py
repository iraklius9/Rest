from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_("Category"))
    name = models.CharField(max_length=200, verbose_name=_("Product Name"))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_("Price"))
    stock = models.IntegerField(verbose_name=_("Stock"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
