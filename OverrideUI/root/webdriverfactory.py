from selenium import webdriver
class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        if self.browser == 'firefox':
            driver = webdriver.Firefox(
                executable_path="C:\\PythonWorkspace\\Drivers\\geckodriver")

        else:
            driver = webdriver.Chrome(
                executable_path="C:\\PythonWorkspace\\Drivers\\chromedriver")

        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)
        return driver
