from django.urls import path

from rest1.views import ProductList, ProductDetail, CreateProduct, DeleteProduct, UpdateProduct

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('products/create/', CreateProduct.as_view()),
    path('products/<int:pk>/delete/', DeleteProduct.as_view()),
    path('products/<int:pk>/update/', UpdateProduct.as_view()),
]
