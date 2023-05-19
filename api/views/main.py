from django.contrib.auth.hashers import make_password
from django.core.management import call_command
from django.db import connection, connections
from phonenumber_field.phonenumber import PhoneNumber
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers.orders import MainSerializer
from api.serializers.tenants import TenantSerializer
from orders.models import Order
from tenants.helpers import add_tenant_into_connections
from tenants.models import Tenant
# from users.models import User
from django.contrib.auth.models import User

from users.models import SuperUser, Customer


class MainView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = MainSerializer

    def retrieve(self, *args, **kwargs):
        # TODO: must calculate Order statistics
        result_ = {
            'total_sum': 1000000,
            'total_sum_paid': 300000,
            'total_sum_not_paid': 2000000,
            'total_sum_must_pay_today': 1000000,
            'total_sum_month_year': 1000000000000,
        }

        serializer = self.get_serializer(result_)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TenantCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        db = serializer.data['name']
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE \"{db}\"")
        add_tenant_into_connections(connections, db)
        call_command("migrate", database=db)
        # phone = PhoneNumber.from_string('+998901234567')
        # superuser = SuperUser.objects.create(
        #     phone=phone,
        #     password=make_password('123'),
        # )
        # superuser.save(using=db)
        # print('superuser')
        # phone_ = PhoneNumber.from_string('+998901234568')
        # user_ = Customer.objects.create(
        #     phone=phone_,
        #     password=make_password('123')
        # )
        # user_.save(using=db)
        # print('created customer')
