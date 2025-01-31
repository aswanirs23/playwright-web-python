import pytest
from playwright.sync_api import sync_playwright
from src.pageActions.login_page import LoginPageActions

def test_login(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPageActions(page)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()