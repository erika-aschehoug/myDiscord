from Class.Back.Db import Db
from Class.Back.Session import Session

class Room:
    def __init__(self):
        self.db = Db(host="localhost", user="root", password="root", database="db_discord")

    def permission(self,user_id, roomId):
        query = "SELECT * FROM permissions WHERE id_affiliate_user = %s"
        values = (user_id,)
        permissions = self.db.fetch(query, values)
        try:
            if permissions[0][2] == roomId:
                return True
            else:
                return False
        except:
            return False
    
    def add_user(self, id, roomId):
        query = "INSERT INTO permissions (id_affiliate_user, id_affiliate_canal, admin) VALUES (%s, %s, %s)"
        values = (id, roomId, 0)
        self.db.execute(query, values)

    def remove_user(self, id, roomId):
        query = "DELETE FROM permissions WHERE id_affiliate_user = %s AND id_affiliate_canal = %s"
        values = (id, roomId)
        self.db.execute(query, values)

    def get_users(self, roomId):
        query = "SELECT users.id, users.username, users.user_first_name, users.mail FROM users INNER JOIN permissions ON users.id = permissions.id_affiliate_user WHERE id_affiliate_canal = %s"
        values = (roomId,)
        return self.db.fetch(query, values)
    
    def update_add_admin(self, id, roomId):
        query = "UPDATE permissions SET admin = 1 WHERE id_affiliate_user = %s AND id_affiliate_canal = %s"
        values = (id, roomId)
        self.db.execute(query, values)

    def update_remove_admin(self, id, roomId):
        query = "UPDATE permissions SET admin = 0 WHERE id_affiliate_user = %s AND id_affiliate_canal = %s"
        values = (id, roomId)
        self.db.execute(query, values)
    
    def add_admin(self, id, roomId):
        query = "INSERT INTO permissions (id_affiliate_user, id_affiliate_canal, admin) VALUES (%s, %s, %s)"
        values = (id, roomId, 1)
        self.db.execute(query, values)

    def get_admin(self, roomId):
        query = "SELECT users.id FROM users INNER JOIN permissions ON users.id = permissions.id_affiliate_user WHERE id_affiliate_canal = %s AND admin = 1"
        values = (roomId,)
        return self.db.fetch(query, values)
