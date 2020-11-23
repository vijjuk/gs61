from django.shortcuts import render
from .forms import Signup,EditUserProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from .forms import ImageForm
from .models import Image


# Create your views here.
def SignUp(request):
    if request.method=="POST":
        fm=Signup(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"ho gya jhsvfjgvsb jsbv")
    else:
        fm=Signup()
    return render(request,'html/signup.html',{'form':fm})

def Login(request):
    if not request.user.is_authenticated:

        if request.method=="POST":
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,'WELCOME LOG IS SUCCESSFULLY')
                    return HttpResponseRedirect("/profile/")
        else:
            fm=AuthenticationForm
        return render(request,"html/login.html",{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def User_profile(request):
    if request.user.is_authenticated:
        return render(request,"html/profile.html",{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

def Logout(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'LOG out is done')
    return HttpResponseRedirect('/login/')

def User_change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.add_message(request,messages.SUCCESS," change ho gya jhsvfjgvsb jsbv")
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'html/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def User_edit(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=EditUserProfile(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.add_message(request,messages.SUCCESS,"uPDATE IS OK")
        else:
            fm=EditUserProfile(instance=request.user)
        return render(request,'html/user_change_form.html',{'form':fm})
    else:
        HttpResponseRedirect('/login/')

def Images(request):
    if request.method == "POST":
        fm=ImageForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'File is uploded')
            fm=ImageForm()
            img=Image.objects.all()
            return render(request,'html/image.html',{'img':img,"form":fm})
    fm=ImageForm()
    img=Image.objects.all()
    return render(request,'html/image.html',{'img':img,"form":fm})

def show_all_img(request):
    img=Image.objects.all()
    return render(request,'html/Home.html',{'img':img})

def about(request):
    return render(request,'html/about.html')