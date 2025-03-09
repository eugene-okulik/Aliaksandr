import requests
import pytest


@pytest.fixture()
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
    assert response_post.status_code == 200, 'Status code is incorrect'
    post_id = response_post.json()['id']
    yield post_id
    print('deleting the object')
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


@pytest.fixture(scope='session')
def header():
    print('Start testing')
    yield
    print('Complete testing')


@pytest.mark.medium
def test_get(post,header):
    response_get = requests.get(f'http://167.172.172.115:52353/object/{post}')
    assert response_get.json(), "Response JSON is empty or null."
    print(response_get.json())

@pytest.mark.critical
def test_put(post):
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
        f'http://167.172.172.115:52353/object/{post}',
        json=put_body,
        headers=put_headers
    ).json()
    assert response_put['name'] == "AT_object"
    print(response_put)

@pytest.mark.medium
def test_patch(post):
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
        f'http://167.172.172.115:52353/object/{post}',
        json=patch_body,
        headers=patch_headers
    ).json()
    assert "id" in response_patch, "Response does not contain 'id'"
    assert "data" in response_patch, "Response does not contain 'data'"
    print(response_patch)


def test_post():  # test w/o fixture
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


object_id = test_post()


def delete(object_id):
    print('deleting the object')
    response_delete = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    print(response_delete.text)
