from django.shortcuts import render
from django.http import *

# Create your views here.
def main(request):
    return HttpResponse("dashboards")