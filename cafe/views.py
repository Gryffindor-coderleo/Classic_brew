from django.shortcuts import render,redirect
from . models import *
from appemp.models import emp_details



def index(request):
    return render(request,'index.html')
def user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        useremail=request.POST.get("useremail")
        userpassword=request.POST.get("userpassword")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        data=userdetails(username=username,useremail=useremail,userpassword=userpassword,phone=phone,address=address)
        data.save()
    return render(request,'user.html')    


    
def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email == 'admin@gmail.com' and password == 'admin':
        request.session['adminemail'] = email
        request.session['admin'] = 'admin'
        return render(request, 'index.html', {'status': 'admin login successful'})
    
    elif userdetails.objects.filter(useremail=email, userpassword=password).exists():
        udet = userdetails.objects.get(useremail=email, userpassword=password)
        request.session['uid'] = udet.id
        request.session['uname'] = udet.username
        request.session['uemail'] = udet.useremail
        request.session['user'] = 'user'
        return render(request, 'index.html', {'status': 'user login successful'})
    
    elif emp_details.objects.filter(emp_email=email, emp_password=password).exists():
        emp = emp_details.objects.get(emp_email=email, emp_password=password)
        request.session['empid'] = emp.id
        request.session['empname'] = emp.emp_name
        request.session['empemail'] = emp.emp_email
        request.session['employee'] = 'employee'
        return render(request, 'index.html', {'status': 'employee login successful'})
    
    else:
        return render(request, 'login.html', {'status': 'incorrect credentials'})

        
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
     del request.session[key]
    return redirect(index)