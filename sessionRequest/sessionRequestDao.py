from db import connect,disconnect
import logging
import  configuration.currentTime as currentTime
from sessionRequest import sessionRequest


def createRequest(listnerId,userId):
    obj=connect()
    mycursor = obj.cursor(buffered=True)
    sql= f"Insert into sessionRequest(listener_id,customer_id, expiry_at, updated_at,created_at) values('{listnerId}','{userId}',DATE_ADD(now(),INTERVAL 2 MINUTE), now(), now())"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj,mycursor)
    logging.info(f"request created with useId : {userId} and listnerId : {listnerId}")
    return "session request  is created"


def getLastRequestByUserId(userId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,listener_id,is_cancelled,customer_id,status, expiry_at,updated_at,created_at from sessionRequest where customer_id='{userId}' order by id desc limit 1"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return sessionRequest.sessionRequest(data[0], data[1], data[2], data[3], data[4], data[5], data[6],data[7])

def cancelSessionRequestBySessionId(sessionRequestId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    sql =f"Update sessionRequest set is_cancelled ='1' , updated_at =now() where id ='{sessionRequestId}'"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj, mycursor)

    logging.info(f"session with id  {sessionRequestId} has been cancelled")
    return "session has been cancelled"


def verifySessionRequestBySessionId(sessionRequestId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,listener_id,is_cancelled,customer_id,status, expiry_at,updated_at,created_at from sessionRequest where id='{sessionRequestId}' "
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return sessionRequest.sessionRequest(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])

def isExpiredOrCancelled(sessionRequestId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id from sessionRequest  where id='{sessionRequestId}' and (expiry_at >= now() or is_cancelled =1 )"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return True
    else:
        return False

def confirmSessionById(sessionRequestId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    sql =f"Update sessionRequest set status ='1' , updated_at =now() where id ='{sessionRequestId}'"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj, mycursor)

    logging.info(f"session with id  {sessionRequestId} has been confirmed")
    return "session has been confirmed"