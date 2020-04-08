from django.shortcuts import render

# Create your views here.
def menuform(request):
    return render(request,'restaurant_system/menu.html')
