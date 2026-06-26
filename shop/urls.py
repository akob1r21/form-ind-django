from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('create-product/', views.product_create, name='products-create'),
    path('update-product/<int:pk>/', views.update_product, name='update_products'),
    path('create-category', views.create_category, name='create_category'),

]
