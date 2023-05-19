from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from api.serializers.image import ImageSerializer
from api.permissions import IsCustomer
from images.models import Image


class ImageViewSet(ModelViewSet):
    parser_classes = (MultiPartParser,)
    permission_classes = (IsCustomer,)
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
