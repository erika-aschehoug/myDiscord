from Class.Back.Connection import Connection
from Class.Back.User import User
from Class.Back.Post import Post
from Class.Back.Notification import Notification
from Class.Back.Room import Room

class Model:
    def __init__(self):
        
        self.connection = Connection()
        self.user = User()
        self.post = Post()
        self.notification = Notification()
        self.room = Room()

    # This method is used to login the user
    def login(self, mail, password):
        return self.connection.login(mail, password)
    
    # This method is used to create an account
    def create_account(self, name, firstname, email, password):
        return self.user.create_account(name, firstname, email, password)
    
    # This method is used to get the user info
    def user_info(self, info):
        return self.user.get_user(info)
    
    # method for public text chat
    def send_post(self, user_id, content, affiliate_chanel_id, date, connection, disconnection):
        return self.post.send_post(user_id, content, affiliate_chanel_id, date, connection, disconnection)
    
    def get_post(self, id_room):
        return self.post.get_post(id_room)
            
    def get_all_users(self):
        return self.user.get_all_users()
    
    def get_author(self, posts_user_id):
        return self.post.get_author(posts_user_id)
    
    # Method for notification
    def update_messages_counter(self, user_id, channel_id, messages_counter):
        return self.notification.update_messages_counter(user_id, channel_id, messages_counter)
    
    def get_new_messages(self, user_id, channel_id):
        return self.notification.get_new_messages(user_id, channel_id)
    
    # Method for room management
    def permission(self,user_id, roomId):
        return self.room.permission(user_id, roomId)
    
    def add_user(self, id, roomId):
        return self.room.add_user(id, roomId)
    
    def remove_user(self, id, roomId):
        return self.room.remove_user(id, roomId)
    
    def get_users(self, roomId):
        return self.room.get_users(roomId)
    
    def get_admin(self, roomId):
        return self.room.get_admin(roomId)
    
    def add_admin(self, roomId, userId):
        return self.room.add_admin(roomId, userId)
    
    def update_add_admin(self, roomId, userId):
        return self.room.update_add_admin(roomId, userId)
    
    def update_remove_admin(self, roomId, userId):
        return self.room.update_remove_admin(roomId, userId)
    

    