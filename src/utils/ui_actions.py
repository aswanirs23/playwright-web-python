
"""
UI Actions Utility
This class provides common UI interaction methods used across the application.
It handles basic Playwright interactions with built-in error handling and logging.

"""
from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from src.utils.logger import setup_logger

logger = setup_logger()

class UIActions:
    def __init__(self, page: Page):
        self.page = page

    def click_element(self, element, timeout=5000):
        try:
            element.wait_for(state="visible", timeout=timeout)
            element.click()
        except PlaywrightTimeoutError:
            logger.warning(f"Element not found: {element}") 

    def enter_text(self, element, text, timeout=5000):
        try:
            element.wait_for(state="visible", timeout=timeout)
            element.fill(text)
        except PlaywrightTimeoutError:
            logger.warning(f"Element not found for text entry: {element}")
            
    def get_text_content(self, element):
        try:
            element.wait_for(state="visible")
            return element.text_content()
        except PlaywrightTimeoutError:
            logger.warning(f"Element not found for getting text content: {element}")  # Use logger instead of print
            return None
    
    def click_dropdown_option(self, dropdown, option, timeout=5000):
        try:
            dropdown.wait_for(state="visible", timeout=timeout)
            dropdown.click()
            dropdown.select_option(option)
        except PlaywrightTimeoutError:
            logger.warning(f"Dropdown element not found or option '{option}' not available")

