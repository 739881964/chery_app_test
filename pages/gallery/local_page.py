# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：local_page.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/22
# 当前系统时间：17:40
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage
from appium.webdriver.webelement import WebElement


class LocalPage(BasePage):
    """
    图库-本地
    """
    local_locator = (By.XPATH, '//android.widget.LinearLayout[@content-desc="本地"]/android.widget.TextView')

    @property
    def local_elem(self) -> WebElement:
        """
        usb按钮
        :return:
        """
        return self.wait_click_element(self.local_locator)
