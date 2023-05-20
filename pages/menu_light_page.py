# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：menu_light_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/10
# 当前系统时间：10:14
# 用于创建文件的IDE的名称: PyCharm


from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

from appium.webdriver.webelement import WebElement


class MenuLightPage(BasePage):
    """
    外灯控制页面
    """
    # value = None
    menu_light_locator = (By.ID, 'com.mega.carsettings:id/menu_light')
    # light_set_locator = (By.XPATH, '//android.widget.RadioButton[contains(@content-desc, "自动")]')

    @property
    def menu_light_elem(self) -> WebElement:
        """
        外灯
        :return:
        """
        return self.wait_click_element(self.menu_light_locator)

    # @property
    def light_set_elem(self, value) -> WebElement:
        """
        大灯调节
        :return:
        """
        # f'//android.widget.RadioButton[@content-desc="{value}"]'
        return self.wait_click_element((By.XPATH, f'//android.widget.RadioButton[contains(@content-desc, "{value}")]'))

    def set_light(self, value):
        """
        设置大灯模式
        :return:
        """
        self.menu_light_elem.click()
        self.light_set_elem(value).click()
        sleep(4)


if __name__ == '__main__':
    pass
