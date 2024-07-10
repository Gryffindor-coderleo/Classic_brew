from django.shortcuts import render,redirect
from cafe.models import userdetails
from app1.models import menu
from .models import *

# Create your views here.

def user_profile(request):
    u_id = request.session['uid']
    user = userdetails.objects.get(pk=u_id)
    return render(request, 'user_profile.html', {'result': user})

def u_update(request,id):
    data=userdetails.objects.get(pk=id)
    return render(request,'user_update.html',{'result1':data})
def user_update(request,id):
    if request.method=="POST":
        username=request.POST.get("username")
        useremail=request.POST.get("useremail")
        userpassword=request.POST.get("userpassword")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        data=userdetails(username=username,useremail=useremail,userpassword=userpassword,phone=phone,address=address,id=id)
        data.save()
        return redirect(user_profile)
    return render(request,'user_update.html')


def order(request, id):
    data = menu.objects.get(pk=id)
    return render(request, 'order.html', {'result': data})

def orders(request):
    if request.method == "POST":
        u_id = request.session.get('uid')
        or_img = request.POST.get("or_img")
        or_name = request.POST.get("or_name")
        or_price = request.POST.get("or_price")
        or_adrs = request.POST.get("or_adrs")
        or_ph = request.POST.get("or_ph")
        data = food_order(u_id=u_id, or_img=or_img, or_name=or_name, or_price=or_price, or_adrs=or_adrs, or_ph=or_ph)
        data.save()
        return redirect(make_order)
    data = menu.objects.all()
    return render(request, 'order.html', {'result': data})
    

def make_order(request):
   data=menu.objects.all()
   return render(request,'user_order.html',{'result':data})


def view_myorder(request):
    u_id=request.session['uid']
    data=food_order.objects.filter(u_id=u_id)
    return render (request,'view_myorder.html',{'result':data})

def orderdelete(request,id):
    ma=food_order.objects.get(pk=id)
    ma.delete()
    return redirect(view_myorder)


