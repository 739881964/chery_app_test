# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：car_settings_page.py
# 当前用户的登录名：yuxiang
# 当前编辑文件名：car_settings
# 当前系统日期：2023/4/27
# 当前系统时间：10:13
# 用于创建文件的IDE的名称: PyCharm


from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage


class CarSettingPage(BasePage):
    """
    车辆设置功能页面
    """
    show_button_locator = (By.ID, 'com.mega.carsettings:id/menu_display')
    screen_clear_locator = (By.XPATH, 'android.widget.RelativeLayout')
    clear_button_locator = (By.XPATH, 'android.widget.FrameLayout')
    scroll_view_locator = (By.ID, 'com.mega.carsettings:id/scroll_View')
    drive_locator = (By.ID, 'com.mega.carsettings:id/menu_drive')

    @property
    def drive_elem(self):
        return self.wait_click_element(self.drive_locator)

    @property
    def scroll_view_elem(self):
        return self.wait_presence_element(self.scroll_view_locator)

    @property
    def show_button_elem(self):
        return self.wait_click_element(self.show_button_locator)

    @property
    def screen_clear_elem(self):
        return self.wait_click_element(self.screen_clear_locator)

    @property
    def clear_button_elem(self):
        return self.wait_click_element(self.clear_button_locator)

    def select_drive(self):
        """
        选择驾驶模式
        :return:
        """
        self.drive_elem.click()

    def clear_screen(self):
        """
        清洁屏幕操作
        :return:
        """
        # 屏幕滑倒底部
        self.switch_frame(locator=self.scroll_view_locator)
        self.execute_js(js=True)
        # self.swipe_down()
        self.show_button_elem.click()
        self.screen_clear_elem.click()
        self.long_press(self.clear_button_locator)


if __name__ == '__main__':
    pass
