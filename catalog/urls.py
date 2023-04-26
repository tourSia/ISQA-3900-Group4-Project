from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('category_detail/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
]
