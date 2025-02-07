from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework import serializers

from .models import URLMapping


class URLMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLMapping
        fields = ['long_url', 'short_code', 'visit_count']
    
    def validate_long_url(self, value):
        validator = URLValidator()
        try:
            validator(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid URL format")
        return value
    
    def create(self, validated_data):
        url_mapping, created = URLMapping.objects.get_or_create(long_url=validated_data['long_url'])
        return url_mapping

