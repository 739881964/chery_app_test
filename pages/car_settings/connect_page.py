# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：connect_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/18
# 当前系统时间：18:29
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element
from appium.webdriver.webelement import WebElement
from pages.btphone_page import BTPhonePage


class ConnectPage(BasePage):
    """
    '连接'功能页面
    """
    bt_button_locator = (By.ID, 'android:id/switch_widget')

    bt_button_elem = Element(locator=bt_button_locator, method='presence', desc='蓝牙开关按钮')
