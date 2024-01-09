from django.urls import path
from .views import ProductDetailView , ProductListView
from .views import product_list,product_details,manufacturer_list,manufacturer_details

urlpatterns=[
    path("",ProductListView.as_view(),name="product-list"),
    path("products/<int:pk>/",ProductDetailView.as_view(),name="product-detail"),
    path("products/",product_list,name="product-list"),
    path("products/<int:pk>/",product_details,name="product-detail"),
    path("manufacturers/",manufacturer_list,name="manufacturer-list"),
    path("manufacturers/<int:pk>/",manufacturer_details,name="manufacturer_details"),
]