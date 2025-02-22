import pytest
from playwright.sync_api import sync_playwright
from src.pageActions.login_page import LoginPageActions
from config import username, password, login_url
from src.utils.logger import setup_logger 

logger = setup_logger(__name__)

@pytest.fixture(scope="session")
def browser():
    logger.info("Launching browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        logger.info("Closing browser")
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    logger.info("Creating new browser context and page")
    context = browser.new_context()
    page = context.new_page()
    yield page
    logger.info("Closing page and context")
    page.close()
    context.close()
    
@pytest.fixture
def login_fixture(page):
    logger.info("Navigating to login page")
    login_page = LoginPageActions(page)
    page.goto(login_url)
    return login_page

@pytest.fixture
def logged_in_user(page):
    logger.info("Logging in user")
    login_page = LoginPageActions(page)
    page.goto(login_url)
    login_page.login(username, password)  
    return page