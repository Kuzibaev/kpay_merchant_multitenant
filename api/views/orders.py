import pdfkit
from dateutil.relativedelta import relativedelta
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from main.settings.base import wkhtml_to_pdf

from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from api.permissions import IsCustomer
from api.filters import OrderFilterSet
from api.serializers import orders as orders_ser

from orders import models as order_models
from utility.enums import OrderFileTypeEnum, StatusEnum


class OderViewSet(ModelViewSet):
    permission_classes = (IsCustomer,)
    queryset = order_models.Order.objects.filter(status=StatusEnum.OPENED)
    filter_backends = (filters.DjangoFilterBackend,)
    search_fields = ()
    filterset_class = OrderFilterSet

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return orders_ser.OrderSerializer
        return orders_ser.OrderSerializerCreate

    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.kwargs.get('pk'))
        return obj

    def create(self, request, *args, **kwargs):
        serializer = orders_ser.OrderSerializerCreate(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = serializer.save()
        end_date = order.created_at + relativedelta(months=+order.interval)
        order.end_date = end_date
        order.save()

        products_data = request.data.get('products', [])
        order_items_data = request.data.get('order_items', [])

        for product in products_data:
            product_serializer = orders_ser.OrderProductSerializerCreate(data=product)
            product_serializer.is_valid(raise_exception=True)
            product_serializer.save(order=order)

        for i, order_item in enumerate(order_items_data):
            i += 1
            order_item_serializer = orders_ser.OrderItemSerializerCreate(data=order_item)
            order_item_serializer.is_valid(raise_exception=True)
            order_item_serializer.save(order=order, order_by=i)

        serializer = self.get_serializer_class()(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.status = StatusEnum.CLOSED
        obj.save()
        return Response(data=dict(status=_("Successfully closed")), status=status.HTTP_200_OK)


class OrderExportView(RetrieveAPIView):
    permission_classes = (IsCustomer,)
    serializer_class = orders_ser.OrderSerializer
    lookup_field = 'order_id'
    queryset = order_models.Order.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs['order_id'])
        return obj

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()
        config = pdfkit.configuration(wkhtmltopdf=wkhtml_to_pdf)
        file_type = request.query_params.get('type', None)
        if file_type == OrderFileTypeEnum.pdf.value:
            pdf = pdfkit.from_string(
                render_to_string(
                    'order_detail.html', context={'order': self.serializer_class(order).data}
                ),
                options={
                    'page-size': 'A4',
                    'margin-top': '0.1in',
                    'margin-right': '0.1in',
                    'margin-bottom': '0.1in',
                    'margin-left': '0.1in',
                },
                configuration=config,
            )

            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="order_detail_{order.id}.pdf"'
            return response
        elif file_type == OrderFileTypeEnum.excel.value:
            return Response(data=_(""), status=status.HTTP_200_OK)
        return super().retrieve(request, *args, **kwargs)
