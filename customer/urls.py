"""BG_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Customer_Home,name="home"),
    path('register/',views.Registercustomer,name="register"),
    path('save/',views.SAvecustomer,name="save"),
    path('logincheck/',views.LoginCheck,name="logincheck"),
    path('home/',views.Home,name="home"),
    path('about_us/',views.AboutUs,name="about_us"),
    path('service/',views.Service,name="service"),
    path('career/',views.Career,name="career"),
    path('contact_us/',views.Conatactus,name="contact_us")
]
