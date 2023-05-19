from django.contrib.auth import get_user_model

from rest_framework import serializers

from settings import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'phone',
            'first_name',
            'last_name',
        )


class SettingsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Settings
        fields = (
            'user',
            'full_name',
            'address',
            'company_name',
            'inn',
            'bank_name',
            'bank_account',
            'mfo'
        )


class SettingsCreateSettings(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Settings
        fields = (
            'user',
            'full_name',
            'address',
            'company_name',
            'inn', 'bank_name',
            'bank_account',
            'mfo',
        )
