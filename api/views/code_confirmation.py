from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

from api.serializers import code_confirmation as code_confirm_ser
from api.permissions import IsCustomer
from credit_cards import models
from utility.enums import StatusUtils
from utility.redis.code_confirmation import CodeConfirmation


class CodeConfirmView(CreateAPIView):
    permission_classes = (IsCustomer,)
    queryset = models.BankCard.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return code_confirm_ser.ConfirmCodeSerializer
        return code_confirm_ser.CardCreateSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)

        card_number = serializer.validated_data['card_number']
        expiry_month = serializer.validated_data['expiry_month']
        expiry_year = serializer.validated_data['expiry_year']

        if card_number and expiry_month and expiry_year:
            bank_card = self.queryset.filter(
                card_number=card_number,
                expiry_month=expiry_month,
                expiry_year=expiry_year
            ).first()
            if bank_card is None:
                bank_card = serializer.save()
                code_token, code = CodeConfirmation.get_code(bank_card.card_number)

                return Response(data=dict(
                    status=StatusUtils.success,
                    message="We sent code.",
                    code=code,
                    code_token=code_token,
                    card_number=bank_card.card_number), status=status.HTTP_200_OK
                )
            elif bank_card.is_verified:
                return Response(data=dict(
                    status=StatusUtils.success,
                    message=_("Try inserting another card with this card")
                ),
                    status=status.HTTP_412_PRECONDITION_FAILED
                )
            else:
                code_token, code = CodeConfirmation.get_code(serializer.validated_data['card_number'])
                return Response(data=dict(
                    message=_(
                        "Your card has not been verified. "
                        "An SMS has been sent to you. "
                        "Please confirm and verify your card.",
                    ),
                    code_token=code_token,
                    code=code
                ),
                    status=status.HTTP_202_ACCEPTED
                )
        return Response(data=dict(
            status=StatusUtils.fail,
            message="Some error occurred. Please try again."),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class CodeConfirmVerifyView(CreateAPIView):
    permission_classes = (IsCustomer,)
    serializer_class = code_confirm_ser.ConfirmCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        code_token, code = serializer.validated_data['code_token'], serializer.validated_data['code']
        card_number = CodeConfirmation.check_code(code_token, code)
        if card_number:
            bank_card = models.BankCard.objects.filter(
                card_number=card_number,
                is_verified=False
            ).first()
            if bank_card is None:
                return Response(
                    data=dict(status=StatusUtils.fail, message=_("")),
                    status=status.HTTP_200_OK
                )
            elif bank_card.is_verified is False:
                bank_card.is_verified = True
                bank_card.save()
                return Response(
                    data=dict(status=StatusUtils.success, message=_("Your card has been verified")),
                    status=status.HTTP_200_OK
                )
        return Response({
            'detail': _('Code is invalid') if card_number is None else _('Card Number does not exist')
        }, status=400
        )
