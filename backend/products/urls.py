from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-list-create')
]