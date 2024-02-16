from Db import Db

class User:
    def __init__(self):
        self.db = Db(host="localhost", user="root", password="root", database="db_discord")

    def create_account(self, name, firstName, email, password):
        query = "INSERT INTO user (name, first_name, email, password) VALUES (%s, %s, %s, %s)"  # The query to execute
        values = (name, firstName, email, password)  # The values to insert
        self.db.execute(query, values)
    
    def get_user(self, email):
        query = "SELECT * FROM user WHERE email = %s"
        values = (email,)
        return self.db.fetch(query, values)
    
    def get_user_by_id(self, id):
        query = "SELECT * FROM user WHERE id = %s"
        values = (id,)
        return self.db.fetch(query, values)
    