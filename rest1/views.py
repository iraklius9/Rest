from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status, generics
from rest1.models import Product
from rest1.serializers import ProductSerializer, ProductStockSerializer, ProductDetailSerializer


def home(request):
    return render(request, 'home.html')


class CreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAdminUser]


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DeleteProduct(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]


class UpdateProduct(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductStockSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]
