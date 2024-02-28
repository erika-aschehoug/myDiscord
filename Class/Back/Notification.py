from Class.Back.Db import Db

class Notification:
    def __init__(self):
        self.db = Db(host='localhost', user='root', password='root', database='db_discord')

    def get_disconnection_datetime(self, id_user, datetime, channel):
        pass

    def get_notification(self, id_user, datetime, channel):
        query = "SELECT * FROM posts LEFT JOIN users ON posts.user_id = (%s)"