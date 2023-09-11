from flask import request,jsonify
import user.userDao as userDao
import json
import otp.otpService as otpService
import psychologist.psychologistService as psychologistService

def createUser(contactNumber):
    return userDao.addUser(contactNumber)

def UserByContact(contactNumber):
    return userDao.getUserByContact(contactNumber)

def firebaseUser():

    tokenValue =getTokenFromRequest()
    token=otpService.getTokenFromTokenValue(tokenValue)
    userDao.updateUserFirebaseData(token.userId)

    user = userDao.getUserById(token.userId)

    return jsonify({
        "msg": "Successfully Updated.",
        "status" :"Success",
        "user" : (user.__dict__)
    })


def updateBusyStatus():
    user = getUser()
    status = request.form.get('busy')
    userDao.updateUsetStatus(user.id,status)

    return jsonify({
        "msg": "Successfully Updated",
        "user": (getUser().__dict__)
    })


def getUser():
    print("before token")
    tokenValue = getTokenFromRequest()
    print("after token " , tokenValue )
    token = otpService.getTokenFromTokenValue(tokenValue)

    user = userDao.getUserById(token.userId)
    return user



def getTokenFromRequest():
    headers = request.headers
    bearer = headers.get('Authorization')  # Bearer YourTokenHere
    token = bearer.split()[1]  # YourTokenHere

    return token

def checkUsername():
    username = request.form.get('username')
    id = userDao.getUserByUserName(username)
    if id ==None:
        return jsonify({
            "status": True,
             "message": "Username is available.",
        })

    return jsonify({
        "status": False,
        "message": "Username is not available",
    })         


def getUserRoleID():
    tokenValue = getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)

    user = userDao.getUserById(token.userId)
    return user.role_id


def addUserCredit(amt):
    user = getUser()
    userDao.updateUserBalance(user.id,amt+ user.credits)
    return


def setUserOnline():
    user = getUser()
    status = request.form.get('online_status')
    userDao.updateUserAvailStatus(user.id, status)

    return jsonify({
        "msg": "Successfully Updated.",
        'status' : 'Success',
        "user": (getUser().__dict__)
    })

def checkUserBusy():
    psyId = request.form.get('psychologist_id')
    psychologist = psychologistService.getPsychologistById(psyId)
    user= userDao.getUserById(psychologist.user_id)

    return jsonify({
        "is_busy": user.is_busy,
        'is_online': user.online

    })



def checkUserBalance():
    user = getUser()

    return jsonify({
        "credits": user.credits
    })

def getUserById(id):
    return userDao.getUserById(id)