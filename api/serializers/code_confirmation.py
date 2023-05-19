from rest_framework import serializers

from credit_cards import models


class CardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankCard
        exclude = ('is_verified',)


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankCard
        exclude = ('is_verified',)


class ConfirmCodeSerializer(serializers.Serializer):
    code_token = serializers.CharField()
    code = serializers.CharField()
