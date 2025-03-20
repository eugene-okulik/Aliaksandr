import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check status code is correct')
    def check_status_code_is_correct(self):
        assert self.response.status_code in [200, 204]
