from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import *
import requests
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
            headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
            response = requests.put(
	            'https://192.168.1.51:9090/mapi/tenants?username=finance&password=aSfR3q13&forcePasswordChange=false',
	            json= serializer.data,
	            headers=headers,
	            verify=False)
            if response.status_code != 200:
                return Response(response.headers, status=response.status_code)
            else:
                return Response(response.headers, status=status.HTTP_200_OK)
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