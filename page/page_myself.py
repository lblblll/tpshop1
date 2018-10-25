from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.baseaction import BaseAction


class MyselfPageAction(BaseAction):

    login_reg_feature = By.XPATH,"text,登录/注册,1"
    num_input_feature = By.ID,"com.tpshop.malls:id/edit_phone_num"
    pwd_input_feature = By.ID,"com.tpshop.malls:id/edit_password"
    enter_btn_feature = By.ID,"com.tpshop.malls:id/btn_login"

    def click_login_reg(self):
        self.click(self.login_reg_feature)

    def input_num(self,value):
        self.input_txt(self.num_input_feature,value)

    def input_pwd(self,value):
        self.input_txt(self.pwd_input_feature,value)

    def click_enter(self):
        self.click(self.enter_btn_feature)

    def get_toast_content(self):
        wait = WebDriverWait(self.driver, 5, 0.1)
        ele = wait.until(lambda x: x.find_element(By.XPATH, "//*[contains(@text,'账号不存在!')]"))
        return ele.text