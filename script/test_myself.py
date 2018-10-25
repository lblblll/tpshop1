import time

from base import initDriver
from page.page import Page


class TestDemo:

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_login_nonum(self):

        self.page.inithomepage.auto_enter_home()
        self.page.inithomepage.click_myself()
        time.sleep(2)

        self.page.initmyselfpage.click_login_reg()
        time.sleep(2)

        self.page.initmyselfpage.input_num("13601360136")
        self.page.initmyselfpage.input_pwd("123456")
        self.page.initmyselfpage.click_enter()

        toast_text = self.page.initmyselfpage.get_toast_content()
        assert toast_text == "账号不存在!"
