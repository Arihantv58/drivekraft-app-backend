import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling





# connect pool can be introduced to speed up

def connect():
    # connection = mysql.connector.connect(host='127.0.0.1',
    #                                      database='drivekraft_backend',
    #                                      user='root',
    #                                      password='root')

    connection_pool = pooling.MySQLConnectionPool(pool_name="drivekraft_db_pool1",
                                                  pool_size=10,
                                                  pool_reset_session=True,
                                                  host='drivekraftbackend.mysql.pythonanywhere-services.com',
                                                  database='drivekraftbacken$drivekraft_backend',
                                                  user='drivekraftbacken',
                                                  password='wearecodingdb')

    # Get connection object from a pool
    connection_object = connection_pool.get_connection()

    #connection_object = connection_pool.get_connection()
    return connection_pool,connection_object

# def connect():
#     connection = mysql.connector.connect(host= 'drivekraftbackend.mysql.pythonanywhere-services.com',
#                                          database='drivekraftbacken$drivekraft_backend',
#                                          user='drivekraftbacken',
#                                          password='wearecodingdb')
#
#     #connection_object = connection_pool.get_connection()
#     return connection

def disconnect(connection_pool,connection_object,cursor):
    # if(connection_object.is_connected()):
    #     cursor.close()
    #     connection_object.close()

    print("release connection to pool")

    if cursor:
         cursor.close()

    #     # Release the connection back to the pool
    if connection_object:
         connection_object.close()