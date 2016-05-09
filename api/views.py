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
from api import xmltodict
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def get_pretty_url(url):
    if "http://" in url:
        url = url.replace("http://", "https://")
    elif "https://" not in url:
        url = "https://" + url
    return url

def getTokenString():
    encoded_data = base64.b64encode(settings.MASTER_USER)
    hash_object = hashlib.md5(settings.MASTER_PASS)
    return encoded_data+":"+hash_object.hexdigest()

def main(request):
    return HttpResponseRedirect('docs/')

# File Area

@api_view(['GET'])
def get_file(request,pk,file):
    tenant_object = UserSubspaces.objects.get(pk=pk)
    token = "hcp-ns-auth="+getTokenString()
    CLUSTER = tenant_object.space_url+"/rest/"+file
    f = open('/tmp/'+file, 'wb+')
    cin = StringIO.StringIO()
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, CLUSTER)
    curl.setopt(pycurl.COOKIE, token)
    curl.setopt(pycurl.SSL_VERIFYPEER, 0)
    curl.setopt(pycurl.SSL_VERIFYHOST, 0)
    curl.setopt(pycurl.WRITEFUNCTION, cin.write)
    curl.perform()
    curl.close()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename="%s"' % file
    response.write(cin.getvalue())
    f.close()
    return response

