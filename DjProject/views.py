from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from DjProject.forms import Usregis,Upd
from DjangoProject import settings 
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import models
from django.views.decorators.http import require_POST
from DjProject.models import Exfd
from DjProject.forms import Pad,Upd


# Create your views here.


from django.http import JsonResponse

# Create your views here.

def store(request):
  return render(request,'html/store.html')

def home(request):
  return render(request,'html/home.html')

@login_required
def prfle(request):
  return render(request,'html/profile.html')

@login_required
def updf(request):
  if request.method == "POST":
    p=Upd(request.POST,instance=request.user)
    t=Pad(request.POST,request.FILES,instance=request.user.exfd) 
    if p.is_valid() and t.is_valid():
      p.save()
      t.save()
      messages.success(request,"{} your profile updated successfully".format(request.user.username))
      return redirect('/pf')
  p = Upd(instance=request.user)
  t = Pad(instance=request.user.exfd)
  return render(request,'html/updateprofile.html',{'r':p,'q':t})

def about(request):
  return render(request,'html/about.html')

def register(request):
  if request.method == "POST":
    y = Usregis(request.POST)
    if y.is_valid():
      p = y.save(commit=False)
      rc =p.email
      # print(rc)
      sb = "Testing Email to register for WorkLog Project"
      mg = "Hi Welcome {} you have been successfully registered in our portal with password: {}".format(p.username,p.password)
      sd = settings.EMAIL_HOST_USER
      snt = send_mail(sb,mg,sd,[rc])
      if snt == 1:
        p.save()
        messages.success(request,"Please check your {} for login credentials".format(rc))
        return redirect('/lg')
      messages.danger(request,"please enter correct emailid or username or password")
      # print(p.username,p.email) to know the username and emailid
  y = Usregis()
  return render(request,'html/register.html',{'t':y})


def lg(request):
  if request.method == "POST":
    uname = request.POST['username']
    pwd = request.POST['password']
    user = auth.authenticate(username=uname,password=pwd)
    if user is not None: 
      auth.login(request,user)
      return redirect('profile')
    else:
      return render(request,'login.html',{'error': "Invalid Login credentials."})
  else:
    return render(request,'login.html',{})


def profile(request):
  return render(request,'html/profile.html')

@login_required
def updf(request):
  if request.method == "POST":
    p=Upd(request.POST,instance=request.user)
    t=Pad(request.POST,request.FILES,instance=request.user.exfd) 
    if p.is_valid() and t.is_valid():
      p.save()
      t.save()
      messages.success(request,"{} your profile updated successfully".format(request.user.username))
      return redirect('/pf')
  p = Upd(instance=request.user)
  t = Pad(instance=request.user.exfd)
  return render(request,'html/updateprofile.html',{'r':p,'q':t}) 