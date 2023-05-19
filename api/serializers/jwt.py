from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as _TokenObtainPairSerializer,
    PasswordField,
)


class TokenObtainPairSerializer(_TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = PhoneNumberField()
        self.fields["password"] = PasswordField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
