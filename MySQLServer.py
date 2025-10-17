import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Step 1: Connect to MySQL server (not to a specific database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # Replace with your MySQL username
            password="Mich@mwichuhulu1" # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Step 2: Create the database if it doesn’t exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Step 3: Ensure cursor and connection are closed properly
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()
