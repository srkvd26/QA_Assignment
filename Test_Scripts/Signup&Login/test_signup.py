from utils import selenium_helpers
from pages.signup import SignupForm
from pages.homepage import HomePage
import time


def test_signup(driver, email, password, username):
    try:
        homepage = HomePage(driver)
        homepage.click_signup_button()
        signup_page = SignupForm(driver)
        signup_page.enter_email(email)
        signup_page.enter_password(password)
        signup_page.enter_username(username)
        time.sleep(5)

    except Exception as e:
        print("[Exception Occured] " + str(e))