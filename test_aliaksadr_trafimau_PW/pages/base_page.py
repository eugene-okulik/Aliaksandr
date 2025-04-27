from playwright.sync_api import Page


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f'{self.base_url}{self.page_url}')

    def find(self, locator):
        return self.page.locator(locator)

    def find_all(self, locator):
        return self.page.locator(locator)
