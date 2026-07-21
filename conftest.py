import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is not None:
            screenshot_name = f"{item.name}_failure.png"
            driver.save_screenshot(screenshot_name)