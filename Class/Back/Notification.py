from Class.Back.Db import Db

class Notification:
    def __init__(self):
        self.db = Db(host='localhost', user='root', password='root', database='db_discord')

    def set_messages_counter(self, user_id, channel_id, messages_counter):
        query = "INSERT INTO notification (user_id, channel_id, messages_counter) VALUES (%s, %s, %s)"
        value = (user_id, channel_id, messages_counter)
        self.db.execute(query, value)

    def update_messages_counter(self, user_id, channel_id, messages_counter):
        query = "UPDATE notification SET messages_counter = %s WHERE user_id = %s AND channel_id = %s"
        value = (messages_counter, user_id, channel_id)
        self.db.execute(query, value)
    
    def add_messages_counter(self, user_id, channel_id):
        query = "UPDATE notification SET messages_counter = messages_counter + 1 WHERE user_id = %s AND channel_id = %s"
        value = (user_id, channel_id)
        self.db.execute(query, value)

    def get_messages_counter(self, user_id, channel_id):
        query = "SELECT messages_counter FROM notification WHERE user_id = %s AND channel_id = %s"
        value = (user_id, channel_id)
        return self.db.fetch(query, value)

    def get_notifications(self, user_id, cnannel_id):
        counter_id = self.set_messages_counter(user_id, cnannel_id)
        query = "SELECT id FROM posts WHERE id > %s AND id_affiliate_channel = %s AND user_id != %s AND disconnection = 0 AND connection = 0"
        value = (counter_id, user_id)
        return self.db.fetch(query, value)