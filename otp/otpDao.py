from db import connect,disconnect
import  configuration.currentTime as currentTime
import  otp.otp as otp
import otp.token as token
from datetime import timedelta

def addOtp(userId, Otp):
    now=currentTime.getCurrentTimeInIst()
    connection_pool,obj=connect()
    mycursor = obj.cursor(buffered=True)
    sql= f"Insert into otp(userId,otpvalue,created,updated) values('{userId}','{Otp}','{now}','{now}')"
    mycursor.execute(sql)
    obj.commit()
    disconnect(connection_pool,obj,mycursor)
    return "value updated in db"

def getLastOtpByUserId(userId):
    connection_pool,obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,userId,otpvalue, state,created from otp where userId='{userId}' order by id desc limit 1"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return otp.otp(data[0],data[1],data[2],data[3],data[4])


def storeToken(tokenValue,userId):
    now=currentTime.getCurrentTimeInIst()
    expiryDate = now + timedelta(days=30)
    connection_pool,obj=connect()
    mycursor = obj.cursor(buffered=True)
    sql= f"Insert into token(userId,tokenvalue,created,expireAt) values('{userId}','{tokenValue}','{now}','{expiryDate}')"
    mycursor.execute(sql)
    obj.commit()
    disconnect(connection_pool,obj,mycursor)
    return "value updated in db"


def getTokenFromValueInternally(tokenValue):
    connection_pool,obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,userId,tokenvalue, created,expireAt from token where tokenvalue='{tokenValue}' order by id desc limit 1"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return token.token(data[0], data[1], data[2], data[3], data[4])

