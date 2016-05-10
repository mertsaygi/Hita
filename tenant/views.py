from django.http import *
from management.models import *
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from django.shortcuts import render_to_response,get_object_or_404
from django.core.urlresolvers import reverse

AREA_CODE = 2 # 0 space , 1 namespace , 2 tenant

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
    nspace_container = pk
    try:
        user_spaces = UserSubspaces.objects.filter(user=request.user,parent_space=UserSpaces.objects.get(pk=pk))
    except UserSpaces.DoesNotExist:
        return HttpResponseRedirect('/spaces/')
    return render_to_response('tenant.html',locals())

@login_required(login_url='/login/')
def tenant_settings(request,pk):
    csrf_token = get_or_create_csrf_token(request)
    area_code = AREA_CODE
    return render_to_response('tenant-settings.html',locals())