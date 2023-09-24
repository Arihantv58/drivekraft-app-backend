import json
from flask import request,jsonify
import requests
import payment.paymentDao as paymentDao
import user.userService as userService
import user.userDao as userDao
def createRazorpayOrder():
    amount=request.form.get('amount')

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
    #obj = json.loads(request.data)
    transId = request.form.get('transaction_id')

    if user.credits<5 :
        return jsonify({
            "user_credits": user.credits,
            "status": "Error",
            "msg":'Insufficient credits'
        })

    transactional = paymentDao.getTransactionaByTransId(transId)
    seconds_chatted = request.form.get('seconds_chatted')
    cost = int((int(seconds_chatted) + 60)/60) * 5

    if transactional== None:
         transId=paymentDao.createTranaction(user.id,request.form.get('psychologist_id'),request.form.get('session_request_id'),request.form.get('seconds_chatted'),cost)
    else:
         paymentDao.updateTranaction(transId,seconds_chatted,cost)

    userDao.updateUserBalance(user.id,user.credits-5)
    sufficent_balance = True
    availability = True

    if user.credits <25:
        sufficent_balance = False

    if user.credits <5:
        availability = False

    return jsonify({
        "transaction": (paymentDao.getTransactionaByTransId(transId)).__dict__,
        "user_credits": user.credits,
        "credits_availablility": availability,
        "credits_sufficient_for_five_minutes": sufficent_balance
    })

def confirmRazorpayOrder():
    payload = request.json
    if 'razorpay_payment_id' in payload:
        paymentDao.updatePamentOrder(payload['razorpay_order_id'],payload['razorpay_payment_id'],payload['razorpay_signature'],'razorpay')

        url = f"https://api.razorpay.com/v1/orders/{payload['razorpay_order_id']}"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic cnpwX2xpdmVfVFR2bFp1VDZDOVZZQ2Y6OXhVNVBhUnVFbktwVUJvQWh1OEtwRUhR'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            responseDict = json.loads(response.text)
            if responseDict['status'] == 'paid':
               # paymentDao.updateOrderStatus(payload['razorpay_order_id'],True) will add filed in future and do this
                userService.addUserCredit(responseDict['amount']/100)

                return jsonify({'msg': 'Your payment id is ' + payload['razorpay_order_id'] + '.', 'status': 'success',
                                'title': 'Session Booked.'})

        else:
             return jsonify({'msg': 'Payment Failed.', 'status': 'error', 'title': 'Error'})

    else:
        return jsonify({'msg': 'Session Booking Failed.', 'status': 'error', 'title': 'Error'})