from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class LoginPage(CommonAction):
    username_field = (By.XPATH, "//*[@id = 'login_field']")
    password_field = (By.XPATH, "//*[@id = 'password']")
    signin_btn = (By.XPATH, "//*[@value = 'Sign in']")   
    invalid_msg = (By.XPATH, "//*[contains(text(), 'Incorrect')]")

    def enter_username(self, username):
        self.wait_till_located(self.username_field).send_keys(username)

    def enter_password(self, password):
        self.wait_till_located(self.password_field).send_keys(password)

    def click_signin_button(self):
        self.wait_till_clickable(self.signin_btn).click()

    def read_invalid_msg(self):
        return self.get_text(self.invalid_msg)
    
    def element_found(self):
        return self.wait_till_seen(By.XPATH, "//*[@class = 'avatar circle']")