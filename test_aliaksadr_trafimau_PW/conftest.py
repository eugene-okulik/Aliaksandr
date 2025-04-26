import pytest
from playwright.sync_api import sync_playwright
from test_aliaksadr_trafimau_PW.pages.user_login import UserLogin
from test_aliaksadr_trafimau_PW.pages.sale_page import SalePage
from test_aliaksadr_trafimau_PW.pages.eco_frendly_page import CategoryPage


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture()
def login_page(page):
    return UserLogin(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def category_page(page):
    return CategoryPage(page)
