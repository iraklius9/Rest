from django.urls import path
from rest1.views import ProductList, ProductDetail, CreateProduct, DeleteProduct, UpdateProduct

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/create/', CreateProduct.as_view(), name='product-create'),
    path('products/delete/<int:pk>', DeleteProduct.as_view(), name='product-delete'),
    path('products/update/<int:pk>', UpdateProduct.as_view(), name='product-update'),
]
