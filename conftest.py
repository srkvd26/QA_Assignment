from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://github.com/")
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addini(
        "TC_signup_001",
        "Test data for TC_singup_001",
        type="linelist"
    )

def pytest_generate_tests(metafunc):
    if metafunc.function.__name__ == "test_TC_signup_001":
        data = metafunc.config.getini("TC_signup_001")
        params = [tuple(line.split(",")) for line in data]
        metafunc.parametrize(("email", "username", "password", "message"), params)