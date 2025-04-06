import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time


@pytest.fixture()
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.maximize_window()
    yield chrom_driver
    chrom_driver.quit()


def test_new_tab(driver):
    driver.get('https://www.demoblaze.com/index.html')
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="Samsung galaxy s6"]')))
    element.send_keys(Keys.CONTROL, Keys.ENTER)
    actual_result = element.text
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[@onclick="addToCart(1)"]'))).click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, 'cartur').click()
    expected_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//tr/td[text()="Samsung galaxy s6"]'))).text
    assert actual_result == expected_result, f"ERROR: expect '{expected_result}', actual '{actual_result}'"


def test_hower_over(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    bag = driver.find_element(By.XPATH, '//img[@class="product-image-photo" and @alt="Push It Messenger Bag"]')
    expected_result = bag.get_attribute("alt")
    action = ActionChains(driver)
    action.move_to_element(bag)
    action.perform()
    button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(@class, "tocompare")]')))
    button.click()
    compare_products = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="Push It Messenger Bag"]')))
    actual_result = compare_products.text
    assert actual_result == expected_result, f"ERROR: expect '{expected_result}', actual '{actual_result}'"
