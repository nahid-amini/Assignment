from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestHome(BaseTest):

    def test_account_holder(self):
        self.loginPage = LoginPage(self.driver)
        self.home_page = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

        account_name = self.home_page.get_account_holder_value()
        assert account_name == TestData.ACCOUNT_HOLDER_NAME

    def test_account_type(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

        account_type = home_page.get_account_type()
        assert account_type == TestData.ACCOUNT_TYPE

    def test_subscription_renewal(self):
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

        subscription_renewal = home_page.get_subscription_renewal()
        assert subscription_renewal == TestData.SUBSCRIPTION_RENEWAL
