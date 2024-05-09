from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest1.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
