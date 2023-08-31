from db import connect,disconnect
import logging
import  configuration.currentTime as currentTime
import  user.user as user

def addUser(contactNumber):
    now=currentTime.getCurrentTimeInIst()
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
    query = f"select id,name, username ,emailId,contact,totalSessions,firebase_id,firebase_name,firebase_email,firebase_password,credits,role_id,is_online,is_busy from user where contact='{contactNumber}'"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return user.user(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13])


def getUserById(userId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,name,username, emailId,contact,totalSessions,firebase_id,firebase_name,firebase_email,firebase_password,credits,role_id,is_online,is_busy from user where id='{userId}'"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return user.user(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13])




def updateUserFirebaseData(userId,responseObj):
    now = currentTime.getCurrentTimeInIst()
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    sql = f"Update user set  firebase_id ='{responseObj['firebase_id']}' , firebase_name ='{responseObj['firebase_name']}' , firebase_email ='{responseObj['firebase_email']}' , firebase_password = '{responseObj['firebase_password']}' , updated ='{now}' where id ='{userId}'"
    mycursor.execute(sql)
    obj.commit()
    disconnect(obj, mycursor)
    logging.info(f"user with user id {userId} updated")
    return "user is updated"


def getUserByUserName(username):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id from user where username='{username}'"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return data[0]


