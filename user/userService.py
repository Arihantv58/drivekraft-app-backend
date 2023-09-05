from flask import request,jsonify
import user.userDao as userDao
import json
import otp.otpService as otpService

def createUser(contactNumber):
    return userDao.addUser(contactNumber)

def UserByContact(contactNumber):
    return userDao.getUserByContact(contactNumber)

def firebaseUser():
    obj = json.loads(request.data)

    tokenValue =getTokenFromRequest()
    token=otpService.getTokenFromTokenValue(tokenValue)
    userDao.updateUserFirebaseData(token.userId,obj)

    user = userDao.getUserById(token.userId)

    return jsonify({
        "msg": "Successfully Updated.",
        "status" :"Success",
        "user" : json.dumps(user.__dict__)
    })

def getUser():
    tokenValue = getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)

    user = userDao.getUserById(token.userId)
    return user




def getTokenFromRequest():
    headers = request.headers
    bearer = headers.get('Authorization')  # Bearer YourTokenHere
    token = bearer.split()[1]  # YourTokenHere

    return token

def checkUsername():
    obj = json.loads(request.data)
    username = request.args.get('username')
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




