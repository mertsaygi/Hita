# -*- coding: utf-8 -*-
from datetime import *
from django.shortcuts import render_to_response
from django.middleware import csrf
from django.http import *
from forms import *
import json
from management.models import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from hita.decorator import active_and_login_required

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
    csrf_token = get_or_create_csrf_token(request)
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/spaces/')
            else:
                auth_login(request, user)
                return HttpResponseRedirect('/spaces/')
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
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/spaces/')
                else:
                    auth_login(request, user)
                    return HttpResponseRedirect('/spaces/')
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
                error_code = 800  # Auth Error
                return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm()
    return render_to_response('register.html',locals())

def forgot(request):
    csrf_token = get_or_create_csrf_token(request)
    if request.method == 'POST':
        email = request.POST.get('email')
        # Send email with activation key
        hash = "1234"
        email_subject = 'Account confirmation'
        if settings.ENVIRONMENT == "DEVELOPMENT":
            email_body = "http://127.0.0.1:8000/forgot/"+hash+"?page=2"
        else:
            email_body = "Bar"
        send_mail(email_subject, email_body, 'myemail@example.com',[email], fail_silently=False)
    return render_to_response('forgot.html',locals())

@login_required(login_url='/login/')
def payment(request):
    area_code = AREA_CODE
    error_code = request.GET.get('c')
    data = open(settings.STATIC_URL+ "/staticdata/countries.json").read()
    data = json.loads(data)
    return render_to_response('payment.html',locals())

@login_required(login_url='/login/')
def spaces(request):
    area_code = AREA_CODE
    csrf_token = get_or_create_csrf_token(request)
    user_spaces = UserSpaces.objects.filter(user=request.user)
    return render_to_response('spaces.html',locals())

@active_and_login_required
def create(request):
    area_code = AREA_CODE
    csrf_token = get_or_create_csrf_token(request)
    try:
        hitatoken = UserProfile.objects.filter(user=request.user).token_string
    except:
        print "No Token"
    return render_to_response('create.html',locals())

@active_and_login_required
def create_namespace(request):
    area_code = AREA_CODE
    csrf_token = get_or_create_csrf_token(request)
    nspace_container = request.GET["container"]
    return render_to_response('create_namespace.html',locals())

@login_required(login_url='/login/')
def account(request):
    area_code = AREA_CODE
    return render_to_response('account.html',locals())

@login_required(login_url='/login/')
def billing(request):
    area_code = AREA_CODE
    return render_to_response('billing.html',locals())

@login_required(login_url='/login/')
def user_settings(request):
    area_code = AREA_CODE
    return render_to_response('settings.html',locals())

def resources(request):
    return HttpResponse("resources")