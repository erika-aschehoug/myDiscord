from Class.Back.Db import Db

class Post:
    def __init__(self):
        self.db = Db(host='localhost', user='root', password='root', database='db_discord')

    def send_post(self, user_id, content, affiliate_chanel_id, date, connection=False, disconnection = False):
        query = "INSERT INTO posts (body, user_id, id_affiliate_chanel, created_at, connection, disconnection) VALUES (%s, %s, %s, now(), %s, %s)"
        value = (content, user_id, affiliate_chanel_id, connection, disconnection)
        self.db.execute(query, value)

    def get_post(self, id_room):
        query = "SELECT * FROM posts WHERE id_affiliate_chanel = %s"
        value = (id_room,)
        return self.db.fetch(query, value)
    
    def get_post_by_id(self, id_post):
        query = "SELECT * FROM posts WHERE id = %s"
        value = (id_post,)
        return self.db.fetch(query, value)
    
    def get_author(self, post_user_id):
        query = "SELECT user_first_name FROM users INNER JOIN posts ON users.id = (%s)"
        value = (post_user_id,)
        author = self.db.fetch(query, value)
        return author[0][0]    
    
