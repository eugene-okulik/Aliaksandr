import requests
import allure
from .endpoints_1 import Endpoint


class DeleteObject(Endpoint):
    url = 'http://167.172.172.115:52353/object'
    response = None

    @allure.step('Delete object')
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else {'Content-Type': 'application/json'}
        self.response = requests.delete(
            f"{self.url}/{object_id}",
            headers=headers
        )
        return self.response
