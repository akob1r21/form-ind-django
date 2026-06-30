from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('create-product/', views.product_create, name='products-create'),
    path('update-product/<int:pk>/', views.update_product, name='update_products'),
    path('create-category', views.create_category, name='create_category'),
    path('p-list', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='detail_product'),
    path('product-create/', views.ProductCreateView.as_view(), name='create_product'),
    path('product-update/<slug:slug>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('product-delete/<slug:slug>/', views.ProductDeleteView.as_view(), name='delete_product'),

]
