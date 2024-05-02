from django.urls import path

from rest1.views import product_list, product_detail, create_product, delete_product, update_product

urlpatterns = [
    path('products/', product_list),
    path('products/<int:pk>/', product_detail),
    path('products/create/', create_product),
    path('products/<int:pk>/delete/', delete_product),
    path('products/<int:pk>/update/', update_product),
]
