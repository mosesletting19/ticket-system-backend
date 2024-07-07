import requests
from requests.auth import HTTPBasicAuth
import base64
import datetime

class MpesaHandler:
    def __init__(self, consumer_key, consumer_secret, shortcode, passkey):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.shortcode = shortcode
        self.passkey = passkey
        self.auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        self.stk_push_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    
    def get_access_token(self):
        response = requests.get(
            self.auth_url, 
            auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret)
        )
        access_token = response.json()['access_token']
        return access_token

    def lipa_na_mpesa_online(self, phone_number, amount, callback_url):
        access_token = self.get_access_token()
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode(
            f"{self.shortcode}{self.passkey}{timestamp}".encode('utf-8')
        ).decode('utf-8')

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        payload = {
            "BusinessShortCode": self.shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": self.shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": callback_url,
            "AccountReference": "TicketPurchase",
            "TransactionDesc": "Purchase of event ticket"
        }

        response = requests.post(self.stk_push_url, json=payload, headers=headers)
        return response.json()
