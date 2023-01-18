import pytest

from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData


class TestLogin(BaseTest):
    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_resend_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_reset_link_exist()
        assert flag

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        page = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert page.get_page_title(TestData.PAGE_TITLE) == TestData.PAGE_TITLE

    def test_unauthorized_login(self):
        self.loginPage = LoginPage(self.driver)
        page = self.loginPage.do_login(TestData.FAKE_USER, TestData.PASSWORD)
        assert page.get_page_title(TestData.LOGIN_PAGE_TITLE) == TestData.LOGIN_PAGE_TITLE





