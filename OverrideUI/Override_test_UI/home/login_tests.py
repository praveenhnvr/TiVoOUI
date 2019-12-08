import time

from OverrideUI.utilities.teststatus import TestStatus
from OverrideUI.pom.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("Admin", "admin123")
        result1 = self.lp.verifyLoginTitle()
        # Here it wont assert any thing because because it is not last
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessfull()
        time.sleep(5)
        self.lp.welcome()
        time.sleep(5)
        self.ts.markFinal("test_vaildLogin", result2, "login was not successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("Admin", "admin")
        result = self.lp.verifyLoginFailed()
        assert result == True