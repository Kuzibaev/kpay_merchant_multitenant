from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS
from django_filters import rest_framework as filters

from api.permissions import IsCustomer
from api.filters import CategoryFilterSet, ProductFilterSet
from api.serializers import products
from products import models


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsCustomer,)
    queryset = models.Category.objects.all()
    search_fields = ('name', 'description')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CategoryFilterSet

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return products.CategorySerializer
        return products.CategoryCreateSerializer


class ProductViewSet(ModelViewSet):
    permission_classes = (IsCustomer,)
    queryset = models.Product.objects.all()
    search_fields = ('name', 'serial_number')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilterSet

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return products.ProductSerializer
        return products.ProductCreateSerializer
