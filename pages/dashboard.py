from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class Dashboard(CommonAction):
    avatar_icon = (By.XPATH, "//*[@class = 'avatar circle']")
    add_icon = (By.XPATH, "//*[@id= 'global-create-menu-anchor']/span")
    new_repo_option = (By.XPATH, "//*[contains(text(), 'New repository')]")
    
    def find_avatar_element(self):
        return self.wait_till_located(self.avatar_icon)
    
    def click_add_icon(self):
        self.wait_till_clickable(self.add_icon).click()

    def select_newrepository(self):
        self.wait_till_located(self.new_repo_option).click()