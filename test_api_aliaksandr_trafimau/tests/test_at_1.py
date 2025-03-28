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
def test_add_object(create_object_endpoint, create_object, data):
    next(create_object(data))
    create_object_endpoint.check_status_code_is_correct()
    create_object_endpoint.check_response_contains_keys('id', 'data', 'name')


@pytest.mark.critical
@pytest.mark.parametrize('data', [TEST_DATA[0]])
def test_update_object(update_object_endpoint, create_object, data):
    object_id = next(create_object(data))
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
    update_object_endpoint.update_object(object_id=object_id, payload=payload_for_update)
    update_object_endpoint.check_status_code_is_correct()


@pytest.mark.critical
@pytest.mark.parametrize('data', [TEST_DATA[0]])
def test_patch_object(patch_object_endpoint, create_object, data):
    object_id = next(create_object(data))
    payload_for_patch = {
        "data": {
            "aat3": "0",
            "aatt5": "100",
            "color7": "blackkkk",
            "size5": "bigggg"
        },
    }
    patch_object_endpoint.patch_object(object_id=object_id, payload=payload_for_patch)
    patch_object_endpoint.check_status_code_is_correct()
    patch_object_endpoint.check_id_in_response()
    patch_object_endpoint.check_data_in_response()
    patch_object_endpoint.check_response_integrity()


@pytest.mark.critical
@pytest.mark.parametrize('data', [TEST_DATA[0]])
def test_delete_object(delete_object_endpoint, create_object, data):
    object_id = next(create_object(data))
    delete_object_endpoint.delete_object(object_id=object_id)
    delete_object_endpoint.check_status_code_is_correct()
