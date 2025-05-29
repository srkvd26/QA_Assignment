from pages.login import LoginPage
from pages.homepage import HomePage
from pages.dashboard import Dashboard

def test_TC_login_001(driver, username, password):
    try:
        homepage = HomePage(driver)
        login_page = LoginPage(driver)
        homepage.click_signin_button()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_signin_button()

        assert "Incorrect" in login_page.read_invalid_msg()
    
    except Exception as e:
        print("[Exception Occured] " + str(e))


def test_TC_login_004(driver):
    try:
        dashboard = Dashboard(driver)
        homepage = HomePage(driver)
        login_page = LoginPage(driver)

        homepage.click_signin_button()
        login_page.enter_username("srkvd26")
        login_page.enter_password("Vasu@265")
        login_page.click_signin_button()

        assert dashboard.find_avatar_element() is not None

    except Exception as e:
        print("[Exception Occured] " + str(e))