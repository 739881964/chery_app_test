# coding:utf-8
# 当前的项目名：chery_app_test-main
# 当前编辑文件名：show_page.py
# 当前用户的登录名：73988
# 当前系统日期：2023/5/25
# 当前系统时间：15:06
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element
from appium.webdriver.webelement import WebElement
from scripts.logger import logger


class ShowPage(BasePage):
    """
    车辆设置-显示功能页面
    """

    show_button_locator = (By.ID, 'com.mega.carsettings:id/menu_display')
    screen_clear_locator = (By.XPATH, '	//android.widget.TextView[@content-desc="清洁屏幕"]')
    theme_locator = (By.XPATH, '//android.widget.TextView[@content-desc="主题设置"]')
    return_button_locator = (By.ID, 'com.mega.carsettings:id/iv_close')
    video_limiter_locator = (By.ID, 'android:id/switch_widget')
    control_bright_locator = (By.ID, 'com.mega.carsettings:id/seekbar')

    # elements
    control_elem = Element(control_bright_locator[1], method='presence', desc='中控滑动条', is_elems=True, index=1)
    video_limiter_elem = Element(locator=video_limiter_locator, method='click', desc='视频限制开关')
    screen_clear_elem = Element(locator=screen_clear_locator, method='click', desc='清洁屏幕按钮')
    show_button_elem = Element(locator=show_button_locator, method='click', desc='显示功能按钮')
    modify_theme_elem = Element(locator=theme_locator, method='click', desc='主题选择功能按钮')
    return_elem = Element(locator=return_button_locator, method='click', desc='返回显示页面按钮')

    @property
    def get_value(self):
        """
        获取中控亮度条的初始位置x, y
        :return:
        """
        return self.get_location(self.control_elem)

    def swipe_control(self):
        """
        滑动控制条
        :return:
        """
        x = self.generate_random()
        self.swipe_up_and_down(758, 695, x, 695)
        logger.info('向x轴滑动距离{}, 调节屏幕亮度成功'.format(x))

    def show_mode_select_elem(self, mode) -> WebElement:
        """
        选择显示模式
        :param mode:
        :return:
        """
        return self.wait_click_element((By.XPATH, f'//android.widget.RadioButton[@content-desc="{mode}"]'))

    # @property
    def choose_theme(self, value) -> WebElement:
        """
        选择不同的主题风格
        :return:
        """
        return self.wait_click_element((By.ID, f'com.mega.carsettings:id/{value}'))

    def scroll_to_show(self):
        """
        滑动并点击车辆设置-显示位置
        :return:
        """
        self.swipe_up_and_down(323, 952, 323, 225)
        self.show_button_elem.click()

    def scroll_to_last(self):
        """
        滑动车辆设置-显示 到最下方
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
