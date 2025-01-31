from playwright.sync_api import Page

class UIActions:
    def __init__(self, page: Page):
        self.page = page

    def click_element(self, element):
        element.click()

    def enter_text(self, element, text):
        element.click()
        element.fill(text)
