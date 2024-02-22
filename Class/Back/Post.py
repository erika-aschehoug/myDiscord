from Class.Back.Db import Db

class Post:
    def __init__(self):
        self.db = Db(host='localhost', user='root', password='root', database='db_discord')

    def send_post(self, user_id, content, affiliate_chanel_id):
        query = "INSERT INTO posts (body, user_id, id_affiliate_chanel) VALUES (%s, %s, %s)"
        value = (content, user_id, affiliate_chanel_id)
        self.db.execute(query, value)

    def get_post(self, id_room):
        query = "SELECT * FROM posts WHERE id_affiliate_chanel = %s"
        value = (id_room,)
        return self.db.fetch(query, value)
    
    def get_post_by_id(self, id_post):
        query = "SELECT * FROM posts WHERE id = %s"
        value = (id_post,)
        return self.db.fetch(query, value)
    
    