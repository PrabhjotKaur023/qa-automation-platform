from tests.pages.login_page import LoginPage
from utils.data_reader import get_login_data
from utils.logger import get_logger

logger = get_logger()


def test_django_admin_login(driver, env):

    data = get_login_data()

    logger.info("Starting Login Test")

    login = LoginPage(driver)

    login.open(env)

    login.login(
        data["username"],
        data["password"]
    )

    assert "logout" in driver.page_source.lower()

    logger.info("Login Test Passed")