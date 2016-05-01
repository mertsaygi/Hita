from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.middleware import csrf
from management.models import *
import requests

AREA_CODE = 1 # 0 space , 1 namespace , 2 tenant

def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token

@login_required(login_url='/login/')
def main(request,pk):
    csrf_token = get_or_create_csrf_token(request)
    area_code = AREA_CODE
    nspace = pk
    try:
        space = UserSubspaces.objects.get(pk=nspace)
        response = requests.get("http://127.0.0.1:8000/api/files/list/"+str(nspace),verify=False)
        user_files = response.json()
        return render_to_response('namespaces.html',locals())
    except UserSubspaces.DoesNotExist:
        return HttpResponseRedirect('/spaces/')

@login_required(login_url='/login/')
def remove_namespace(request,pk):
    area_code = AREA_CODE
    user_profile = UserProfile.objects.filter(user=request.user)
    if user_profile.count() > 0:
        response = requests.get('http://127.0.0.1:8000/api/namespace/delete/'+pk)
        if response.status_code != 200:
            return HttpResponse(response)
        else:
            return HttpResponseRedirect('/namespaces/'+pk)
    return HttpResponseRedirect('/namespaces/'+pk)

@login_required(login_url='/login/')
def namespace_settings(request,pk):
    area_code = AREA_CODE
    return render_to_response('namespace-settings.html',locals())