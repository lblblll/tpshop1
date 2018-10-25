import time

from selenium.webdriver.common.by import By

from base.baseaction import BaseAction


class HomePageAction(BaseAction):

    into_btn_feature = By.ID,"com.tpshop.malls:id/start_Button"
    home_btn_feature = By.XPATH,( "text,首页,1","resource-id,com.tpshop.malls:id/tab_txtv,1" )


    def auto_enter_home(self):

        time.sleep(3)
        # 实现左滑
        try:
            self.find_element(self.home_btn_feature)
            print("欢迎进入首页")

        except Exception:
            for i in range(3):
                self.swipe_left()
                time.sleep(0.6)

            self.click(self.into_btn_feature)