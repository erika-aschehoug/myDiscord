from Class.Back.Db import Db
from Class.Back.User import User
from Class.Back.Session import Session
import bcrypt

class Connection(User):
    def __init__(self):
        User.__init__(self)
        self.db = Db(host='localhost', user='root', password='root', database='db_discord')

    def check_mail(self, mail): # check if the mail is already in the database
        query = "SELECT mail FROM users"
        list_mail = self.db.fetch(query)
        if mail in list_mail:
            return True
        else:
            return False
        
    def verify_password(self, password, hashed_password): # verify if the password is correct
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
    
    def login(self, mail, password): # login the user
        user = self.get_user(mail)
        if user and self.verify_password(password, user['password']):
            Session.login(user['id']) # get the user id
            return True
        else:
            return False
