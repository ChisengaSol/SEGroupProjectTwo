from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.getMenu),
    path('orders/', views.Orderform),
    path('post_menu/', views.post_menu)
]

