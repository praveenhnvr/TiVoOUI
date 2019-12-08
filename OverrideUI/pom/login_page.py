from OverrideUI.root.selenium_driver import SeleniumDriver
import OverrideUI.utilities.custom_logger as cl
import logging
from OverrideUI.root.rootpage import BasePage
class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    # _login_link = "Login"
    _email_field = "txtUsername"
    _password_field = "txtPassword"
    _login_button = "btnLogin"
    # def clickLoginLink(self):
    #     self.elementClick(self._login_link, locatorType="link")
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
    def clickLoginButton(self):
        self.elementClick(self._login_button)
    def login(self, email="", password=""):
        # self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
    def verifyLoginSuccessfull(self):
        return self.isElementPresent("//a[@id='welcome']",locatorType="xpath")
    def welcome(self):
        c = self.isElementPresent("//a[@id='welcome']", locatorType="xpath")
        if c == True:
            self.elementClick("//a[@id='welcome']", locatorType="xpath")
            self.elementClick("//a[text()='Logout']",locatorType="xpath")
    def verifyLoginFailed(self):
        self.clearText(self._email_field)
        return self.isElementPresent("//span[text()='Invalid credentials']",locatorType="xpath")
    def verifyLoginTitle(self):
        return self.verifyPageTitle("opensource")
