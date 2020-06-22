from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def admin_login(request):
    return render(request,"bgtrans/admin_login.html")


def Admin_logincheck(request):
    if request.POST.get("admin_username")=="9981634163" and request.POST.get("admin_password")=="vicky123":
        return render(request,"bgtrans/admin_welcome.html")
    else:
        return render(request,"bgtrans/admin_login.html",{"m":"Invalid_username_or_password"})

