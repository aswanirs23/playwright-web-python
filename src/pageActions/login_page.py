from src.pageObjects.login_PO import LoginPO
from src.utils.ui_actions import UIActions

class LoginPageActions:
    def __init__(self, page):
        self.page_objects = LoginPO(page)
        self.ui_actions = UIActions(page)
    
    def enter_username(self, username):
        username_locator = self.page_objects.txt_username()
        self.ui_actions.enter_text(username_locator, username)
        
        
    def enter_password(self, password):
        password_locator = self.page_objects.txt_password()
        self.ui_actions.enter_text(password_locator, password)
        
    
    def click_login_button(self):
        login_button_locator = self.page_objects.btn_login()
        self.ui_actions.click_element(login_button_locator)
