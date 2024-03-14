from django.urls import path
from .views import CategoryListCreateView, ProductListCreateView, UserListCreateView, OrderListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]

