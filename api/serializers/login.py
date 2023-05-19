from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})


class LoginTokenResponse(serializers.Serializer):
    token = serializers.CharField()
    message = serializers.CharField(required=False)


class LoggedResponse(serializers.Serializer):
    new_user = serializers.BooleanField()
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
