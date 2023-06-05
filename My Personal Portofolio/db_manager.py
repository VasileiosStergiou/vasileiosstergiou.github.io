import mysql.connector
import datetime

class db_manager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="bill",
            password="1771999bs",
            database="email_db"
        )
        self.cursor = self.conn.cursor()

    def fetchData(self):
        # Create a connection
        self.cursor.execute("SELECT * FROM person_info")
        result = self.cursor.fetchall()
        self.conn.close()
        return result