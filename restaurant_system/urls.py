from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.menuform),
    path('order/', views.Orderform),
    path('post_menu/', views.post_menu),
    path('login/', views.login_view),
    path('signup/', views.register_view),
    path('logout/', views.logout_view)
]
