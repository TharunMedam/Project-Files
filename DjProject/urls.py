from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from DjProject import views
from django.contrib.auth import views as g


urlpatterns = [
	path('',views.home,name="hm"),
	path('sto/',views.store,name="st"),
	path('abt/',views.about,name="ab"),
	path('pf/',views.profile,name="pfe"),
    path('upf/',views.updf,name="upfe"),
	path('rg/', views.register, name="reg"),
	path('lg/',g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
	path('lgg/',g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]