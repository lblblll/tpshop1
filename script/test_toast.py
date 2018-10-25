import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base import initDriver
from page.page import Page
import pytest

pytestmark = pytest.mark.skip("跳过")

class Testdemo:
    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_toast(self):
        self.page.inithomepage.auto_enter_home()
        time.sleep(3)
        self.driver.press_keycode(4)

        # ele = self.driver.find_element(By.XPATH,"//*[contains(@text,'再按一次退出')]")

        wait = WebDriverWait(self.driver,5,0.1)
        ele = wait.until(lambda x:x.find_element(By.XPATH,"//*[contains(@text,'再按一次退出')]"))
        print( ele.text )