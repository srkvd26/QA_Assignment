from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class NewRepo(CommonAction):
    reponame_field = (By.XPATH, "//*[@id = ':r5:']")
    public_chkbx = (By.XPATH, "//*[@id = ':rf:']")
    private_chkbx = (By.XPATH, "//*[@id = ':rg:']")
    create_btn = (By.XPATH, "//*[contains(text(), 'Create repository')]")
    
    def enter_reponame(self, reponame):
        self.wait_till_located(self.reponame_field).send_keys(reponame)
    
    def click_public_chkbx(self):
        self.wait_till_clickable(self.public_chkbx).click()

    def click_private_chkbx(self):
        self.wait_till_located(self.private_chkbx).click()
        
    def scroll_to_create_and_click(self):
        element = self.wait_till_located(self.create_btn)
        self.scroll_till_visible(element)
        element.click()