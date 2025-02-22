from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class UIActions:
    def __init__(self, page: Page):
        self.page = page

    def click_element(self, element, timeout=5000):
        try:
            element.wait_for(state="visible", timeout=timeout)
            element.click()
        except PlaywrightTimeoutError:
            print(f"Element not found: {element}")

    def enter_text(self, element, text, timeout=5000):
        try:
            element.wait_for(state="visible", timeout=timeout)
            element.fill(text)
        except PlaywrightTimeoutError:
            print(f"Element not found for text entry: {element}")

