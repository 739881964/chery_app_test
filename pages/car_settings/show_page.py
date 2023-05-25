# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：show_page.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/25
# 当前系统时间：15:06
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage
from appium.webdriver.webelement import WebElement


class ShowPage(BasePage):
    """
    车辆设置-显示功能页面
    """

    show_button_locator = (By.ID, 'com.mega.carsettings:id/menu_display')
    screen_clear_locator = (By.XPATH, '	//android.widget.TextView[@content-desc="清洁屏幕"]')
    theme_locator = (By.XPATH, '//android.widget.TextView[@content-desc="主题设置"]')

    @property
    def modify_theme_elem(self) -> WebElement:
        """
        设置主题
        :return:
        """
        return self.wait_click_element(self.theme_locator)

    @property
    def show_button_elem(self):
        return self.wait_click_element(self.show_button_locator)

    @property
    def screen_clear_elem(self):
        return self.wait_click_element(self.screen_clear_locator)

    def scroll_to_show(self):
        """
        滑动并点击车辆设置-显示位置
        :return:
        """
        self.swipe_up_and_down(323, 952, 323, 225)
        self.show_button_elem.click()

    def scroll_to_last(self):
        """
        滑动并点击车辆设置-显示位置
        :return:
        """
        self.swipe_up_and_down(1065, 737, 1065, 251)

    def clear_screen(self):
        """
        清洁屏幕操作
        :return:
        """
        self.scroll_to_show()
        self.scroll_to_last()
        self.screen_clear_elem.click()
        sleep(1)
        self.press(1270, 691)
