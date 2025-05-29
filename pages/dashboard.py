from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class Dashboard(CommonAction):
    avatar_icon = (By.XPATH, "//*[@class = 'avatar circle']")
    

    def find_avatar_element(self):
        return self.wait_till_located(self.avatar_icon)