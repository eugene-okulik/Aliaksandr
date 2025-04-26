from .base_page import BasePage
from .locators import sale_page_locator as sale_loc
from playwright.sync_api import expect


class SalePage(BasePage):
    page_url = '/sale.html'

    def click_women_category(self):
        self.page.locator(sale_loc.WOMEN_SALE_IMAGE).click()

    def click_men_category(self):
        self.page.locator(sale_loc.MEN_SALE_IMAGE).click()

    def verify_page_title(self, expected_title):
        title_locator = f'//span[@class="base" and @data-ui-id="page-title-wrapper" and text()="{expected_title}"]'
        expect(self.page.locator(f"xpath={title_locator}")).to_be_visible()

    def hover_on_training_menu(self):
        self.page.locator(sale_loc.TRAINING_MENU).hover()

    def select_training_option(self):
        self.page.locator(sale_loc.TRAINING_OPTION).click()

    def verify_training_video_is_displayed(self):
        expect(self.page.locator(sale_loc.TRAINING_VIDEO)).to_be_visible()
