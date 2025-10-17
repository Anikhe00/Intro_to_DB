import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MYSQL server
        mydb = mysql.connector.connect(
            host='localhost',
            user='Keerah',
            password='1234'
        )
        if mydb.is_connected():
            mycursor = mydb.cursor()

            # Create database if it doesn't exist
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error Connecting to MySQL: {e}")
    finally:
        # Close the connection
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

# Run the function
if __name__ == "__main__":
    create_database()