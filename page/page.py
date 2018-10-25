from page.page_home import HomePageAction

class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def inithomepage(self):
        return HomePageAction(self.driver)