from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class HomePage(CommonAction):
    signup_btn = (By.LINK_TEXT, "Sign up")
    signin_btn = (By.LINK_TEXT, "Sign in")


    def click_signup_button(self):
        self.wait_till_clickable(self.signup_btn).click()

    def click_signin_button(self):
        self.wait_till_clickable(self.signin_btn).click()
