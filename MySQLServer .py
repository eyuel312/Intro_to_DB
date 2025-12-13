import mysql.connector
from mysql.connector import errorcode
HOST = "localhost"       
USER = "root"            
PASSWORD = "your_password"  

try:
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    cursor = connection.cursor()
  
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
