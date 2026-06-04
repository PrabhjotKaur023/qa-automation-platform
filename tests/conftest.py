import pytest
import os
from utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# Store test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


# Screenshot on failure
@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield

    if request.node.rep_call.failed:

        screenshots_dir = "reports/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        file_name = f"{request.node.name}.png"
        file_path = os.path.join(screenshots_dir, file_name)

        driver.save_screenshot(file_path)

        print(f"\nScreenshot saved: {file_path}")