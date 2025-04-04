import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.maximize_window()
    yield chrom_driver
    chrom_driver.quit()


def test_text_input(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_text = '123ADdf'
    search_input = driver.find_element(By.ID, 'id_text_string')
    search_input.send_keys(input_text)
    search_input.send_keys(Keys.RETURN)

    search_result_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'result-text'))
    )
    result_text = search_result_input.text
    print(result_text)
    assert input_text == result_text, f"ERROR expected result: {input_text}, actual result: {result_text}"


def test_submit_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = 'Alex'
    last_name = 'Traf'
    email = 'alextraf@traf.com'
    mobile_number = '1222231217'
    current_address = 'Bak st. 16-22-3'
    subject = 'English'
    state = 'Haryana'
    city = 'Karnal'
    search_first_name = driver.find_element(By.ID, "firstName")
    search_first_name.send_keys(first_name)
    search_last_name = driver.find_element(By.ID, "lastName")
    search_last_name.send_keys(last_name)
    search_email = driver.find_element(By.ID, "userEmail")
    search_email.send_keys(email)
    search_mobile_number = driver.find_element(By.ID, "userNumber")
    search_mobile_number.send_keys(mobile_number)
    search_current_address = driver.find_element(By.ID, "currentAddress")
    search_current_address.send_keys(current_address)
    gender = driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]')
    gender.click()
    open_calendar = driver.find_element(By.ID, "dateOfBirthInput")
    open_calendar.click()
    open_month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    open_month.click()
    search_month = driver.find_element(By.XPATH, '//option[text()="June"]')
    search_month.click()
    open_year = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    open_year.click()
    search_year = driver.find_element(By.XPATH, '//option[text()="2025"]')
    search_year.click()
    driver.find_element(By.CSS_SELECTOR, 'div.react-datepicker__day.react-datepicker__day--023').click()
    search_subject = driver.find_element(By.ID, 'subjectsInput')
    search_subject.send_keys(subject)
    search_subject.send_keys(Keys.ENTER)
    search_hobbies = driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]')
    search_hobbies.click()
    search_state = driver.find_element(By.CSS_SELECTOR, 'input#react-select-3-input')
    search_state.send_keys(state)
    search_state.send_keys(Keys.ENTER)
    search_city = driver.find_element(By.ID, 'react-select-4-input')
    search_city.send_keys(city)
    search_city.send_keys(Keys.ENTER)
    search_submit = driver.find_element(By.ID, 'submit')
    search_submit.click()


def test_submit_value(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    search_language = driver.find_element(By.ID, 'id_choose_language')
    search_language.click()
    search_value = driver.find_element(By.XPATH, '//option[text()="Python"]')
    search_value.click()
    expected_value = search_value.text
    search_submit = driver.find_element(By.ID, 'submit-id-submit')
    search_submit.click()
    search_value_field = driver.find_element(By.ID, 'result-text')
    actual_value = search_value_field.text
    print(actual_value)
    assert actual_value == expected_value, f"ERROR: expect '{expected_value}', actual '{actual_value}'"


def test_loading(driver):
    expected_value = 'Hello World!'
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    search_start = driver.find_element(By.XPATH, '//button[text()="Start"]')
    search_start.click()
    search_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h4[text()="Hello World!"]')))
    actual_result = search_result.text
    assert actual_result == expected_value, f"ERROR: expect '{expected_value}', actual '{actual_result}'"
