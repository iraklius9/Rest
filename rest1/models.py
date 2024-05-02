from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Product Name"))
    price = models.FloatField(verbose_name=_("Product Price"))
    stock = models.IntegerField(verbose_name=_("Stock"))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_("Category"))

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
