from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers.login import LoginSerializer
from users.models import Customer


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    queryset = Customer.objects.all()

    def post(self, reqeust):
        serializer = self.serializer_class(data=reqeust.data)
        serializer.is_valid(raise_exception=True)
        phone, password = serializer.data['phone'], serializer.data['password']
        if phone:
            if phone:
                user = self.queryset.filter(phone=phone).first()
                if user:
                    refresh_token = RefreshToken.for_user(user)
                    return Response(data=dict(
                        access_token=str(refresh_token.access_token),
                        refresh_token=str(refresh_token),
                    ), status=200)
            return Response({
                'detail': _('Phone invalid') if phone is None else _('Password invalid')
            }, status=400)
        return Response({
            'detail': _('Phone does\'not exists')
        }, status=400)
