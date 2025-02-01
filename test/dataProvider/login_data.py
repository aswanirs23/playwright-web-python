import pytest

login_data = [
    pytest.param(
        "invalid_user",
        "invalid_password",
        "Epic sadface: Username and password do not match any user in this service",
        id="login with invalid username and password"
    ),
    pytest.param(
        "invalid_user",
        "secret_sauce",
        "Epic sadface: Username and password do not match any user in this service",
        id="login with invalid username and valid password"
    ),
    pytest.param(
        "standard_user",
        "invalid_password",
        "Epic sadface: Username and password do not match any user in this service",
        id="login with valid username and invalid password"
    ),
    pytest.param(
        "", 
        "secret_sauce", 
        "Epic sadface: Username is required",
        id="login with no username"
    ),
    pytest.param(
        "standard_user", 
        "", 
        "Epic sadface: Password is required",
        id="login with no password"
    ),
    pytest.param(
        "", 
        "", 
        "Epic sadface: Username is required",
        id="login with no username and no password"
    ),
    pytest.param(
        "standard_user", 
        "secret_sauce", 
        None, 
        id="login with valid credentials"
    )
]
