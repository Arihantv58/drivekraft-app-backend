from flask import request, jsonify
import json
import logging
from validation.contactValidation import isValidContact
from random import randint
from externalAPIs.whatsappApi import sendTemplateChatApi as chatApi
from user.userService import createUser,UserIdByContact
from otp.otpDao import addOtp





def sendOtpInternally():
    obj = json.loads(request.data)
    contactNumber = obj['mobile']

    if  isValidContact(contactNumber)== False:
         return jsonify({
        "Message": "Please enter correct contact number",
    })

    otp= generateOtp()
    chatApi.sendTemplate('otp', [otp],[], contactNumber)
    logging.info(f"OTP :  {otp} send to user")

    userId= UserIdByContact(contactNumber)

    if userId ==None:
        createUser(contactNumber)
        userId = UserIdByContact(contactNumber)

    addOtp(userId,otp)
    return jsonify({
        "Message": "OTP has been sent to user",
        "OTP" : otp
    })

def generateOtp():
        return randint(100000, 1000000)

