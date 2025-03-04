# pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error, connect

db_config = { "host" : "localhost",
    "database" : "todos_db",
    "username" : "root",
    "password" : "tanya"
    }

def get_db():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
        return None
    except Error as e: 
        print(f"Error connecting to databasecand error is {e}")
        return None

