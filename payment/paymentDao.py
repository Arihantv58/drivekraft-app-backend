from db import connect,disconnect
import logging
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


