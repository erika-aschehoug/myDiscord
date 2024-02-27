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

    # Method of public_text_chat_page
    def send_post(self):
        print(self.user_ID)
        content = self.view.message
        print(content)
        chanel = self.view.chanel
        print(chanel)
        self.model.send_post(self.user_ID, content, chanel)

if __name__ == "__main__":
    controller = Controller()
    controller.main()