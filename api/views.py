# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from django.http import *
import requests
from serializers import *

def main(request):
    return HttpResponseRedirect('docs/')

@api_view(['GET'])
def get_spaces(request):
    return HttpResponseRedirect('docs/')

#TODO: Login crediantals must be ok
@api_view(['GET'])
def get_tenants(request):
    if request.method == 'GET':
        #TODO: Tenant user matching
        #TODO: Response type not be xml
        headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
        response = requests.get(
	        'https://31.145.7.26:9090/mapi/tenants?username=finance&password=aSfR3q13&forcePasswordChange=false',
	        headers=headers,
	        verify=False)
        if response.status_code != 200:
            return Response(response.headers, status=response.status_code)
        else:
            return Response(response, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def create_tenant(request):
    if request.method == 'POST':
        serializer = TenantCreateSerializer(data=request.data)
        print request.data
        if serializer.is_valid():
            #TODO: Tenant user matching
            headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
            response = requests.put(
	            'https://31.145.7.26:9090/mapi/tenants?username=finance&password=aSfR3q13&forcePasswordChange=false',
	            json= serializer.data,
	            headers=headers,
	            verify=False)
            if response.status_code != 200:
                return Response(response.headers, status=response.status_code)
            else:
                tenant = UserSpaces(user=request.user, space_url=request.data["name"] + ".mertsaygi.khas.edu.tr",
                                    space_type=2)
                tenant.save()
                #FIXME: Bu DNS kullanmaya başlayınca kalkacak!
                os.system('echo "31.145.7.26 '+request.data["name"] + '.mertsaygi.khas.edu.tr /etc/hosts" >> /etc/hosts')
                return Response(response.headers, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def delete_tenant(request,pk):
    if request.method == 'GET':
        tenant_object = UserSpaces.objects.get(pk=pk)
        if tenant_object.count() > 0:
            headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
            response = requests.delete(
	            'https://31.145.7.26:9090/mapi/tenants/finance?username=finance&password=aSfR3q13&forcePasswordChange=false',
	            headers=headers,
	            verify=False)
            if response.status_code != 200:
                return Response(response.headers, status=response.status_code)
            else:
                return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_namespaces(request):
    if request.method == 'GET':
        #TODO: Tenant user matching
        #TODO: Response type not be xml
        headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
        response = requests.get(
	        'https://31.145.7.26:9090/mapi/tenants/rooooot/namespaces?username=finance&password=aSfR3q13',
	        headers=headers,
	        verify=False)
        print response.headers
        print response
        if response.status_code != 200:
            return Response(response.headers, status=response.status_code)
        else:
            return Response(response, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def create_namespace(request):
    if request.method == 'POST':
        serializer = NamespaceCreateSerializer(data=request.data)
        if serializer.is_valid():
            #TODO: Namespace user matching
            headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
            response = requests.put(
	            'https://31.145.7.26:9090/mapi/tenants/finance/namespaces?username=finance&password=aSfR3q13&forcePasswordChange=false',
	            json= serializer.data,
	            headers=headers,
	            verify=False)
            if response.status_code != 200:
                return Response(response.headers, status=response.status_code)
            else:
                #TODO: Tenant name ekle
                namespace = UserSpaces(user=request.user, space_url=request.data["name"] + ".tenant.mertsaygi.khas.edu.tr",
                                    space_type=2)
                namespace.save()
                return Response(response.headers, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)