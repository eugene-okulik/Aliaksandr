from time import sleep

from playwright.async_api import BrowserContext
from playwright.sync_api import Page, expect, Dialog


def test_alert(page: Page):
    page.on("dialog", lambda dialog: dialog.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm#')
    page.locator("a.a-button:has-text('Click')").click()
    result_text = page.locator("p.result-text#result-text")
    expect(result_text).to_have_text("Ok")


def test_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_button = page.locator("#new-page-button")
    with context.expect_page() as new_page_event:
        click_button.click()

    new_page_2 = new_page_event.value
    new_page_2.wait_for_load_state()

    result_text = new_page_2.locator("#result-text")
    expect(result_text).to_have_text("I am a new page in a new tab")

    page.bring_to_front()
    expect(click_button).to_be_visible()
    expect(click_button).to_be_enabled()


def test_waiting_color_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_change_button = page.locator("#colorChange")
    expect(color_change_button).to_have_attribute("class", "mt-4 text-danger btn btn-primary")
    color_change_button.click()
    sleep(3)
