from playwright.sync_api import Page


class LoginPO:
    def __init__(self, page: Page):
        self.page = page

    def txt_username(self):
        return self.page.get_by_placeholder("Username")
    
    def txt_password(self):
        return self.page.get_by_placeholder("Password")
    
    def btn_login(self):
        return self.page.get_by_role("button", name="LOGIN")
    
    def error_message(self):
        return self.page.locator("[data-test=\"error\"]")
        