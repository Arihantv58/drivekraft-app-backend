from db import connect,disconnect
import logging
import  configuration.currentTime as currentTime


def createRequest(listnerId,userId):
    obj=connect()
    mycursor = obj.cursor(buffered=True)
    sql= f"Insert into sessionRequest(listener_id,customer_id, expiry_at, updated_at,created_at) values('{listnerId}','{userId}',now(), now(), now())"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj,mycursor)
    logging.info(f"request created with useId : {userId} and listnerId : {listnerId}")
    return "session request  is created"



