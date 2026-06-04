from tests.pages.login_page import LoginPage


def test_login_and_logout(driver):
    login = LoginPage(driver)

    login.open()
    login.login("admin", "admin@2003K")

    assert "logout" in driver.page_source.lower()