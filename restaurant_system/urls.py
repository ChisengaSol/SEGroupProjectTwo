from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.getMenu),
    path('orders/', views.Orderform),
<<<<<<< HEAD
    path('bill/',views.getBill),
    path('post_menu/', views.post_menu),
    #path('or/', views.getBill)
=======
    path('post_menu/', views.post_menu)
>>>>>>> 0b15ddb706505c912b47b7b9263961612c8d20bf
]

