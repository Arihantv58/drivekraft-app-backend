import json
from flask import request
import requests
import payment.paymentDao as paymentDao
import user.userService as userService
import user.userDao as userDao
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

def placeRazorpayOrder():
    user= userService.getUser()
    obj = json.loads(request.data)
    transId = obj['transaction_id']

    if user.credits<5 :
        return ({
            "user_credits": user.credits,
            "status": "Error",
            "msg":'Insufficient credits'
        })

    transactional = paymentDao.getTransactionaByTransId(transId)
    seconds_chatted = obj['seconds_chatted']
    cost = int((seconds_chatted + 60)/60) * 5;

    if transactional== None:
         transId=paymentDao.createTranaction(user.id,obj['psychologist_id'],obj['session_request_id'],obj['seconds_chatted'],cost)
    else:
         paymentDao.updateTranaction(transId,seconds_chatted,cost)

    userDao.updateUserBalance(user.id,user.credits-5)
    sufficent_balance = True
    availability = True

    if user.credits <25:
        sufficent_balance = False

    if user.credits <5:
        availability = False

    return ({
        "transaction": paymentDao.getTransactionaByTransId(transId),
        "user_credits": user.credits,
        "credits_availablility": availability,
        "credits_sufficient_for_five_minutes": sufficent_balance
    })
