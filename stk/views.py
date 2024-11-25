from django.shortcuts import render
from django.http import HttpResponse
import requests
from .credentials import MpesaAccessToken, MpesaPassword

def home(request):
    return render(request, 'homepage.html')

def checkout(request):
    return render(request, 'checkout.html')

def stk(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        amount = request.POST['amount']
        a_token = MpesaAccessToken.mpesa_access_token
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {'Authorization': f"Bearer {a_token}"}
        request_body = {    
            "BusinessShortCode": MpesaPassword.business_short_code,    
            "Password": MpesaPassword.decode_password,    
            "Timestamp": MpesaPassword.pay_time,    
            "TransactionType": "CustomerPayBillOnline",    
            "Amount": amount,    
            "PartyA": phone,    
            "PartyB": MpesaPassword.business_short_code,    
            "PhoneNumber": phone,    
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa",    
            "AccountReference":"Test",    
            "TransactionDesc":"Test"
        }
        response = requests.post(api_url, json=request_body, headers=headers)
        print(response)
    return HttpResponse('Success')