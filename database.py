import mysql.connector

class Database:
    def connect(self):
        
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="vansh@989sql",
            database="garbage_db3"
        )
        return con
