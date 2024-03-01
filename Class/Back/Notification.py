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

    def get_messages_counter(self, user_id, channel_id):
        query = "SELECT messages_counter FROM notification WHERE user_id = %s AND channel_id = %s"
        value = (user_id, channel_id)
        result = self.db.fetch(query, value)
        return result[0][0]

    def get_new_messages(self, user_id, channel_id):
        counter_id = self.get_messages_counter(user_id, channel_id)
        query = "SELECT id FROM posts WHERE id > %s AND id_affiliate_chanel = %s AND user_id != %s AND disconnection = 0 AND connection = 0"
        value = (counter_id, channel_id, user_id)
        result = self.db.fetch(query, value)
        return result