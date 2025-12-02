from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_List),
    path('products/<int:id>/', views.product_Detail),
    path('products/add/', views.add_Product),
    path('api', include('shop.urls')),
]