from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def emp_register(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_email=request.POST.get("emp_email")
        emp_password=request.POST.get("emp_password")
        phone=request.POST.get("phone")
        position=request.POST.get("position")
        data=emp_details(emp_name=emp_name,emp_email=emp_email,emp_password=emp_password,phone=phone,position=position)
        data.save()
    return render(request,'emp_reg.html') 

def emp_profile(request):
    emp_id=request.session['empid']
    data=emp_details.objects.get(pk=emp_id)
    return render(request,'emp_profile.html',{"result":data})

def e_update(request,id):
    data=emp_details.objects.get(pk=id)
    return render(request,'emp_proupdate.html',{'result1':data})
def emp_update(request,id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_email=request.POST.get("emp_email")
        emp_password=request.POST.get("emp_password")
        phone=request.POST.get("phone")
        position=request.POST.get("position")
        data=emp_details(id=id,emp_name=emp_name,emp_email=emp_email,emp_password=emp_password,phone=phone,position=position)
        data.save()
        
        return redirect(emp_profile)
    return render(request,'emp_proupdate.html')


