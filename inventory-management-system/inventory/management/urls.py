from django.urls import path
from .views import home_view,create_product,get_products,update_product,delete_product

urlpatterns = [
    path('',home_view,name="home"),
    path('create/',create_product,name='product_form'),
    path('list/',get_products,name="product_list"),
    path("update/<int:product_id>/",update_product,name="product_update"),
    path("delete/<int:product_id>/",delete_product,name="delete_product")
]