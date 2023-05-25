# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：sound_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/23
# 当前系统时间：19:04
# 用于创建文件的IDE的名称: PyCharm

from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage
from appium.webdriver.webelement import WebElement


class SoundPage(BasePage):
    """
    车辆设置-声音
    """

    menu_sound_locator = (By.ID, 'com.mega.carsettings:id/menu_sound')
    media_mute_locator = (By.ID, 'android:id/switch_widget')

    @property
    def media_mute_elem(self) -> WebElement:
        """
        媒体静音按钮
        :return:
        """
        return self.wait_click_element(self.media_mute_locator)

    @property
    def menu_sound_elem(self) -> WebElement:
        """
        声音按钮
        :return:
        """
        return self.wait_presence_element(self.menu_sound_locator)

    def scroll_to_mute(self):
        """
        滑动并点击车辆设置-声音
        :return:
        """
        self.swipe_up_and_down(329, 1080, 329, 380)
        self.menu_sound_elem.click()
