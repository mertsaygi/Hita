# -*- coding: utf-8 -*-
from datetime import *
from django.shortcuts import render_to_response
from django.middleware import csrf
from django.http import *
from forms import *
from management.models import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

AREA_CODE = 0 # 0 space , 1 namespace , 2 tenant

def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token

def main(request):
    return render_to_response('index.html',locals())

def login(request):
    user = authenticate(username='caferbezgetiren', password='caferbezgetiren')
    if user is not None:
        # the password verified for the user
        if user.is_active:
            auth_login(request, user)
        else:
            print("The password is valid, but the account has been disabled!")
            error_code = 900 # Not Paid User
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        error_code = 800 # Auth Error
    return render_to_response('login.html',locals())

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

def register(request):
    csrf_token = get_or_create_csrf_token(request)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render_to_response('register.html',locals())

@login_required(login_url='/login/')
def payment(request):
    return render_to_response('payment.html',locals())

@login_required(login_url='/login/')
def spaces(request):
    area_code = AREA_CODE
    user_spaces = UserSpaces.objects.filter(user=request.user)
    return render_to_response('spaces.html',locals())

def account(request):
    area_code = AREA_CODE
    return HttpResponse("account")

def billing(request):
    area_code = AREA_CODE
    return HttpResponse("billing")

def user_settings(request):
    area_code = AREA_CODE
    return HttpResponse("user_settings")

def support(request):
    return HttpResponse("support")

def docs(request):
    return HttpResponse("docs")

def training(request):
    return HttpResponse("training")

def resources(request):
    return HttpResponse("resources")