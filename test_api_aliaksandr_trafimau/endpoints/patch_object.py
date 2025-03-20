import requests
import allure
from .endpoints_1 import Endpoint


class PatchObject(Endpoint):

    @allure.step('Patch object')
    def patch_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        return self.response

    @allure.step('Check id in response')
    def check_id_in_response(self):
        response_patch = self.response.json()
        assert "id" in response_patch, "Response does not contain 'id'"

    @allure.step('Check data in response')
    def check_data_in_response(self):
        response_patch = self.response.json()
        assert "data" in response_patch, "Response does not contain 'data'"

    @allure.step('Check response integrity')
    def check_response_integrity(self):
        response_patch = self.response.json()
        assert "data" in response_patch, "Response does not contain 'datas'"
        