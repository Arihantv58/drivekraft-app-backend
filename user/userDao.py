from db import connect,disconnect
from configuration.currentTime import getCurrentTimeInIst
import logging
from user.user import user

def addUser(contactNumber):
    now=getCurrentTimeInIst()
    obj=connect()
    mycursor = obj.cursor(buffered=True)
    sql= f"Insert into user(contact,created,updated) values('{contactNumber}','{now}','{now}')"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj,mycursor)
    logging.info(f"user with contact number {contactNumber} created")
    return "user is created"

def getUserByContact(contactNumber):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,name, emailId,contact,totalSessions from user where contact='{contactNumber}'"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return user(data[0],data[1],data[2],data[3],data[4])