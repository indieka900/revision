import requests
import json
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime

class MpesaCredentials:
    consumer_key = '0SGf9AyyWOL178BczGEIr7R6ScdpYILvU9ACN0IPbwGGjwl7'
    consumer_secret = 'EVn20BnzL4YwLETec0yuA8HXPBQxIBq10QhsSiC8OjLuzCGfPijzA9bz0lOWxmQd'
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    
class MpesaAccessToken:
    r = requests.get(
        MpesaCredentials.api_url, 
        auth=HTTPBasicAuth(MpesaCredentials.consumer_key, MpesaCredentials.consumer_secret)
        )
    mpesa_access_token = json.loads(r.text)['access_token']
    print(f"Access token {mpesa_access_token}")
    
class MpesaPassword:
    pay_time = datetime.now().strftime('%Y%m%d%H%M%S')
    business_short_code = '174379'
    offset_value = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    data_to_encode = business_short_code + passkey + pay_time
    print(f"data to encode {data_to_encode}")
    password = base64.b64encode(data_to_encode.encode())
    print(f"Password {password}")
    decode_password = password.decode('utf-8')
    print(f"Decoded password {decode_password}")