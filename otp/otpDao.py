from db import connect,disconnect
from configuration.currentTime import getCurrentTimeInIst

def addOtp(userId, Otp):
    now=getCurrentTimeInIst()
    obj=connect()
    mycursor = obj.cursor(buffered=True)
    sql= f"Insert into otp(userId,otpvalue,created,updated) values('{userId}','{Otp}','{now}','{now}')"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj,mycursor)
    return "value updated in db"