from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('category_detail/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

