from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services'),
    path('product/<int:myid>', views.product, name='product'),
    path('cart-item', views.cartItem, name='cart-item'),
    path('cart',views.cartPage, name='cart'),
    path('checkout',views.checkout, name='checkout'),
    path('apiviews', views.ProductList.as_view(), name='api')
]
 