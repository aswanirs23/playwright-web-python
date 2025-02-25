from src.pageObjects.login_PO import LoginPO
from src.utils.ui_actions import UIActions

class LoginPageActions(LoginPO,UIActions):

    def enter_username(self, username=""):
        username_locator = self.txt_username()
        self.enter_text(username_locator, username)
    
    def enter_password(self, password=""):
        password_locator = self.txt_password()
        self.enter_text(password_locator, password)
    
    def click_login_button(self):
        login_button_locator = self.btn_login()
        self.click_element(login_button_locator)
        
    def get_error_message(self):
        error_message_locator = self.error_message()
        return self.get_text_content(error_message_locator)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
