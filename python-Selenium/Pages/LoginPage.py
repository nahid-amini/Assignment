from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Config.config import TestData


class LoginPage(BasePage):
    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.ID, "loginFormSubmit")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    RESEND_LINK = (By.LINK_TEXT, "Resend link")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page Actions"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """this is used to check Resend link"""
    def is_reset_link_exist(self):
        return self.is_visible(self.RESEND_LINK)

    """this is used to login"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)






