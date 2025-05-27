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
        "credentials",
        "List of user credentials",
        type="linelist"
    )

def pytest_generate_tests(metafunc):
    if metafunc.function.__name__ == "test_signup":
        data = metafunc.config.getini("credentials")
        params = [tuple(line.split(",")) for line in data]
        metafunc.parametrize(("email", "password", "username"), params)