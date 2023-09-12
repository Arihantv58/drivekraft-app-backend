from db import connect,disconnect
import  configuration.currentTime as currentTime
import logging
def addFeedback(sessionId,feedback,rating):
    now = currentTime.getCurrentTimeInIst()
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    sql = f"Insert into sessionFeedback(sessionId,feedback,rating,created_at,updated_at) values('{sessionId}','{feedback}','{rating}','{now}','{now}')"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj, mycursor)
    logging.info(f"sessionFeedback with for session  {sessionId} created")
    return "feedback updated"