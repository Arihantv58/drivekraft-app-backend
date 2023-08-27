from db import connect,disconnect
from configuration.currentTime import getCurrentTimeInIst
import logging

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

def getUserIdByContact(contactNumber):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id from user where contact='{contactNumber}'"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return data[0]