@api_view(['DELETE'])
def delete_files(request):
    try:
        serializer = FileDeleteSerializer(data=request.data)
        if serializer.is_valid():
            tenant_object = UserSubspaces.objects.get(pk=serializer.data['namespace_id'])
            token = "hcp-ns-auth="+getTokenString()
            CLUSTER = tenant_object.space_url+"/rest/"+serializer.data['name']
            cin = StringIO.StringIO()
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, CLUSTER)
            curl.setopt(pycurl.COOKIE, token)
            curl.setopt(pycurl.SSL_VERIFYPEER, 0)
            curl.setopt(pycurl.SSL_VERIFYHOST, 0)
            curl.setopt(pycurl.HEADER, 1)
            curl.setopt(pycurl.WRITEFUNCTION, cin.write)
            curl.setopt(pycurl.CUSTOMREQUEST, "DELETE")
            curl.perform()
            return Response(cin.getvalue(), status=curl.getinfo(pycurl.HTTP_CODE))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as inst:
        print inst
        return Response(inst.args, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def upload_file(request,pk):
    tenant_object = UserSubspaces.objects.get(pk=pk)
    uploaded_file = request.FILES['file']
    token = "hcp-ns-auth="+getTokenString()
    CLUSTER = tenant_object.space_url+"/rest/"
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
    if "https://" not in CLUSTER:
        CLUSTER = "https://"+str(CLUSTER)
    print CLUSTER
    headers = {'content-type': 'application/xml','accept': 'application/xml','Authorization': 'HCP '+getTokenString()}
    response = requests.get(CLUSTER,headers=headers, verify=False)
    if response.status_code != 200:
        return Response(response.headers, status=response.status_code)
    else:
        o = xmltodict.parse(response.text)
        return Response(o, status=response.status_code, content_type="application/json")

# Tenant Area

@api_view(['POST'])
def create_tenant(request):
    if request.method == 'POST':
        serializer = TenantCreateSerializer(data=request.data)
        if serializer.is_valid():
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
                grant_tenant_authentication(tenant)
                return Response(response.headers, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
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

@api_view(['GET'])
def get_tenant_info(request,pk):
    tenant_object = UserSpaces.objects.get(pk=pk)
    CLUSTER = 'https://'+tenant_object.space_url+':9090/mapi/tenants/'+tenant_object.space_url.replace(".mertsaygi.khas.edu.tr", "")
    headers = {'content-type': 'application/xml','accept': 'application/xml','Authorization': 'HCP '+getTokenString()}
    response = requests.get(CLUSTER,headers=headers, verify=False)
    if response.status_code != 200:
        return Response(response.headers, status=response.status_code)
    o = xmltodict.parse(response.text)
    return Response(o, status=response.status_code, content_type="application/json")

# Namespace Area

@api_view(['POST'])
def create_namespace(request,pk):
    if request.method == 'POST':
        tenant_object = UserSpaces.objects.get(pk=pk)
        try:
            serializer = NamespaceCreateSerializer(data=request.data)
            if serializer.is_valid():
                headers = {'content-type': 'application/json','Authorization': 'HCP '+getTokenString()}
                url = tenant_object.space_url+':9090/mapi/tenants/'+tenant_object.space_url.replace(".mertsaygi.khas.edu.tr", "")+'/namespaces'
                url = get_pretty_url(url)
                response = requests.put(url,
	                json= serializer.data,
	                headers=headers,
	                verify=False)
                if response.status_code != 200:
                    return Response(response.headers, status=response.status_code)
                else:
                    namespace = UserSubspaces(parent_space=tenant_object,user=request.user, space_url=request.data["name"] + "."+tenant_object.space_url,
                                    space_type=1,space_name=request.data["name"])
                    namespace.save()
                    os.system('echo "31.145.7.26 '+namespace.space_name + '.'+tenant_object.space_url +'" >> /etc/hosts')
                    grant_namespace_authentication(namespace)
                    return Response(response.headers, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as inst:
            return Response(inst.args, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_namespace(request,pk):
    if request.method == 'GET':
        namespace_object = UserSubspaces.objects.get(pk=pk)
        try:
            user_profile = UserProfile.objects.get(user=namespace_object.user)
            headers = {'content-type': 'application/json','Authorization': 'HCP '+getTokenString()}
            response = requests.delete('',
	            headers=headers,
	            verify=False)
            if response.status_code != 200:
                return Response(response.headers, status=response.status_code)
            else:
                namespace_object.delete()
                return Response(response, status=status.HTTP_200_OK)
        except:
            return Response("Object not found.", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# Tenant or Namespace level authentication methods

def grant_tenant_authentication(tenant_object):
    import json
    json_data = '{"roles" : {"role" : [ "COMPLIANCE", "MONITOR", "SECURITY", "ADMINISTRATOR" ]}}'
    headers = {'content-type': 'application/json', 'Authorization': 'HCP ' + getTokenString()}
    response = requests.post(
        'https://' + tenant_object.space_url + ':9090/mapi/tenants/' + tenant_object.space_url.replace(
            ".mertsaygi.khas.edu.tr", "") + '/userAccounts/'+settings.MASTER_USER,
        json=json.loads(json_data),
        headers=headers,
        verify=False)
    print response.headers
    return response

def grant_namespace_authentication(namespace_object):
    import json
    json_data = '{"namespacePermission":[{"namespaceName" : "'+namespace_object.space_name+'","permissions" : {"permission" : [ "BROWSE", "READ", "SEARCH", "PURGE", "DELETE", "WRITE" ]}}]}'
    headers = {'content-type': 'application/json', 'Authorization': 'HCP ' + getTokenString()}
    url = namespace_object.parent_space.space_url + ':9090/mapi/tenants/' + namespace_object.parent_space.space_name + '/userAccounts/' + settings.MASTER_USER+ "/dataAccessPermissions"
    url = get_pretty_url(url)
    response = requests.post(url,
        json=json.loads(json_data),
        headers=headers,
        verify=False)
    print response.text
    return response

# Single Namespace Creation Area

@api_view(['POST'])
def create_single_namespace(request,pk):
    return Response("", status=status.HTTP_200_OK)

# Folder Area

@api_view(['POST'])
def create_folder(request):
    try:
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            tenant_object = UserSubspaces.objects.get(pk=serializer.data['namespace_id'])
            CLUSTER = tenant_object.space_url.lower()+"/rest/"
            PATH = serializer.data['folder_name']
            FN = ""
            OPT = "?type=directory"
            token = "hcp-ns-auth="+getTokenString()
            cin = StringIO.StringIO()
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, CLUSTER + PATH + FN + OPT)
            curl.setopt(pycurl.COOKIE, token)
            curl.setopt(pycurl.SSL_VERIFYPEER, 0)
            curl.setopt(pycurl.SSL_VERIFYHOST, 0)
            curl.setopt(pycurl.CUSTOMREQUEST, "PUT")
            curl.setopt(pycurl.HEADER, 1)
            curl.setopt(pycurl.NOBODY, 0)
            curl.setopt(pycurl.WRITEFUNCTION, cin.write)
            curl.perform()
            curl.close()
            return Response(cin.getvalue(), status=curl.getinfo(pycurl.HTTP_CODE))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as inst:
        print inst
        return Response(inst.args, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_folder(request,pk):
    try:
        serializer = FolderDeleteSerializer(data=request.data)
        if serializer.is_valid():
            tenant_object = UserSubspaces.objects.get(pk=serializer.data['namespace_id'])
            token = "hcp-ns-auth=" + getTokenString()
            CLUSTER = tenant_object.space_url + "/rest/" + serializer.data['name']
            cin = StringIO.StringIO()
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, CLUSTER)
            curl.setopt(pycurl.COOKIE, token)
            curl.setopt(pycurl.SSL_VERIFYPEER, 0)
            curl.setopt(pycurl.SSL_VERIFYHOST, 0)
            curl.setopt(pycurl.HEADER, 1)
            curl.setopt(pycurl.WRITEFUNCTION, cin.write)
            curl.setopt(pycurl.CUSTOMREQUEST, "DELETE")
            curl.perform()
            return Response(cin.getvalue(), status=curl.getinfo(pycurl.HTTP_CODE))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as inst:
        print inst
        return Response(inst.args, status=status.HTTP_400_BAD_REQUEST)