from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from app import models
from .models import UserDetails

def Register(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname= request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        #validation
        error_message = None 
        if not firstname :
            error_message = "firstname is required !!"
        if not lastname :
            error_message = "lastname is required !!"
        if not email:
            error_message = "email is required !!"
        if not password:
            error_message = "password is required !!"

        if not error_message:
            user = UserDetails(firstname=firstname,lastname=lastname,email=email,password=password)
            user.password = make_password(user.password)
            user.save()
            return redirect('login')
        else:
            return render(request,'register.html',{"error":error_message})
    return render(request,'register.html')

def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password= request.POST['password']


        user = UserDetails.get_user_email(email)
        error_message = None 
        if user:
            flag = check_password(password,user.password)
            if flag:
                request.session['user'] = user.id
                return redirect('base')
            else:
                error_message = "email or passsword invalid"
        else:
            return render(request,'login.html',{'error':error_message})

    return render(request,'login.html')

def Logout(request):
    request.session.clear()
    return redirect('register')

def base(request):
    return render(request,'base.html')


