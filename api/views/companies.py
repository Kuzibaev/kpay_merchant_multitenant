from django_filters import rest_framework as filters

from rest_framework.viewsets import ModelViewSet

from api.serializers import companies
from api.permissions import IsCustomer
from api.filters import CompanyNameFilterSet, MerchantFilterSet
from companies import models
from merchants import models as mer_models


class CompanyViewSet(ModelViewSet):
    permission_classes = (IsCustomer,)
    queryset = models.CompanyName.objects.all()
    serializer_class = companies.CompanySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    search_fields = ('full_name', 'company_name',)
    filterset_class = CompanyNameFilterSet


class MerchantViewSet(ModelViewSet):
    permission_classes = (IsCustomer,)
    serializer_class = companies.MerchantSerializer
    queryset = mer_models.Merchant.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    search_fields = ('type', 'name', 'phone')
    filterset_class = MerchantFilterSet
