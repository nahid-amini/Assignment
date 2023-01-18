from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import time


class HomePage(BasePage):
    ACCOUNT_HOLDER = (By.XPATH, "(//div[@class='full-name display-large semibold midnight pt1 pb2 mb2'])[1]")
    ACCOUNT_TYPE = (By.XPATH, "//div[@class='body-text midnight']")
    SUBSCRIPTION_RENEWAL = (By.XPATH, "//div[@class='body-text midnight mb3']")

    def __init__(self, driver):
        super().__init__(driver)

    """this is used to get the page title"""
    def get_page_title(self, title):
        return self.get_title(title)

    def get_account_holder_value(self):
        return self.get_element_text(self.ACCOUNT_HOLDER)

    def get_account_type(self):
        return self.get_element_text(self.ACCOUNT_TYPE)

    def get_subscription_renewal(self):
        return self.get_element_text(self.SUBSCRIPTION_RENEWAL)



