from .base_page import BasePage
from .locators import login_locators as log_loc
from playwright.sync_api import expect


class UserLogin(BasePage):
    page_url = '/customer/account/create/'

    def open_registration_page(self):
        self.open_page()

    def fill_login_form(self, first_name, last_name, email, password, confirm_password):
        self.page.locator(log_loc.FIRST_NAME_INPUT).fill(first_name)
        self.page.locator(log_loc.LAST_NAME_INPUT).fill(last_name)
        self.page.locator(log_loc.EMAIL_INPUT).fill(email)
        self.page.locator(log_loc.PASSWORD_INPUT).fill(password)
        self.page.locator(log_loc.CONFIRM_PASSWORD_INPUT).fill(confirm_password)

    def submit_registration_form(self):
        self.page.locator(log_loc.CREATE_ACCOUNT_BUTTON).click()

    def verify_confirm_password_error_is_displayed(self):
        expect(self.page.locator(log_loc.CONFIRM_PASSWORD_ERROR)).to_be_visible()

    def verify_validation_message_is_displayed(self):
        self.page.wait_for_selector(log_loc.VALIDATION_MESSAGE)
