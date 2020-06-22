from django.shortcuts import render,redirect
from customer.models import CustomerLogin
# Create your views here.
def Customer_Home(request):
    return render(request,"customer/home.html")


def Registercustomer(request):
    return render(request,"customer/register.html")


def SAvecustomer(request):
    usr=request.POST.get("username")
    psw=request.POST.get("password")
    c=CustomerLogin(username=usr,password=psw)
    c.save()
    return render(request,"customer/register.html",{"message":"Now_you_are_register_with_B.G_company"})


def LoginCheck(request):
    user1=request.POST.get("username1")
    pass1=request.POST.get("password1")
    try:
        CustomerLogin.objects.get(username=user1,password=pass1)
        return render(request,"customer/welcome.html")

    except:
        return render(request,"customer/home.html",{"message":"Invalid_username_or_password"})


def Home(request):
    return render(request,"customer/welcome.html")


def AboutUs(request):
    return render(request,"customer/about.html")


def Service(request):
    return render(request,"customer/service.html")


def Career(request):
    return render(request, "customer/career.html")


def Conatactus(request):
    return render(request, "customer/contact.html")

