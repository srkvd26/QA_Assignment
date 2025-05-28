from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class SignupForm(CommonAction):
    email_field = (By.XPATH, "//*[@id = 'email']")
    password_field = (By.XPATH, "//*[@id = 'password']")
    username_field = (By.XPATH, "//*[@placeholder = 'Username']")
    continue_btn = (By.XPATH, "//*[contains(text(), 'Continue')]")
    blank_email_msg = (By.XPATH, "//*[@class = 'mb-0 nux-error' and contains(text(), 'Email cannot be blank')]")
    blank_password_msg = (By.XPATH, "//*[@class = 'mb-0 nux-error' and contains(text(), 'Password cannot be blank')]")
    blank_username_msg = (By.XPATH, "//*[@class = 'mb-0 nux-error' and contains(text(), 'Username cannot be blank')]")


    def enter_email(self, email):
        self.wait_till_located(self.email_field).send_keys(email)

    def enter_password(self, password):
        self.wait_till_located(self.password_field).send_keys(password)
    
    def enter_username(self, username):
        self.wait_till_located(self.username_field).send_keys(username)

    def click_continue_button(self):
        self.wait_till_clickable(self.continue_btn).click()

    def read_blank_usrname_msg(self):
        return self.wait_till_located(self.blank_username_msg).text
    
    def read_blank_pwd_msg(self):
        return self.wait_till_located(self.blank_password_msg).text
    
    def read_blank_email_msg(self):
        return self.wait_till_located(self.blank_email_msg).text
