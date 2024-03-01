from Class.Front.view import View
from Class.Back.model import Model

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()
        
    def user_info(self, info):
        self.user_ID = info[0][0]
        self.username = info[0][1]
        self.user_firstname = info[0][2]
        self.user_mail = info[0][3]

    def get_user_info(self):
        return self.user_ID, self.username, self.user_firstname, self.user_mail
    
    def reset_user_info(self):
        self.user_ID = None
        self.username = None
        self.user_firstname = None
        self.user_mail = None

    # Methof of login_page
    def get_login_variables(self, mail, password):
        acces = self.model.login(mail, password)
        if acces:
            info = self.model.user_info(mail)
            self.user_info(info)
            self.view.show_home_page()
        else:
            self.view.set_error_login()


    # Method of create_account_page
    def get_create_account_variables(self, name, firstname, email, password):
        self.model.create_account(name, firstname, email, password)
        self.view.show_login_page()

    # Method of text_chat_page
    def send_post(self):
        content = self.view.message
        chanel = self.view.chanel
        connection = self.view.connection
        disconnection = self.view.disconnection
        date = self.view.date
        self.model.send_post(self.user_ID, content, chanel, date, connection, disconnection)

    def get_post(self, id_room):
        return self.model.get_post(id_room)
    
    def get_all_users(self):
        return self.model.get_all_users()
    
    def get_author(self, posts_user_id):
        return self.model.get_author(posts_user_id)
    
    # Method for notification
    def update_messages_counter(self, user_id, channel_id, messages_counter):
        return self.model.update_messages_counter(user_id, channel_id, messages_counter)
    
    def get_new_messages(self, user_id, channel_id):    
        return self.model.get_new_messages(user_id, channel_id)
    
    # Method for room management
    def permission(self, user_id, roomId):
        return self.model.permission(user_id, roomId)
    
    def add_user(self, id, roomId):   
        return self.model.add_user(id, roomId)
    
    def remove_user(self, id, roomId):
        return self.model.remove_user(id, roomId)
    
if __name__ == "__main__":
    controller = Controller()
    controller.main()