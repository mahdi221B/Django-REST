from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_random_product),
    path('add/', views.add_product)
]