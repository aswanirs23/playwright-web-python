from src.pageObjects.login_PO import LoginPO
from src.utils.ui_actions import UIActions
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class LoginPageActions:
    def __init__(self, page):
        self.page_objects = LoginPO(page)
        self.ui_actions = UIActions(page)
    
    def enter_username(self, username):
        if username:
            username_locator = self.page_objects.txt_username()
            self.ui_actions.enter_text(username_locator, username)
            logger.info(f"Entered username: {username}")
    
    def enter_password(self, password):
        if password:
            password_locator = self.page_objects.txt_password()
            self.ui_actions.enter_text(password_locator, password)
            logger.info("Entered password (hidden for security)")
    
    def click_login_button(self):
        login_button_locator = self.page_objects.btn_login()
        self.ui_actions.click_element(login_button_locator)
        logger.info("Clicked login button")
        
    def get_error_message(self):
        error_message_locator = self.page_objects.error_message()
        return error_message_locator.text_content()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
