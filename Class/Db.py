import mysql.connector

class Db:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()
        self.cursor.close()

    def execute(self, query, values=None):
        self.connect()
        self.cursor.execute(query, values)
        self.connection.commit()
        self.disconnect()
    
    def fetch(self, query, values=None):
        self.connect()
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        self.disconnect()
        return result