from db import connect,disconnect
import logging
import payment.transaction
import uuid

def storePaymentOrder(responseDict, userId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    sql = f"Insert into paymentOrder(order_id, payment_id,signature,amount,userId," \
          f"paymentGateway,created_at,updated_at) values('{responseDict['id']}','none','none'," \
          f"'{responseDict['amount']/100}','{userId}' ,'Razorpay',now(),now())"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj, mycursor)
    logging.info(f"order for user {userId} created for amount {responseDict['amount']/100}")
    return "order created is created"


def getTransactionaByTransId(transId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,transaction_id, user_id,psychologist_id,session_request_id,seconds_chatted,amount_deducted,created_at,updated_at from transaction where transaction_id='{transId}'"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return payment.transaction(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])


def createTranaction(user_id,psychologist_id,session_request_id,seconds_chatted,cost):
    tranactionalId= str(uuid.uuid4())
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    sql = f"Insert into transaction(transaction_id, user_id,psychologist_id," \
          f"session_request_id,seconds_chatted,amount_deducted,created_at,updated_at)" \
          f" values('{tranactionalId}','{user_id}','{psychologist_id}','{session_request_id}'," \
          f"'{seconds_chatted}','{cost}', now(), now() )"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj, mycursor)
    logging.info(f"transaction created with {tranactionalId} id")
    return tranactionalId

def updateTranaction(transId,seconds_chatted,cost):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    sql = f"Update transaction set seconds_chatted ='{seconds_chatted}' ,amount_deducted ='{cost}' ,updated_at =now() where id ='{transId}'"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj, mycursor)

    logging.info(f"transaction upated with {tranactionalId} id")
    return