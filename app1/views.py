from django.shortcuts import render,redirect
from .models import *
from cafe .models import userdetails
from appemp.models import emp_details
from appuser.models import food_order

# Create your views here.
def add_menu(request):
    if request.method=="POST":
       dish_name=request.POST.get("dish_name")
       price=request.POST.get("price")
       dish_img=request.FILES["dish_img"]
       data=menu(dish_name=dish_name,price=price,dish_img=dish_img)
       data.save()
    return render(request,'add_dish.html')

def view_user(request):
    data=userdetails.objects.all()
    return render (request,'admin_user.html',{"result":data})

def userdelete(request,id):
    mark=userdetails.objects.get(pk=id)
    mark.delete()
    return redirect(view_user)
def view_menu(request):
    data=menu.objects.all()
    return render(request,'view_menu.html',{"result":data})

def view_emp(request):
    data=emp_details.objects.all()
    return render (request,'ad_empview.html',{"result":data})

def empdelete(request,id):
    ma=emp_details.objects.get(pk=id)
    ma.delete()
    return redirect(view_emp)

def view_order(request):
    data=food_order.objects.all()
    return render (request,'view_myorder.html',{'result':data})


