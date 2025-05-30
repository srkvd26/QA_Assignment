from selenium import webdriver
import pytest
import logging
import os
import time
from pages.login import LoginPage
from pages.homepage import HomePage

@pytest.fixture()
def driver():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://github.com/")
    yield driver
    driver.quit()


@pytest.fixture()
def login(request, driver):
    username, password = request.param
    homepage = HomePage(driver)
    login_page = LoginPage(driver)

    homepage.click_signin_button()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_signin_button()
    
    yield driver


def pytest_addoption(parser):
    parser.addini(
        "TC_signup_001",
        "Test data for TC_signup_001",
        type="linelist"
    )

    parser.addini(
        "TC_signin_001",
        "Test data for TC_signin_001",
        type="linelist"
    )


def pytest_generate_tests(metafunc):
    if metafunc.function.__name__ == "test_TC_signup_001":
        data = metafunc.config.getini("TC_signup_001")
        params = [tuple(line.split(",")) for line in data]
        metafunc.parametrize(("email", "username", "password", "message"), params)

    if metafunc.function.__name__ == "test_TC_login_001":
        data = metafunc.config.getini("TC_signin_001")
        params = [tuple(line.split(",")) for line in data]
        metafunc.parametrize(("username", "password"), params)


@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(f"./data/QA_Automation.log")
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger



@pytest.fixture
def screen_shots_list():
    return []

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.get_plugin("html")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    try:
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, "extra", [])

        if report.when in ("setup", "call"):
            xfail = hasattr(report, "wasxfail")
            if (report.skipped and xfail) or (report.failed and not xfail):

                # Attach multiple screenshots if available
                screen_shots = item.funcargs.get("screen_shots_list", [])
                for i, file_name in enumerate(screen_shots):
                    if file_name and os.path.exists(file_name):
                        html = f'<a href="{file_name}">Failure Screenshot {i+1}</a>'
                        extra.append(pytest_html.extras.html(html))

                # Final termination screenshot
                file_base = report.nodeid.split("/")[-1].replace("::", "_")
                timestamp = str(int(time.time()))
                file_name = os.path.join(os.getcwd(), "data", "test_result", f"{file_base}_{timestamp}.png")

                # Capture screenshot
                driver = item.funcargs.get("driver")
                if driver:
                    driver.save_screenshot(file_name)
                    html = f'<a href="{file_name}">Test case Termination Screenshot</a>'
                    extra.append(pytest_html.extras.html(html))

        report.extra = extra

    except Exception as e:
        print("Exception occurred in pytest_runtest_makereport Hook:", str(e))