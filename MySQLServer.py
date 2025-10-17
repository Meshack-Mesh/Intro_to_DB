import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mich@mwichuhulu1"  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Safely close the connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function
if __name__ == "__main__":
    create_database()

