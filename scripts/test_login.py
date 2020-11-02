import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        self.page.homepage.click_me()
        self.page.registerpage.click_login()
        self.page.loginpage.input_username(username)
        self.page.loginpage.input_password(password)
        self.page.loginpage.click_login()

        if toast is None:
            assert self.page.mepage.get_nick_name_text() == username
        else:
            # 找toast提示，找args中的toast提示是否能找到，如果能则通过，如果不能则不通过
            assert self.page.loginpage.is_toast_exist(toast)
