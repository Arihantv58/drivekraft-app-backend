import sessionRequest.sessionRequestDao as sessionRequestDao
import json
from flask import request,jsonify
import user.userService as userService
import otp.otpService as otpService
import sessionRequest.sessionRequestDao as sessionRequestDao

def sendSessionRequest():
    obj = json.loads(request.data)
    listnersId = obj['listener_id']

    tokenValue = userService.getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)

    sessionRequestDao.createRequest(listnersId,token.userId)

    sessionRequest=sessionRequestDao.getLastRequestByUserId(token.userId)

    return ({
        'data': str(sessionRequest.__dict__)
    })

def cancelSessionRequest():
    obj = json.loads(request.data)
    sessionRequestId = obj['session_request_id']
    sessionRequestDao.cancelSessionRequestBySessionId(sessionRequestId)

    return ({
        'status' : 'Success',
        'message': "Session request cancelled.",
    })