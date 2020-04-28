from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.getMenu),
    path('orders/', views.Orderform),
    path('bill/',views.getBill),
    path('post_menu/', views.post_menu),
    path('post_menu/', views.post_menu),
    #path('orders/',views.makeMoreOrders)
]

