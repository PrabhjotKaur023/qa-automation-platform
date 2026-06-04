import pytest

from tests.pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("admin", "admin@2003K", "success"),
        ("admin", "wrongpassword", "failure"),
        ("wronguser", "admin@2003K", "failure"),
    ]
)
def test_login_data_driven(driver, env, username, password, expected):

    login = LoginPage(driver)

    login.open(env)

    login.login(username, password)

    if expected == "success":

        assert "site administration" in driver.page_source.lower()

    else:

        assert (
            "please enter the correct username and password"
            in driver.page_source.lower()
        )