from Class.Back.Db import Db
import hashlib
from Class.Back.Notification import Notification

class User:
    def __init__(self):
        self.db = Db(host="localhost", user="root", password="root", database="db_discord")

    def create_account(self, name, firstName, email, password):
        def sha256_hash(password):              #hash function and in parameter password chosen
            sha256 = hashlib.sha256()           
            sha256.update(password.encode('utf-8'))
            return sha256.hexdigest()
        
        hashed_password= sha256_hash(password)  #hash password before insert in data base     

        query = "INSERT INTO users (username, user_first_name, mail, passwd) VALUES (%s, %s, %s, %s)"  # The query to execute
        values = (name, firstName, email, hashed_password)  # The values to insert
        self.db.execute(query, values)

        Notification().set_messages_counter(self.get_user(email)[0][0], 1, 0)

    
    def get_user(self, email):
        query = "SELECT * FROM users WHERE mail = %s"
        values = (email,)
        return self.db.fetch(query, values)
    
    def get_user_by_id(self, id):
        query = "SELECT * FROM users WHERE id = %s"
        values = (id,)
        return self.db.fetch(query, values)
    
    def get_all_users(self):
        query = "SELECT id, username, user_first_name, mail FROM users"
        return self.db.fetch(query)
    