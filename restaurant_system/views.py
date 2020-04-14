from django.shortcuts import render
from .models import Menu
# Create your views here.
def menuform(request):
    meals = Menu.objects.all()
    return render(request,'restaurant_system/menu.html',{'meals': meals})

def Orderform(request):
    return render(request,'restaurant_system/order.html')
