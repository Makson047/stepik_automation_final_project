from selenium import webdriver
# from selenium.common.exceptions import имя_исключения


class BasePage(object):
    def __init__(self, browser: webdriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except Exception as error:
            print(error)
            return False
        return True

    def open(self):
        self.browser.get(self.url)
