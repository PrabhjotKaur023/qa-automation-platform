from tests.pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()


def test_django_admin_login(driver):

    logger.info("Starting Login Test")

    login = LoginPage(driver)

    login.open()

    logger.info("Opened Admin Page")

    login.login("admin", "admin@2003K")

    logger.info("Login Attempt Completed")

    assert "logout" in driver.page_source.lower()

    logger.info("Login Test Passed")