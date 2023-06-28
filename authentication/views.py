from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserAccount
from django.conf import settings


def login_view(request):

    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    if request.method == "POST":
        client = request.tenant
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email:
            return HttpResponse("Please enter your email address")
        if not password:
            return HttpResponse("Password is required")

        user : UserAccount = authenticate(request, email=email, password=password)

        if not user:
            return HttpResponse("Invalid Credentials")
        if not user.is_active:
            return HttpResponse("User is inactive")
        
        if client.is_active:
            login(request, user)

            next_url = request.GET.get('next')

            if next_url:
                return redirect(next_url)
            else:
                return redirect("/")
    return render(request, "login.html")


def logout_view(request):

    logout(request)

    return redirect(settings.LOGIN_URL)