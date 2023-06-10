# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：car_settings_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/4/27
# 当前系统时间：10:13
# 用于创建文件的IDE的名称: PyCharm


from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage
from appium.webdriver.webelement import WebElement


class CarSettingPage(BasePage):
    """
    车辆设置功能页面
    """

    show_button_locator = (By.ID, 'com.mega.carsettings:id/menu_display')
    screen_clear_locator = (By.XPATH, 'android.widget.RelativeLayout')
    clear_button_locator = (By.XPATH, 'android.widget.FrameLayout')
    scroll_view_locator = (By.ID, 'com.mega.carsettings:id/scroll_View')
    drive_locator = (By.ID, 'com.mega.carsettings:id/menu_drive')
    radio_group_locator = (By.ID, '	com.mega.carsettings:id/radio_group')
    menu_light_locator = (By.ID, 'com.mega.carsettings:id/menu_light')
    hud_locator = (By.ID, 'com.mega.carsettings:id/menu_hud')


if __name__ == '__main__':
    pass
