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


def capture_screen_shot(name):
    driver.get_screenshot_as_file(name)


# This hook is capture the screenshot upon failure and add the screenshot to the respective TC in report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    try:
        # Instantiate the pytest plugin manager for html
        pytest_html = item.config.pluginmanager.get_plugin("html")
        outcome = yield
        # get the current test case result
        report = outcome.get_result()
        extra = getattr(report, "extra", [])
        # At Setup phase or when framework calls it to update report we need to capture screenshot only on failure
        if report.when == "call" or report.when == "setup":
            xfail = hasattr(report, "wasxfail")
            if (report.skipped and xfail) or (report.failed and not xfail):
                # get all screenshots from current test case
                screen_shots = item.funcargs["screen_shots_list"]
                for i, file_name in enumerate(screen_shots):
                    # If file exist, then add the extra hyperlink that can show the screen shot captured
                    if file_name:
                        html = f'<a href="{file_name}">Failure Screenshot {i+1}</a>'
                        extra.append(pytest_html.extras.html(html))
                # Upon failure, capture the last screen where it is terminated
                file_name_with_out_path = report.nodeid.split("/")[-1]
                file = (
                    file_name_with_out_path.replace("::", "_")
                    + str(int(time.time()))
                    + ".png"
                )
                # Define the custom path where to store the screen shots
                file_name = os.path.join(os.getcwd(), "data", "test_result", file)
                capture_screen_shot(file_name)
                if file_name:
                    html = f'<a href="{file}">Test case Termination Screenshot</a>'
                    extra.append(pytest_html.extras.html(html))
            report.extras = extra
    except Exception as e:
        print("Exception occured in Pytest makereport Hook")