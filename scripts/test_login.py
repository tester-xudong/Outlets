import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        self.page.homepage.click_me()
        self.page.registerpage.click_login()
        self.page.loginpage.input_username("itheima_test")
        self.page.loginpage.input_password("itheima")
        self.page.loginpage.click_login()
