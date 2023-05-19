from django.http import Http404
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.response import Response

from api.permissions import IsCustomer
from api.serializers.users import SettingsSerializer, SettingsCreateSettings, UserSerializer
from settings import models


class User(RetrieveAPIView):
    permission_classes = (IsCustomer,)
    serializer_class = UserSerializer

    def get_object(self, *args, **kwargs):
        return self.request.user


class SettingsCreateAPIView(CreateAPIView):
    permission_classes = (IsCustomer,)
    serializer_class = SettingsCreateSettings

    def create(self, request, *args, **kwargs):
        user = request.user
        settings = models.Settings.objects.filter(user=user).first()
        if settings:
            serializer = self.get_serializer(settings, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SettingsRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsCustomer,)
    serializer_class = SettingsSerializer
    queryset = models.Settings.objects.all()

    def get_object(self):
        user = self.request.user
        settings = models.Settings.objects.filter(user=user).first()
        if not settings:
            raise Http404
        return settings

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SettingsUpdateAPIView(UpdateAPIView):
    permission_classes = (IsCustomer,)
    serializer_class = SettingsSerializer

    def get_object(self):
        user = self.request.user
        obj_ = models.Settings.objects.filter(user=user)
        return obj_

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
