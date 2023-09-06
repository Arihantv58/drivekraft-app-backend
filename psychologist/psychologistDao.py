from db import connect,disconnect
import  psychologist.psychologist as psychologist
import json

def getPsychologistInOrder():
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = '''select id,name,profile_image,is_busy,firebase_id,firebase_name,firebase_email,firebase_password,uuid,
      user_id, description,session_count,rating,
               yrs_of_exp,education,short_desc,status,order_,created_at
               ,updated_at,gender,age,interests,languages,`online` from psychologist order by `online` desc , is_busy '''
    mycursor.execute(query)
    psyData = mycursor.fetchall()

    psychologistList= list()

    for data in psyData:
        psy=psychologist.psychologist(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                     data[11], data[12], data[13],data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24])

        psychologistList.append(psy.__dict__)

    return psychologistList


def getPsychologistById(psyId):
    obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f'''select id,name,profile_image,is_busy,firebase_id,firebase_name,firebase_email,firebase_password,uuid,
          user_id, description,session_count,rating,
                   yrs_of_exp,education,short_desc,status,order_,created_at
                   ,updated_at,gender,age,interests,languages,`online` from psychologist where id ='{psyId}' '''
    mycursor.execute(query)
    data = mycursor.fetchone()

    if data == None:
        return None
    return psychologist.psychologist(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                     data[11], data[12], data[13],data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24])


