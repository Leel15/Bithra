from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('store/', views.store, name='store'),
    path('seed/<int:seed_id>/', views.seed_detail, name='seed_detail'),
    path('calendar/', views.planting_calendar, name='calendar'), 
    path('add-to-cart/<int:seed_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
]