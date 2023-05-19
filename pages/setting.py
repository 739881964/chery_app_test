# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：setting.py
# 当前用户的登录名：yuxiang
# 当前编辑文件名：setting
# 当前系统日期：2023/4/26
# 当前系统时间：14:43
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from pages.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.webelement import WebElement


class SettingPage(BasePage):
    """
    设置功能页面的相关属性及操作
    """
    show_button_locator = (By.ID, 'android:id/title')
    auto_control_light_locator = (By.ID, 'android:id/switch_widget')

    def switch_auto(self):
        self.show_button_elem.click()
        self.auto_control_light_elem.click()
        sleep(3)

    @property
    def show_button_elem(self) -> WebElement:
        """获取显示按钮"""
        return self.wait_click_element(self.show_button_locator)

    @property
    def auto_control_light_elem(self) -> WebElement:
        return self.wait_click_element(self.auto_control_light_locator)


if __name__ == '__main__':
    pass
