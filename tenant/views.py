from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

AREA_CODE = 2 # 0 space , 1 namespace , 2 tenant

@login_required(login_url='/login/')
def main(request,pk):
    area_code = AREA_CODE
    return render_to_response('tenant.html',locals())

@login_required(login_url='/login/')
def tenant_settings(request,pk):
    area_code = AREA_CODE
    return render_to_response('tenant-settings.html',locals())