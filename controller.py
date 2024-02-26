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

    # Methof of login_page
    def get_login_variables(self, mail, password):
        acces = self.model.login(mail, password)
        if acces:
            info = self.model.user_info(mail)
            self.user_info(info)
            self.view.show_start_page()
        else:
            self.view.show_login_page()


    # Method of create_account_page
    def get_create_account_variables(self, name, firstname, email, password):
        self.model.create_account(name, firstname, email, password)
        self.view.show_login_page()

if __name__ == "__main__":
    controller = Controller()
    controller.main()