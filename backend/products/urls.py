from django.urls import path
from . import views

# View per action
urlpatterns = [
    path('', views.product_list_create_view, name='product-list-create'),
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view, name='product-detail')
]


#Using just two Views
# urlpatterns = [
#     path('', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
#     path('<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-add-update-delete-retrive')
# ]