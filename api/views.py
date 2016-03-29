from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import *
import time
from datetime import datetime, timedelta
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets

def main(request):
    return HttpResponseRedirect('docs/')

def get_spaces(request):
    return HttpResponseRedirect('docs/')

def get_tenants(request):
    return HttpResponseRedirect('docs/')

def create_tenant(request):
    return HttpResponseRedirect('docs/')

def get_namespaces(request):
    return HttpResponseRedirect('docs/')

def create_namespace(request):
    return HttpResponseRedirect('docs/')