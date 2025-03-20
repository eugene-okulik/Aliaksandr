import requests
import allure
from .endpoints_1 import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Update a object')
    def update_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        return self.response
