import pytest
from endpoints.create_post import CreatePost
from endpoints.delete_object import DeletePost
from endpoints.update_object import UpdateObject
from endpoints.patch_object import PatchObject


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_post_endpoint():
    return PatchObject()
