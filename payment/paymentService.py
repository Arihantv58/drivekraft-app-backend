import json
from flask import request
import requests
import payment.paymentDao as paymentDao
import user.userService as userService
def createRazorpayOrder():
    obj = json.loads(request.data)
    amount = obj['amount']

    url = "https://api.razorpay.com/v1/orders"

    payload = json.dumps({
      "amount": int(amount)*100,
      "currency": "INR",
      "receipt": "Drivekraft"
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Basic cnpwX2xpdmVfVFR2bFp1VDZDOVZZQ2Y6OXhVNVBhUnVFbktwVUJvQWh1OEtwRUhR'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    userId = userService.getUser().id

    responseDict= json.loads(response.text)
    paymentDao.storePaymentOrder(responseDict, userId)

    return responseDict
