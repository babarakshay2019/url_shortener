from django.conf import settings
from django.shortcuts import get_object_or_404, redirect

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .models import URLMapping
from .serializers import URLMappingSerializer


class URLMappingViewSet(viewsets.ModelViewSet):
    queryset = URLMapping.objects.all()
    serializer_class = URLMappingSerializer
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]

    def create(self, request, *args, **kwargs):
        existing_mapping = URLMapping.objects.filter(long_url=request.data.get("long_url")).first()
        if existing_mapping:
            return Response(
                {
                    "short_url": f"{settings.SHORTENER_DOMAIN}/{existing_mapping.short_code}",
                    "short_code": f"{existing_mapping.short_code}"
                }, 
                status=status.HTTP_200_OK
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url_mapping = serializer.save()
        return Response(
            {"short_url": f"{settings.SHORTENER_DOMAIN}/{url_mapping.short_code}"},
            status=status.HTTP_201_CREATED
        )
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        url_mapping = get_object_or_404(URLMapping, short_code=pk)
        url_mapping.visit_count += 1
        url_mapping.save()        
        return redirect(url_mapping.long_url)
