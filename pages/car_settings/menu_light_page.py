# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：menu_light_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/10
# 当前系统时间：10:14
# 用于创建文件的IDE的名称: PyCharm


from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element

from appium.webdriver.webelement import WebElement


class MenuLightPage(BasePage):
    """
    外灯控制页面
    """
    # locators
    menu_light_locator = (By.ID, 'com.mega.carsettings:id/menu_light')

    # elements
    menu_light_elem = Element(locator=menu_light_locator, method='click', desc='外灯')

    def light_delay_elem(self, value):
        """
        大灯延时元素
        :param value:
        :return:
        """
        return self.wait_click_element((By.XPATH, f'//android.widget.RadioButton[@content-desc="{value}"]'))

    def set_light_delay(self, value):
        """
        设置大灯延时操作
        :param value:
        :return:
        """
        self.light_delay_elem(value).click()
        sleep(3)

    # @property
    def light_set_elem(self, value) -> WebElement:
        """
        大灯调节元素
        :return:
        """
        # f'//android.widget.RadioButton[@content-desc="{value}"]'
        return self.wait_click_element((By.XPATH, f'//android.widget.RadioButton[contains(@content-desc, "{value}")]'))

    def light_high_control(self, value):
        """
        大灯高度调节元素
        :param value:
        :return:
        """
        return self.wait_click_element((By.XPATH, f'//android.widget.TextView[@content-desc="{value}"]'))

    def set_light_high(self, value):
        """
        设置大灯高度调节操作
        :param value:
        :return:
        """
        # self.menu_light_elem.click()
        self.light_high_control(value).click()
        sleep(3)

    def set_light(self, value):
        """
        设置大灯调节操作
        :return:
        """
        # self.menu_light_elem.click()
        self.light_set_elem(value).click()
        sleep(3)


if __name__ == '__main__':
    pass
