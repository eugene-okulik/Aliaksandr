import pytest


@pytest.fixture()
def add_ending_text():
    yield
    print("=== This is the end of the test case ===")