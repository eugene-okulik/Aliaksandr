import requests


def get():
    response_get = requests.get('http://167.172.172.115:52353/object')
    assert response_get.json(), "Response JSON is empty or null."
    print(response_get.json())


get()


def post():
    post_body = {
        "data": {
            "aat1": "66669844",
            "at1": "45668944",
            "color1": "white6894",
            "size1": "big268944"
        },
        "id": "420",
        "name": "First3 object233689"
    }
    post_headers = {'Content-Type': 'application/json'}

    response_post = requests.post(
        'http://167.172.172.115:52353/object',
        json=post_body,
        headers=post_headers
    )
    assert response_post.status_code == 200, 'Status code is incorrect'
    print(response_post.json())
    return response_post.json()['id']


object_id = post()


def delete(object_id):
    response_delete = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(response_delete.text)


delete(object_id)


def post():
    post_body = {
        "data": {
            "aat1": "66669844",
            "at1": "45668944",
            "color1": "white6894",
            "size1": "big268944"
        },
        "id": "420",
        "name": "First3 object233689"
    }
    post_headers = {'Content-Type': 'application/json'}

    response_post = requests.post(
        'http://167.172.172.115:52353/object',
        json=post_body,
        headers=post_headers
    )
    return response_post.json()['id']


def put():
    put_body = {
        "data": {
            "AT": "111",
            "AT_12": "GTS_334",
            "AT_AT": "1230",
            "size_AT": "AT@1915"
        },
        "id": "420",
        "name": "AT_object"
    }
    put_headers = {'Content-Type': 'application/json'}

    response_put = requests.put(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=put_body,
        headers=put_headers
    ).json()
    assert response_put['name'] == "AT_object"
    print(response_put)


def delete(object_id):
    response_delete = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(response_delete.text)


post_id = post()
put()
delete(post_id)


def post():
    post_body = {
        "data": {
            "aat1": "66669844",
            "at1": "45668944",
            "color1": "white6894",
            "size1": "big268944"
        },
        "id": "420",
        "name": "First3 object233689"
    }
    post_headers = {'Content-Type': 'application/json'}

    response_post = requests.post(
        'http://167.172.172.115:52353/object',
        json=post_body,
        headers=post_headers
    )
    print(response_post.json())
    return response_post.json()['id']


def patch():
    patch_body = {
        "data": {
            "AT": "111_p",
            "AT_12": "GTS_334_p",
            "AT_AT": "1230-P",
            "size_AT": "AT@1915-p"
        },
    }
    patch_headers = {'Content-Typ': 'application/json'}

    response_patch = requests.patch(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=patch_body,
        headers=patch_headers
    ).json()
    assert "id" in response_patch, "Response does not contain 'id'"
    assert "data" in response_patch, "Response does not contain 'data'"
    print(response_patch)


def delete(object_id):
    response_delete = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response_delete.status_code == 200, 'Status code is incorrect'
    print(response_delete.text)


object_id = post()
patch()
delete(object_id)
