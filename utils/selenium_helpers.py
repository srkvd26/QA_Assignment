from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class CommonAction:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 30)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def update_wait_time(self, time):
        self._wait = WebDriverWait(self.driver, time)

    def wait_till_located(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def wait_till_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def wait_till_seen(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def wait_till_not_seen(self, locator):
        return self._wait.until_not(EC.visibility_of_element_located(locator))

    def click_enter_key(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()

    def scroll_till_visible(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text