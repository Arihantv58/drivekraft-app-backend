from flask import request, jsonify, Response
import json
import logging
import string
import random
import  validation.contactValidation as contactValidation
from random import randint
import externalAPIs.whatsappApi.sendTemplateChatApi as chatApi 
import user.userService as userService
import otp.otpDao as otpDao






def sendOtpInternally():
    obj = json.loads(request.data)
    contactNumber = obj['mobile']

    if  contactValidation.isValidContact(contactNumber)== False:
         return jsonify({
        "Message": "Please enter correct contact number",
    })

    otp= generateOtp()
    chatApi.sendTemplate('otp', [otp],[], contactNumber)
    logging.info(f"OTP :  {otp} send to user")

    user= userService.UserByContact(contactNumber)

    if user ==None:
        userService.createUser(contactNumber)
        user = userService.UserByContact(contactNumber)

    otpDao.addOtp(user.id,otp)
    return jsonify({
        "Message": "OTP has been sent to user",
        "OTP" : otp
    })


def generateTokenInternally():
    obj = json.loads(request.data)
    contactNumber = obj['mobile']
    otpVal = obj['otp']

    user = userService.UserByContact(contactNumber)
    otp = otpDao.getLastOtpByUserId(user.id)
    logging.info(otpVal)
    logging.info(otp.otpvalue)
    if otpVal != str(otp.otpvalue):
        return Response("{'message':'OTP does not match.'}", status=401, mimetype='application/json')
         
    #need tocheck if token hasnt expired , then we can use that only by inc its expiry date .. if expired then we can generate new

    tokenValue= getToken()
    otpDao.storeToken(tokenValue,user.id)
    logging.info(f"token updated for user with contact number  :  {contactNumber}")

    return jsonify({
        "access_token": tokenValue,
        "token_type" : "Bearer"
    })



def generateOtp():
        return randint(100000, 1000000)


def getToken():
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=50))
    return res


def getTokenFromTokenValue(tokenValue):
    return otpDao.getTokenFromValueInternally(tokenValue)