from django.shortcuts import render, redirect
from .models import Menu
from django.contrib.auth.decorators import login_required


from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login, 
    logout
)
from .forms import UserLoginForm
# UserRegisterForm


# Create your views here.
def menuform(request):
    objects  = Menu.objects.all()
    return render(request, 'restaurant_system/menu.html', {"meals":objects })


def post_menu(request):

    return render(request, 'restaurant_system/menu.html')


def getMenu(request):
    return render(request, 'restaurant_system/')
    meals = Menu.objects.all()
    return render(request,'restaurant_system/menu.html',{'meals': meals})

def Orderform(request):
    return render(request,'restaurant_system/order.html')


def login_view(request):
    next = request.GET.get('next')
    form  = UserLoginForm(request.POST or None)
    # import pdb; pdb.set_trace()
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('/restaurant/login')
        login(request, user)


        if next:
            return redirect(next)
        return redirect('/restaurant')
    
    context = {
        "form": form
    }
    return render(request, "login.html", context)



def register_view(request):
    next = request.GET.get('next')
    form  = UserRegisterForm(request.POST or None)
    # import pdb; pdb.set_trace()
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user =  authenticate(username=username, password=password)
        login(request, user)


        if next:
            return redirect(next)
        return redirect('/restaurant')
    
    context = {
        "form": form
    }
    return render(request, "signup.html", context)

def logout_view(request):
    logout(request)
    return redirect('/restaurant')
