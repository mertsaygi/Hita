# -*- coding: utf-8 -*-
from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.middleware import csrf
from management.models import *
from django.conf import settings
import json
import paypalrestsdk
from models import *
import requests, hashlib, base64, time

AREA_CODE = 0 # 0 space , 1 namespace , 2 tenant

def build_string(*args):
    return ''.join([str(a) for a in args])

def prepare_hash(clientid,orderid,amount,okUrl,failUrl,islemtipi,rnd,storekey):
    string_to_be_hashed = build_string(clientid,orderid,amount,okUrl,failUrl,islemtipi,rnd,storekey)
    sha1_hashed = hashlib.sha1(string_to_be_hashed).digest()
    base64_enc = base64.b64encode(sha1_hashed)
    return base64_enc

def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token

@login_required(login_url='/login/')
def main(request):
    csrf_token = get_or_create_csrf_token(request)
    area_code = AREA_CODE
    error_code = request.GET.get('c')
    data = open(settings.STATIC_URL+ "/staticdata/countries.json").read()
    data = json.loads(data)
    if request.method == "POST":
        user_profile = UserProfileSerializer(request.POST.get('firstname'),request.POST.get('lastname'),request.POST.get('phone'),request.POST.get('address'),request.POST.get('city'),request.POST.get('state'),request.POST.get('postal'),request.POST.get('country'))
        credit_card = CreditCardSerializer(request.POST.get('cardnumber'),request.POST.get('holdername'),request.POST.get('expration'),request.POST.get('cvv'))
        expration = request.POST.get('expration')
        expration = expration.split("/")
        return make_3d_payment(request,1.0,request.POST.get('cardnumber'),expration[1],expration[0],request.POST.get('cvv'),request.POST.get('holdername'))
    return render_to_response('payment.html',locals())

@login_required(login_url='/login/')
def success(request):
    csrf_token = get_or_create_csrf_token(request)
    user = request.user
    user.is_active = True
    user.save()
    return HttpResponseRedirect("/spaces/")

@login_required(login_url='/login/')
def fail(request):
    csrf_token = get_or_create_csrf_token(request)
    return HttpResponse("fail")

def make_3d_payment(request,order,credit_card,exp_year,exp_month,cvv,cardholder_name):
    rnd = int(round(time.time() * 1000))
    if credit_card[0] == "4":
        brand = 1
    elif credit_card[0] == "5":
        brand = 2
    elif credit_card[0] == "6":
        brand = 3
    else:
        brand = ""
    payload = {
        'clientid' : settings.EST_MERCHANT_ID,
        'islemtipi' : 'Auth',
        'okUrl': settings.EST_RETURN_URL,
        'failUrl': settings.EST_FAIL_URL,
        'storetype':'3d_pay',
        'amount' :  "{0:.2f}".format(order),
        'currency' : '949',
        'cardType' : brand,
        'mode' : 'TEST',
        'pan': credit_card,
        'Ecom_Payment_Card_ExpDate_Year':exp_year,
        'Ecom_Payment_Card_ExpDate_Month':exp_month,
        'cv2':cvv,
        'rnd': rnd,
        'hash': prepare_hash(settings.EST_MERCHANT_ID,2,"{0:.2f}".format(order),settings.EST_RETURN_URL,settings.EST_FAIL_URL,"Auth",rnd,settings.EST_3D_KEY),
        'oid': 2,
        'lang':'tr',
    }
    resp = requests.post(settings.EST_3D_URL, data=payload, verify=False)
    print resp.headers
    print resp.text
    return HttpResponse(resp.text)

def finalize_3d_payment(request,result):
    order_id = result.get("oid")
    response = result.get("Response")
    if response == "Approved":
        transaction_id = result.get("TransId")
        #başarılı olarak kaydet
        return redirect("success_page")
    else:
        return redirect("checkout_page")

def paypal(request):
    api = paypalrestsdk.configure({'mode': 'sandbox','client_id': settings.CLIENT_ID,'client_secret': settings.CLIENT_SECRET})
    payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
    "payment_method": "paypal" },
    "redirect_urls": {
        "return_url": "https://devtools-paypal.com/guide/pay_paypal/python?success=true",
        "cancel_url": "https://devtools-paypal.com/guide/pay_paypal/python?cancel=true" },
    "transactions": [ {
        "amount": {
            "total": "1",
            "currency": "USD" },
    "description": "Hita Account Registration" } ] }, api=api)
    payment.create()
    print payment['links'][1]['href']
    return HttpResponseRedirect(payment['links'][1]['href'])