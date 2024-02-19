from Db import Db

class Session:
    def __init__(self):
        self.db = Db(host='localhost', user='root', password='root', db='db_discord')
        self.current_user_id = None

    def login(self, user_id):
        self.current_user_id = user_id

    def logout(self):
        self.current_user_id = None

    def get_current_user(self):
        return self.current_user_id
    