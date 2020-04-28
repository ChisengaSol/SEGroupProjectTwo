from django.shortcuts import render, redirect
from .models import Menu, Orders
from django.db.models import F
from django.contrib.auth.decorators import login_required

from decimal import Decimal

from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login, 
    logout
)
from .forms import UserLoginForm
from django.contrib import messages
# UserRegisterForm


# Create your views here.
def menuform(request):
    objects  = Menu.objects.all()
    return render(request, 'restaurant_system/menu.html', {"meals":objects })


def post_menu(request):
    return render(request, 'restaurant_system/menu.html')

# @login_required
def getMenu(request):
    meals = Menu.objects.all()
    user = request.user
    return render(request,'restaurant_system/menu.html',{'meals': meals, 'user': user})

def Orderform(request):

    if request.POST:

        menu_id = request.POST.get("meal_id")
        # user_id = request.POST.get("user_id")

        meal = Menu.objects.filter(id = menu_id)
        meal_obj = meal[0]
        meal_order = Orders.objects.filter(user=request.user).filter(menu= meal_obj)
        if not meal_order :
            meal_order = Orders(user=request.user)
            meal_order.save()
            meal_order.menu.add(meal_obj)
            messages.success(request, 'successfully added')
            return redirect('/')
        else:
            meal_order = Orders.objects.filter(user = request.user)
            messages.warning(request, 'already exist in your order please proceed to check out!')
            return redirect('/')
            # return render(request,'restaurant_system/order.html', {"meals":meal_order, "failed": True})

        
        
        # meal_order.save()
            
    else:
        meal_order = Orders.objects.filter(user = request.user)
        return render(request,'restaurant_system/order.html', {"meals":meal_order})

def addOrder(req, id):
    if request.POST:
        menu_id = request.POST.get("meal_id")
        # user_id = request.POST.get("user_id")

        meal = Menu.objects.filter(id = menu_id)
        meal_obj = meal[0]
        meal_order = Orders.objects.filter(user=request.user).filter(menu= meal_obj)

        meal_order = Orders(user=request.user)
        meal_order.save()
        meal_order.menu.add(meal_obj)
        messages.success(request, 'successfully added')
        return redirect(request.path_info)




def getOrders(request):
    
    return render(request, 'restaurant_system/orders.html', {"orders": meal_order})

def getBill(request):
    order = {}
    total = 0
    for obj in Orders.objects.all():
        for meal in obj.menu.all():
            order[meal.meal_name] =meal.meal_price
    
    for k,v in order.items():
        total += v

    return render(request,'restaurant_system/bill.html',{'orderlist':order,'total':total})


def makeMoreOrders(request):
    if request.POST:

        menu_name = request.POST["mealname"]
        menu_id = request.POST["mealid"]
        if Orders.objects.filter(id=menu_id).exists():
            Orders.objects.filter(id=menu_id).update(qty=F('qty') +1)
        return render(request,'restaurant_system/order.html')       
            
    else:
        return render(request,'restaurant_system/order.html')

            
    