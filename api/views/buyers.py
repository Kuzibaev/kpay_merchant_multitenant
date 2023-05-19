from rest_framework import status
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from api.filters import BuyerFilterSet
from api.serializers import buyers
from api.permissions import IsCustomer

from buyers import models


class BuyerViewSet(ModelViewSet):
    permission_classes = (IsCustomer,)
    queryset = models.Buyer.objects.all()
    search_fields = ('pnfl', 'first_name', 'last_name', 'middle_name')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BuyerFilterSet

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return buyers.BuyerSerializer
        return buyers.BuyerSerializerCreate

    def create(self, request, *args, **kwargs):
        # Create a new instance of the BuyerSerializerCreate serializer with the request data
        serializer = buyers.BuyerSerializerCreate(data=request.data)

        # Validate the serializer data and raise an exception if it is invalid
        serializer.is_valid(raise_exception=True)

        # Save the validated serializer data to create a new buyer object
        buyer = serializer.save()

        # Get the addresses, phone numbers, and bank cards data from the request data
        addresses_data = request.data.get('addresses', [])
        phone_numbers_data = request.data.get('phone_numbers', [])
        bank_cards_data = request.data.get('bank_cards', [])

        # Create a new address object for each address data item and associate it with the new buyer object
        for address in addresses_data:
            address_serializer = buyers.BuyerAddressCreateSerializer(data=address)
            address_serializer.is_valid(raise_exception=True)
            address_serializer.save(buyer=buyer)

        # Create a new phone number object for each phone number data item and associate it with the new buyer object
        for phone_number in phone_numbers_data:
            phone_number_serializer = buyers.BuyerPhoneNumberCreateSerializer(data=phone_number)
            phone_number_serializer.is_valid(raise_exception=True)
            phone_number_serializer.save(buyer=buyer)

        # Create a new bank card object for each bank card data item and associate it with the new buyer object
        for bank_card in bank_cards_data:
            bank_cards_serializer = buyers.BankCardCreateSerializer(data=bank_card)
            bank_cards_serializer.is_valid(raise_exception=True)
            bank_cards_serializer.save(buyer=buyer)

        # Serialize the new buyer object and return it in the response with a 201 Created status code
        response_serializer = self.get_serializer_class()(buyer)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):

        buyer = self.get_object()

        # Delete all child objects
        buyer.addresses.all().delete()
        buyer.phone_numbers.all().delete()
        buyer.bank_cards.all().delete()

        # Recreate child objects from request data
        addresses_data = request.data.get('addresses', [])
        phone_numbers_data = request.data.get('phone_numbers', [])
        bank_cards_data = request.data.get('bank_cards', [])

        for address in addresses_data:
            address_serializer = buyers.BuyerAddressCreateSerializer(data=address)
            address_serializer.is_valid(raise_exception=True)
            address_serializer.save(buyer=buyer)

        for phone_number in phone_numbers_data:
            phone_number_serializer = buyers.BuyerPhoneNumberCreateSerializer(data=phone_number)
            phone_number_serializer.is_valid(raise_exception=True)
            phone_number_serializer.save(buyer=buyer)

        for bank_card in bank_cards_data:
            bank_cards_serializer = buyers.BankCardCreateSerializer(data=bank_card)
            bank_cards_serializer.is_valid(raise_exception=True)
            bank_cards_serializer.save(buyer=buyer)

        # Update buyer object
        serializer = buyers.BuyerSerializerCreate(buyer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Return response
        response_serializer = self.get_serializer_class()(buyer)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
