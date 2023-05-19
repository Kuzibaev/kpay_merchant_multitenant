from typing import Optional

from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from products import models


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = "__all__"

    @extend_schema_field(Optional[str])
    def get_parent(self, obj: models.Category):
        if obj.parent:
            return CategorySerializer(obj.parent).data
        else:
            return None


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('name', 'description', 'parent',)
        extra_kwargs = {
            'parent': {'required': False}
        }


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
