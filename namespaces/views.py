from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.middleware import csrf

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
    return render_to_response('namespaces.html',locals())