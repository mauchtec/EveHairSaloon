from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    

    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('products_list', views.products_list, name='products-list'),
    path('add_product', views.add_product, name='add_product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
