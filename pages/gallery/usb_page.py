# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：usb_page.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/22
# 当前系统时间：17:34
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element
from appium.webdriver.webelement import WebElement


class UsbPage(BasePage):
    """
    图库-usb
    """
    # locators
    usb_locator = (By.XPATH, '//android.widget.LinearLayout[@content-desc="USB"]/android.widget.TextView')

    # elements
    usb_elem = Element(usb_locator, method='click', desc='usb按钮')
