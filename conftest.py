from selenium import webdriver
import pytest
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