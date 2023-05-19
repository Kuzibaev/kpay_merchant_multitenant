from django_filters import rest_framework as filters
from django_filters.constants import EMPTY_VALUES

from products import models as products_models
from buyers import models as buyers_models
from companies import models as companies_models
from merchants import models as merchants_models
from orders import models as orders_models
from utility.enums import OrderFileTypeEnum


class CategoryParentFilter(filters.NumberFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        if value == 0:
            value = None
        if self.distinct:
            qs = qs.distinct()
        lookup = "%s__%s" % (self.field_name, self.lookup_expr)
        qs = self.get_method(qs)(**{lookup: value})
        return qs


class CategoryFilterSet(filters.FilterSet):
    q = filters.CharFilter(label='Search', field_name='name', lookup_expr='icontains')
    parent = CategoryParentFilter(field_name='parent', lookup_expr='exact')

    class Meta:
        model = products_models.Category
        fields = (
            "q",
            "parent"
        )


class ProductFilterSet(filters.FilterSet):
    q = filters.CharFilter(label='Search', field_name='name', lookup_expr='icontains')

    class Meta:
        model = products_models.Product
        fields = (
            'q',
            'category'
        )


class BuyerFilterSet(filters.FilterSet):
    q = filters.CharFilter(label='Search', field_name='name', lookup_expr='icontains')

    class Meta:
        model = buyers_models.Buyer
        fields = (
            'q',
        )


class CompanyNameFilterSet(filters.FilterSet):
    q = filters.CharFilter(label='Search', field_name='name', lookup_expr='icontains')

    class Meta:
        model = companies_models.CompanyName
        fields = (
            'q',
        )


class MerchantFilterSet(filters.FilterSet):
    q = filters.CharFilter(label='Search', field_name='name', lookup_expr='icontains')

    class Meta:
        model = merchants_models.Merchant
        fields = (
            'q',
        )


class OrderFilterSet(filters.FilterSet):
    q = filters.CharFilter(label='Search', field_name='name', lookup_expr='icontains')

    class Meta:
        model = orders_models.Order
        fields = (
            'q',
        )
