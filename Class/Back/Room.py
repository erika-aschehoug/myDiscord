from Db import Db
from Session import Session

class Room:
    def __init__(self):
        self.db = Db(host="localhost", user="root", password="root", database="db_discord")

    def persmissions(self, id, roomId):
        query = "SELECT * FROM permissions WHERE id_affiliate_user = %s"
        values = (id,)
        permissions = self.db.fetch(query, values)
        for permission in permissions:
            if permission["id_affiliate_canal"] == roomId:
                return True
        return False
    
    def add_user(self, id, roomId, admin = False):
        query = "INSERT INTO permissions (id_affiliate_user, id_affiliate_canal, admin) VALUES (%s, %s, %s)"
        values = (id, roomId, admin)
        self.db.execute(query, values)

    def remove_user(self, id, roomId):
        query = "DELETE FROM permissions WHERE id_affiliate_user = %s AND id_affiliate_canal = %s"
        values = (id, roomId)
        self.db.execute(query, values)

    def get_users(self, roomId):
        query = "SELECT * FROM permissions WHERE id_affiliate_canal = %s"
        values = (roomId,)
        return self.db.fetch(query, values)
    
    def get_chat_rooms(self):
        query = "SELECT * FROM chat_room WERE canal_type = text"
        return self.db.fetch(query)
    
    def get_voice_rooms(self):
        query = "SELECT * FROM chat_room WERE canal_type = voice"
        return self.db.fetch(query)
    
    def access_room(self, roomId):
        if Session.get_current_user() in self.get_users(roomId) or self.get_users(roomId) == []:
            return True