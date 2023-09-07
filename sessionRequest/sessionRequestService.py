import sessionRequest.sessionRequestDao as sessionRequestDao
import json
from flask import request,jsonify
import user.userService as userService
import otp.otpService as otpService
import sessionRequest.sessionRequestDao as sessionRequestDao

def sendSessionRequest():
    listnersId = request.form.get('listener_id')

    tokenValue = userService.getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)

    sessionRequestDao.createRequest(listnersId,token.userId)

    sessionRequest=sessionRequestDao.getLastRequestByUserId(token.userId)

    return ({
        'data': str(sessionRequest.__dict__)
    })

def cancelSessionRequest():
    obj = json.loads(request.data)
    sessionRequestId = request.form.get('session_request_id')
    sessionRequestDao.cancelSessionRequestBySessionId(sessionRequestId)

    return ({
        'status' : 'Success',
        'message': "Session request cancelled.",
    })

def verifySessionRequest():
    obj = json.loads(request.data)
    sessionRequestId = request.form.get('session_request_id')

    sessionRequest=sessionRequestDao.verifySessionRequestBySessionId(sessionRequestId)

    return ({
        'session': str(sessionRequest.__dict__)
    })

def confirmSessionRequest():
    obj = json.loads(request.data)
    sessionRequestId = request.form.get('session_request_id')

    if sessionRequestDao.isExpiredOrCancelled(sessionRequestId)== True:
        return ({
            "status": "Error",
            "message": "Session request either expired or cancelled."
        })
    else:
        sessionRequestDao.confirmSessionById(sessionRequestId)
        sessionRequest = sessionRequestDao.verifySessionRequestBySessionId(sessionRequestId)

        return ({
            "status": "Success",
            "message": "Session request successfully confirmed.",
            'session': str(sessionRequest.__dict__)
        })

def fetchSessionRequest():
    user= userService.getUser()
    return sessionRequestDao.getValidSessionRequest(user.id)




