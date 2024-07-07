from flask import Flask, request, jsonify
from mpesa_handler import MpesaHandler

app = Flask(__name__)

consumer_key = "M9yyMrwGNbYLcGjaZAYuGjimkfAhEZBw3s6aO9mhjuQ7lnbv"
consumer_secret = "fQV9ZQTIuZjRIcspRfRAzMB2ysAb9P0ZHq3z685iXNgWZQvcWbvbmkAWNU9tn1Yo"
shortcode = "4527586"
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

mpesa = MpesaHandler(consumer_key, consumer_secret, shortcode, passkey)

@app.route('/initiate-payment', methods=['POST'])
def initiate_payment():
    data = request.json
    phone = data.get('phone')
    amount = data.get('amount')
    callback_url = "http://localhost:3400/callback"  # Local callback URL for development
    response = mpesa.lipa_na_mpesa_online(phone, amount, callback_url)
    return jsonify(response)

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    # Process the callback data here
    return jsonify({"ResultCode": 0, "ResultDesc": "Accepted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3400, debug=True)
