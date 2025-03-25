import requests
import allure
from .endpoints_1 import Endpoint


class CreatePost(Endpoint):

    @allure.step('Create object')
    def new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )

        self.json = self.response.json()
        return self.response

    @allure.step('Check required keys in response')
    def check_response_contains_keys(self, *keys):
        missing_keys = [key for key in keys if key not in self.json]
        assert not missing_keys, f"В ответе отсутствуют обязательные ключи: {missing_keys}"
