from flask import request,jsonify
import user.userDao as userDao
import json
import otp.otpService as otpService

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
            "Message": "Invalid user",
        })

    return jsonify({
        "Message": "User exist in our system",
    })         


def getUserRoleID():
    tokenValue = getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)

    user = userDao.getUserById(token.userId)
    return user.role_id




