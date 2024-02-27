from Class.Back.Connection import Connection
from Class.Back.User import User
from Class.Back.Post import Post

class Model:
    def __init__(self):
        
        self.connection = Connection()
        self.user = User()
        self.post = Post()

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
    def send_post(self, user_id, content, affiliate_chanel_id):
        return self.post.send_post(user_id, content, affiliate_chanel_id)
    
    def get_post(self, id_room):
        return self.post.get_post(id_room)
        
    