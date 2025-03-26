from locust import task, HttpUser, between


class Objects(HttpUser):
    created_object_id = None
    wait_time = between(1, 3)

    @task
    def get_object(self):
        response = self.client.get(
            '/object',
            headers={'Content-Type': 'application/json'}
        )
        print(f"GET запрос выполнен. Статус: {response.status_code}")

    @task
    def workflow(self):
        response = self.client.post(
            '/object',
            headers={'Content-Type': 'application/json'},
            json={
                "data": {
                    "aat1": "66669844",
                    "aatt1": "45668944",
                    "color1": "white6894",
                    "size1": "big268944"
                },
                "name": "First3 object233689"
            }
        )
        self.created_object_id = response.json().get("id")
        print(f"Пользователь {id(self)} создал объект с ID: {self.created_object_id}")

        response = self.client.put(
            f'/object/{self.created_object_id}',
            headers={'Content-Type': 'application/json'},
            json={
                "data": {
                    "aat1": "updated_value",
                    "aatt1": "updated_value",
                    "color1": "red",
                    "size1": "small"
                },
                "name": "Updated object name"
            }
        )
        print(f"Пользователь {id(self)} обновил объект с ID: {self.created_object_id}. Статус: {response.status_code}")

        response = self.client.patch(
            f'/object/{self.created_object_id}',
            headers={'Content-Type': 'application/json'},
            json={
                "data": {
                    "color1": "blue",
                },
                "name": "Partially updated object name"
            }
        )
        print(f"Пользователь {id(self)} частично обновил объект с ID: {self.created_object_id}."
              f" Статус: {response.status_code}")

        response = self.client.delete(
            f'/object/{self.created_object_id}',
            headers={'Content-Type': 'application/json'}
        )
        print(f"Пользователь {id(self)} удалил объект с ID: {self.created_object_id}. Статус: {response.status_code}")
