# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：drive_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/30
# 当前系统时间：16:26
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element
from appium.webdriver.webelement import WebElement


class DrivePage(BasePage):
    """
    驾驶
    """
    # locators
    drive_locator = (By.ID, 'com.mega.carsettings:id/menu_drive')

    # elements
    drive_elem = Element(drive_locator, 'click', desc='驾驶模式选择')

    def drive_list_select_elem(self, value) -> WebElement:
        """
        不同的驾驶模式选择
        :param value:
        :return:
        """
        return self.wait_click_element((By.XPATH, f'//android.widget.RadioButton[contains(@content-desc, "{value}")]'))

    def select_drive_mode(self, value):
        """
        选择驾驶模式操作
        :return:
        """
        self.drive_elem.click()
        self.drive_list_select_elem(value).click()
