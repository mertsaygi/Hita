from django.http import *
from management.models import *
from django.contrib.auth.decorators import login_required
import requests
from django.shortcuts import render_to_response,get_object_or_404

AREA_CODE = 2 # 0 space , 1 namespace , 2 tenant

@login_required(login_url='/login/')
def main(request,pk):
    area_code = AREA_CODE
    return render_to_response('tenant.html',locals())

@login_required(login_url='/login/')
def remove_tenant(request,pk):
    area_code = AREA_CODE
    user_profile = UserProfile.objects.filter(user=request.user)
    if user_profile.count() > 0:
        response = requests.get(
            'http://127.0.0.1:8000/api/delete-tenant/'+pk)
        if response.status_code != 200:
            return HttpResponse(response)
        else:
            return HttpResponseRedirect('/spaces/')
    return HttpResponseRedirect('/spaces/')

@login_required(login_url='/login/')
def tenant_settings(request,pk):
    area_code = AREA_CODE
    return render_to_response('tenant-settings.html',locals())