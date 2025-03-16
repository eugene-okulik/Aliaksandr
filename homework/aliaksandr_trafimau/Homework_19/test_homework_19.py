import requests
import pytest


@pytest.fixture(autouse=True)
def test_lifecycle_messages():
    print("Before test")
    yield
    print("After test")


@pytest.fixture()
def created_object():
    post_body = {
        "data": {
            "aat1": "66669844",
            "aatt1": "45668944",
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
    print("Create response:", response_post.json())
    assert response_post.status_code == 200, 'Status code is incorrect'

    post_id = response_post.json()['id']

    yield post_id

    print('Checking if the object still exists for deletion.')
    get_response = requests.get(f'http://167.172.172.115:52353/object/{post_id}')

    if get_response.status_code == 200:
        print('Deleting the object.')
        delete_response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')

        if delete_response.status_code == 200:
            print("Object deleted successfully.")
        else:
            print("Failed to delete object.")

    else:
        print("Object does not exist, skipping deletion.")


@pytest.fixture(scope='session')
def test_session():
    print('Start of testing session')
    yield
    print('End of testing session')


@pytest.mark.critical
def test_add_object(test_session):
    post_body = {
        "data": {
            "aat1": "1111",
            "aatt1": "33322",
            "color1": "blue",
            "size1": "small"
        },
        "id": "999",
        "name": "New Object"
    }
    post_headers = {'Content-Type': 'application/json'}

    response_post = requests.post(
        'http://167.172.172.115:52353/object',
        json=post_body,
        headers=post_headers
    )
    response_json = response_post.json()
    print("POST response:", response_json)

    assert response_post.status_code == 200, 'Failed to create object'
    assert response_json["name"] == "New Object", "Object name mismatch"

    delete_response = requests.delete(f'http://167.172.172.115:52353/object/{response_json["id"]}')
    assert delete_response.status_code == 200, "Failed to delete created object"
    print("Object created and deleted successfully.")


@pytest.mark.critical
def test_delete_object(created_object):
    delete_response = requests.delete(f'http://167.172.172.115:52353/object/{created_object}')
    assert delete_response.status_code == 200, 'Failed to delete object'
    print("Object deleted successfully.")

    response_get = requests.get(f'http://167.172.172.115:52353/object/{created_object}')
    assert response_get.status_code == 404, 'Object still exists after deletion'
    print("Verified that object was deleted.")


@pytest.mark.medium
def test_get_object(created_object):
    response_get = requests.get(f'http://167.172.172.115:52353/object/{created_object}')
    assert response_get.status_code == 200, "Failed to GET object."
    assert response_get.json(), "Response JSON is empty or null."
    print("GET response:", response_get.json())


@pytest.mark.critical
def test_update_object(created_object):
    put_body = {
        "data": {
            "AP1": "111",
            "AP_12": "UPDATE_334",
            "AP_456": "9999",
            "size_AP": "UpdateTest"
        },
        "id": "420",
        "name": "Updated Object"
    }
    put_headers = {'Content-Type': 'application/json'}

    response_put = requests.put(
        f'http://167.172.172.115:52353/object/{created_object}',
        json=put_body,
        headers=put_headers
    ).json()

    print("PUT response:", response_put)
    assert response_put['name'] == "Updated Object", "Object name not updated."


@pytest.mark.medium
def test_patch_object(created_object):
    patch_body = {
        "data": {
            "AP": "111_p",
            "AP_12": "PATCH_334_p",
            "AP_PATCH": "4321",
            "size_AP": "PatchTest-p"
        },
    }
    patch_headers = {'Content-Type': 'application/json'}

    response_patch = requests.patch(
        f'http://167.172.172.115:52353/object/{created_object}',
        json=patch_body,
        headers=patch_headers
    ).json()

    assert "id" in response_patch, "Response does not contain 'id'"
    assert "data" in response_patch, "Response does not contain 'datas'"
    print("PATCH response:", response_patch)
