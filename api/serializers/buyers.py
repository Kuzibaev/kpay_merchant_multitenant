from rest_framework import serializers

from buyers import models


class BuyerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        exclude = ('buyer', 'created_at', 'updated_at',)


class BuyerAddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ('name', 'address',)


class BuyerPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber
        exclude = ('buyer', 'created_at', 'updated_at',)


class BuyerPhoneNumberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber
        fields = ('name', 'is_main', 'phone_number')


class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankCard
        exclude = ('buyer', 'created_at', 'updated_at')


class BankCardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankCard
        fields = (
            'card_number',
            'expiry_month',
            'expiry_year',
            'is_main'
        )


class BuyerSerializer(serializers.ModelSerializer):
    addresses = BuyerAddressSerializer(many=True, read_only=True)
    phone_numbers = BuyerPhoneNumberSerializer(many=True, read_only=True)
    bank_cards = BankCardSerializer(many=True, read_only=True)

    class Meta:
        model = models.Buyer
        fields = (
            'id',
            'pnfl',
            'first_name',
            'middle_name',
            'last_name',
            'passport_series',
            'passport_number',
            'passport_issued_by',
            'passport_date_of_issue',
            'passport_date_of_expiry',
            'birth_date',
            'limit',
            'nationality',
            'citizenship',
            'addresses',
            'phone_numbers',
            'bank_cards',
        )


class BuyerSerializerCreate(serializers.ModelSerializer):
    addresses = BuyerAddressCreateSerializer(many=True, read_only=True)
    phone_numbers = BuyerPhoneNumberCreateSerializer(many=True, read_only=True)
    bank_cards = BankCardCreateSerializer(many=True, read_only=True)

    class Meta:
        model = models.Buyer
        exclude = ('limit',)
