import pytest
from dataProvider.login_data import login_data
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

@pytest.mark.login
@pytest.mark.parametrize("username, password, expected_error", login_data)
def test_login(login_fixture, username, password, expected_error):
    logger.info(f"Attempting to login with username: {username}")
    login_fixture.login(username, password)

    if expected_error:
        error_message = login_fixture.get_error_message()
        logger.info(f"Expected error: {expected_error}, Got error: {error_message}")

        assert error_message == expected_error, f"Expected: {expected_error}, Got: {error_message}"
    else:
        logger.info(f"Login successful for username: {username}")
