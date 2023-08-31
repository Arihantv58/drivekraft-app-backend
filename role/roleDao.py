from db import connect,disconnect
import  role.role as role
import logging

def getRoleFromId(role_id):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"select id,name, label,created_at,updated_at from role where id='{role_id}'"
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return role.role(data[0] ,data[1] ,data[2] ,data[3] ,data[4])
