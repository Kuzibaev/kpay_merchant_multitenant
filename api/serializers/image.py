from rest_framework import serializers

from images import models


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = models.Image
        fields = "__all__"
