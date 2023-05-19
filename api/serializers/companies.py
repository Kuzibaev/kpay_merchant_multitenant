from rest_framework import serializers

from companies import models
from merchants import models as mer_models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyName
        exclude = (
            'created_at',
            'updated_at',
        )


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = mer_models.Merchant
        exclude = (
            'created_at',
            'updated_at',
        )
