from db import connect,disconnect
from configuration.currentTime import getCurrentTimeInIst
from otp.otp import otp
from datetime import timedelta

def addOtp(userId, Otp):
    now=getCurrentTimeInIst()
    obj=connect()
    mycursor = obj.cursor(buffered=True)
    sql= f"Insert into otp(userId,otpvalue,created,updated) values('{userId}','{Otp}','{now}','{now}')"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj,mycursor)
    return "value updated in db"

def getLastOtpByUserId(userId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,userId,otpvalue, state,created from otp where userId='{userId}' order by id desc limit 1"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return otp(data[0],data[1],data[2],data[3],data[4])


def storeToken(tokenValue,userId):
    now=getCurrentTimeInIst()
    expiryDate = now + timedelta(days=30)
    obj=connect()
    mycursor = obj.cursor(buffered=True)
    sql= f"Insert into token(userId,tokenvalue,created,expireAt) values('{userId}','{tokenValue}','{now}','{expiryDate}')"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj,mycursor)
    return "value updated in db"