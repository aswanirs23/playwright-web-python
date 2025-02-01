import pytest
from dataProvider.login_data import login_data

@pytest.mark.parametrize("username, password, expected_error", login_data)
def test_login(login_fixture, username, password, expected_error):
    login_fixture.login(username, password)

    if expected_error:
        error_message = login_fixture.get_error_message()
        assert error_message == expected_error, f"Expected: {expected_error}, Got: {error_message}"
    else:
        print("Login successful")
