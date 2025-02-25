"""
Pytest Configuration and Fixtures
This module contains the core test configuration and shared fixtures.

"""

import pytest
from playwright.sync_api import sync_playwright
from src.pageActions.login_page import LoginPageActions
from config import username, password, login_url
from src.utils.logger import setup_logger 

logger = setup_logger()

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
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    
@pytest.fixture
def login_fixture(page):
    login_page = LoginPageActions(page)
    page.goto(login_url)
    return login_page

@pytest.fixture
def logged_in_user(page):
    login_page = LoginPageActions(page)
    page.goto(login_url)
    login_page.login(username, password)  
    return page