import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PatchObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture
def create_object(create_object_endpoint, delete_object_endpoint):
    def _create(data):
        create_object_endpoint.new_post(payload=data)
        object_id = create_object_endpoint.response.json().get('id')
        yield object_id
        delete_object_endpoint.delete_object(object_id=object_id)
        delete_object_endpoint.check_status_code_is_correct()

    return _create
