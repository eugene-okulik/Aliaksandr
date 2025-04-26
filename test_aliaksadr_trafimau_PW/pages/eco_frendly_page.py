from .base_page import BasePage
from .locators import eco_frendly_page_locators as eco_log
from playwright.sync_api import expect


class CategoryPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def open_main_category_men(self):
        self.page.locator(eco_log.MAIN_CATEGORY).hover()

    def select_subcategory(self):
        self.open_main_category_men()
        self.page.locator(eco_log.SUB_CATEGORY).hover()
        self.page.locator(eco_log.SUB_SUB_CATEGORY).click()

    def verify_image_is_displayed(self):
        expect(self.page.locator(eco_log.PRODUCT_IMAGE)).to_be_visible()

    def sort_products_by_price(self):
        dropdown = self.page.locator(eco_log.SORT_DROPDOWN).nth(0)
        dropdown.click()
        self.page.select_option(eco_log.SORT_DROPDOWN, value="price")

    def verify_selected_sorting_option(self):
        dropdown = self.page.locator(eco_log.SORT_DROPDOWN).nth(0)
        expect(dropdown).to_have_value("price")

    def select_training_element(self):
        self.page.locator(eco_log.TRAINING_CATEGORY).hover()

    def select_video_option(self):
        self.page.locator(eco_log.TRAINING_OPTION).click()

    def verify_training_video_message_is_displayed(self):
        expect(self.page.locator(eco_log.TRAINING_VIDEO_MESSAGE)).to_be_visible()
