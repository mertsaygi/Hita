from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.http import *
import time,os
from datetime import datetime, timedelta
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from serializers import *

def main(request):
    return HttpResponseRedirect('docs/')

@api_view(['GET'])
def get_spaces(request):
    return HttpResponseRedirect('docs/')

@api_view(['GET'])
def get_tenants(request):
    return HttpResponseRedirect('docs/')

@api_view(['POST'])
def create_tenant(request):
    if request.method == 'POST':
        serializer = TenantCreateSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_namespaces(request):
    return HttpResponseRedirect('docs/')

@api_view(['POST'])
def create_namespace(request):
    if request.method == 'POST':
        serializer = NamespaceCreateSerializer(data=request.data)
        if serializer.is_valid():
            print serializer.data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)