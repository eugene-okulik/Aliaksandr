def test_login_form_conf_pass_attribute_empty(login_page):
    login_page.open_registration_page()
    login_page.fill_login_form('Alex', 'Traf', 'Soulsesiz1@rambler.ru', 'Galuzoid@1', '')
    login_page.submit_registration_form()
    login_page.verify_confirm_password_error_is_displayed()


def test_login_form_first_name_invalid(login_page):
    login_page.open_registration_page()
    login_page.fill_login_form('Alex@134', 'Traf', 'Soulsesiz1@rambler.ru', 'Galuzoid@1', 'Galuzoid@1')
    login_page.submit_registration_form()
    login_page.verify_validation_message_is_displayed()


def test_login_form_last_name_invalid(login_page):
    login_page.open_registration_page()
    login_page.fill_login_form('Alex', 'Traf@123', 'Soulsesiz1@rambler.ru', 'Galuzoid@1', 'Galuzoid@1')
    login_page.submit_registration_form()
    login_page.verify_validation_message_is_displayed()
