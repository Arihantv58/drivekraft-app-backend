import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling





# connect pool can be introduced to speed up

# def connect():
#     connection = mysql.connector.connect(host='127.0.0.1',
#                                          database='drivekraft_backend',
#                                          user='root',
#                                          password='root')
#
#     #connection_object = connection_pool.get_connection()
#     return connection

def connect():
    connection = mysql.connector.connect(host= 'drivekraftbackend.mysql.pythonanywhere-services.com',
                                         database='drivekraftbacken$drivekraft_backend',
                                         user='drivekraftbacken',
                                         password='wearecodingdb')

    #connection_object = connection_pool.get_connection()
    return connection

def disconnect(connection_object,cursor):
    if(connection_object.is_connected()):
        cursor.close()
        connection_object.close()