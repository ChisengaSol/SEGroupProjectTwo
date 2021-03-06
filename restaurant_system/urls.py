from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.getMenu),
    path('orders/', views.Orderform),
    path('bill/',views.getBill),
    path('post_menu/', views.post_menu),
    path('bill/',views.getBill),
    path('payment/', views.pay),
    path('confirmpayment/',views.paymentconfirmation),
    path('more_orders/', views.makeMoreOrders),
    path('adm/orders', views.admin_view_order)
]

