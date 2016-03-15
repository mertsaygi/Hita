# -*- coding: utf-8 -*-
from datetime import *
from django.shortcuts import render_to_response
from django.http import *

def main(request):
    return render_to_response('index.html',locals())

def login(request):
    return render_to_response('login.html',locals())

def register(request):
    return render_to_response('register.html',locals())