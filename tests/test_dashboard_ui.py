from tests.pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()


def test_login_and_logout(driver):

    logger.info("Starting Dashboard Test")

    login = LoginPage(driver)

    login.open()
    login.login("admin", "admin@2003K")

    logger.info("User Logged In Successfully")

    assert "logout" in driver.page_source.lower()

    logger.info("Dashboard Test Passed")