import sessionRequest.sessionRequestDao as sessionRequestDao
import json
from flask import request
import user.userService as userService
import otp.otpService as otpService
def sendSessionRequest():
    obj = json.loads(request.data)
    listnersId = obj['listener_id']

    tokenValue = userService.getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)


    return sessionRequestDao.createRequest(listnersId,token.userId)