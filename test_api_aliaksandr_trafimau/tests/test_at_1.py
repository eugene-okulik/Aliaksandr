import pytest

TEST_DATA = [
    {
        "data": {
            "aat1": "1111",
            "aatt1": "33322",
            "color1": "blue",
            "size1": "small"
        },
        "id": "999",
        "name": "New Object"
    },
    {
        "data": {
            "aat2": "1",
            "aatt2": "3",
            "color2": "black",
            "size2": "big"
        },
        "id": "1000",
        "name": "New Object 1"
    }
]


@pytest.mark.medium
@pytest.mark.parametrize('data', TEST_DATA)
def test_add_object(create_post_endpoint, delete_post_endpoint, data):
    create_post_endpoint.new_post(payload=data)
    create_post_endpoint.check_status_code_is_correct()
    create_post_endpoint.check_response_contains_keys('id', 'data', 'name')
    object_id = create_post_endpoint.response.json().get('id')
    delete_post_endpoint.delete_post(object_id=object_id)
    delete_post_endpoint.check_status_code_is_correct()


@pytest.mark.critical
@pytest.mark.parametrize('data', [TEST_DATA[0]])
def test_update_object(create_post_endpoint, update_post_endpoint, delete_post_endpoint, data):
    create_post_endpoint.new_post(payload=data)

    object_id = create_post_endpoint.response.json().get('id')

    payload_for_update = {
        "data": {
            "aat3": "0",
            "aatt5": "100",
            "color7": "blackkkk",
            "size5": "bigggg"
        },
        "id": "10000",
        "name": "New Object 7777"
    }

    update_post_endpoint.update_object(object_id=object_id, payload=payload_for_update)
    update_post_endpoint.check_status_code_is_correct()
    delete_post_endpoint.delete_post(object_id=object_id)
    delete_post_endpoint.check_status_code_is_correct()


@pytest.mark.critical
@pytest.mark.parametrize('data', [TEST_DATA[0]])
def test_patch_object(create_post_endpoint, delete_post_endpoint, data, patch_post_endpoint):
    create_post_endpoint.new_post(payload=data)

    object_id = create_post_endpoint.response.json().get('id')
    assert object_id, "Object ID is missing after POST request!"
    payload_for_patch = {
        "data": {
            "aat3": "0",
            "aatt5": "100",
            "color7": "blackkkk",
            "size5": "bigggg"
        },

    }

    patch_post_endpoint.patch_object(object_id=object_id, payload=payload_for_patch)
    patch_post_endpoint.check_status_code_is_correct()
    patch_post_endpoint.check_id_in_response()
    patch_post_endpoint.check_data_in_response()
    patch_post_endpoint.check_response_integrity()
    delete_post_endpoint.delete_post(object_id=object_id)
    delete_post_endpoint.check_status_code_is_correct()


@pytest.mark.critical
@pytest.mark.parametrize('data', [TEST_DATA[0]])
def test_delete_object(create_post_endpoint, delete_post_endpoint, data):
    create_post_endpoint.new_post(payload=data)
    object_id = create_post_endpoint.response.json().get('id')
    delete_post_endpoint.delete_post(object_id=object_id)
    delete_post_endpoint.check_status_code_is_correct()
