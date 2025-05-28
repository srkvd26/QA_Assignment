from pages.signup import SignupForm
from pages.homepage import HomePage


def test_signup(driver, email, username, password, message):
    try:
        homepage = HomePage(driver)
        homepage.click_signup_button()
        signup_page = SignupForm(driver)
        signup_page.enter_email(email)
        signup_page.enter_password(password)
        signup_page.enter_username(username)
        signup_page.click_continue_button()
        assert message in signup_page.read_blank_email_msg() or signup_page.read_blank_pwd_msg() or signup_page.read_blank_usrname_msg()
    
    except Exception as e:
        print("[Exception Occured] " + str(e))