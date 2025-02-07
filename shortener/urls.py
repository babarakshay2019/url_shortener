from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import URLMappingViewSet

router = DefaultRouter()
router.register(r'shorten', URLMappingViewSet, basename='shorten')

urlpatterns = [
    path('', include(router.urls)),
]