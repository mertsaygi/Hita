# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from django.http import *
import requests
from django.conf import settings
from serializers import *
import hashlib
import base64
import pycurl
import StringIO
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def getTokenString():
    encoded_data = base64.b64encode(settings.MASTER_USER)
    hash_object = hashlib.md5(settings.MASTER_PASS)
    return encoded_data+":"+hash_object.hexdigest()

def main(request):
    return HttpResponseRedirect('docs/')

@api_view(['POST'])
def upload_file(request,pk):
    uploaded_file = request.FILES['file']
    token = "hcp-ns-auth="+getTokenString()
    CLUSTER = "https://test.mertmain.mertsaygi.khas.edu.tr/rest/"
    FN = str(uploaded_file.name)
    path = default_storage.save('tmp/'+uploaded_file.name, ContentFile(uploaded_file.read()))
    path = os.path.join(settings.MEDIA_ROOT, path)
    cin = StringIO.StringIO()
    filehandle = open(path, 'r')
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, CLUSTER + FN)
    curl.setopt(pycurl.COOKIE, token)
    curl.setopt(pycurl.SSL_VERIFYPEER, 0)
    curl.setopt(pycurl.SSL_VERIFYHOST, 0)
    curl.setopt(pycurl.UPLOAD, 1)
    curl.setopt(pycurl.INFILESIZE, os.path.getsize(path))
    curl.setopt(pycurl.READFUNCTION, filehandle.read)
    curl.setopt(pycurl.HEADER, 1)
    curl.setopt(pycurl.NOBODY, 0)
    curl.setopt(pycurl.WRITEFUNCTION, cin.write)
    curl.perform()
    return Response(cin.getvalue(), status=curl.getinfo(pycurl.HTTP_CODE))

@api_view(['GET'])
def get_files(request,pk):
    tenant_object = UserSubspaces.objects.get(pk=pk)
    CLUSTER = tenant_object.space_url.lower()+"/rest/"
    headers = {'content-type': 'application/xml','accept': 'application/xml','Authorization': 'HCP '+getTokenString()}
    response = requests.get(CLUSTER,headers=headers, verify=False)
    #TODO: XML to JSON
    print ET.fromstring(response.text)
    return Response("", status=response.status_code, content_type="application/xml")


@api_view(['POST'])
def create_tenant(request):
    if request.method == 'POST':
        serializer = TenantCreateSerializer(data=request.data)
        if serializer.is_valid():
            #TODO: Tenant user matching
            headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
            response = requests.put(
	            'https://31.145.7.26:9090/mapi/tenants?username='+settings.MASTER_USER+'&password='+settings.MASTER_PASS+'&forcePasswordChange=false',
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
                os.system('echo "31.145.7.26 '+request.data["name"] + '.mertsaygi.khas.edu.tr" >> /etc/hosts')
                return Response(response.headers, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def delete_tenant(request,pk):
    if request.method == 'GET':
        tenant_object = UserSpaces.objects.get(pk=pk)
        try:
            user_profile = UserProfile.objects.get(user=tenant_object.user)
            headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
            response = requests.delete(
	            'https://31.145.7.26:9090/mapi/tenants/'+tenant_object.space_url.replace(".mertsaygi.khas.edu.tr", "")+'?username='+settings.MASTER_USER+'&password='+settings.MASTER_PASS+'&forcePasswordChange=false',
	            headers=headers,
	            verify=False)
            if response.status_code != 200:
                return Response(response.headers, status=response.status_code)
            else:
                tenant_object.delete()
                return Response(response, status=status.HTTP_200_OK)
        except:
            return Response("Object not found.", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def create_single_namespace(request,pk):
    if request.method == 'POST':
        tenant_object = UserSpaces.objects.get(pk=pk)
        try:
            serializer = NamespaceCreateSerializer(data=request.data)
            if serializer.is_valid():
                #TODO: Namespace user matching
                headers = {'content-type': 'application/json','Authorization': 'HCP '+getTokenString()}
                response = requests.put(
	                'https://31.145.7.26:9090/mapi/tenants/'+tenant_object.space_url.replace(".mertsaygi.khas.edu.tr", "")+'/namespaces?username='+settings.MASTER_USER+'&password='+settings.MASTER_PASS+'&forcePasswordChange=false',
	                json= serializer.data,
	                headers=headers,
	                verify=False)
                if response.status_code != 200:
                    return Response(response.headers, status=response.status_code)
                else:
                    #TODO: Tenant name ekle
                    namespace = UserSpaces(user=request.user, space_url=request.data["name"] + ".tenant.mertsaygi.khas.edu.tr",
                                    space_type=1)
                    namespace.save()
                    return Response(response.headers, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as inst:
            return Response(inst.args, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def create_namespace(request,pk):
    if request.method == 'POST':
        tenant_object = UserSpaces.objects.get(pk=pk)
        try:
            serializer = NamespaceCreateSerializer(data=request.data)
            if serializer.is_valid():
                #TODO: Namespace user matching
                headers = {'content-type': 'application/json','Authorization': 'HCP '+getTokenString()}
                print 'https://'+tenant_object.space_url+':9090/mapi/tenants/'+tenant_object.space_url.replace(".mertsaygi.khas.edu.tr", "")+'/namespaces'
                response = requests.put(
	                'https://'+tenant_object.space_url+':9090/mapi/tenants/'+tenant_object.space_url.replace(".mertsaygi.khas.edu.tr", "")+'/namespaces',
	                json= serializer.data,
	                headers=headers,
	                verify=False)
                if response.status_code != 200:
                    return Response(response.headers, status=response.status_code)
                else:
                    #TODO: Tenant name ekle
                    namespace = UserSpaces(user=request.user, space_url=request.data["name"] + ".tenant.mertsaygi.khas.edu.tr",
                                    space_type=1)
                    namespace.save()
                    return Response(response.headers, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as inst:
            return Response(inst.args, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)