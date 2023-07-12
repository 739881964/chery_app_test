# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：wifi_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/27
# 当前系统时间：15:01
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element
from appium.webdriver.webelement import WebElement
from scripts.logger import logger


class WiFiPage(BasePage, Element):
    """
    wifi开关
    """
    # locator
    wifi_switch_widget_locator = (By.ID, 'android:id/switch_widget')
    wifi_arrow_locator = (By.ID, 'com.mega.carsettings:id/iv_arrow')
    wifi_delete_locator = (By.ID, 'com.mega.carsettings:id/iv_action_delete')
    connect_sure_locator = (By.ID, 'com.mega.carsettings:id/tv_sure')
    connect_cancel_locator = (By.ID, 'com.mega.carsettings:id/tv_cancel')
    connect_already_locator = (By.ID, 'com.mega.carsettings:id/tv_connect_state')
    password_input_locator = (By.ID, 'com.mega.carsettings:id/et_password_content')

    # element
    wifi_switch_widget_elem = Element(wifi_switch_widget_locator, 'click', 'WIFI开关')
    wifi_arrow_elem = Element(wifi_arrow_locator, 'click', '进去wifi连接按钮', is_elems=True, one_elem=True,
                              index=1, one_from_elems=True)
    wifi_delete_elem = Element(wifi_delete_locator, 'click', 'wifi删除按钮')
    connect_sure_elem = Element(connect_sure_locator, 'click', '确认连接/断开按钮')
    disconnect_sure_elem = Element(connect_sure_locator, 'click', '断开连接按钮')
    connect_cancel_elem = Element(connect_cancel_locator, 'click', '取消连接按钮')
    connect_already_elem = Element(connect_already_locator, 'presence', '已连接提示')
    password_input_elem = Element(password_input_locator, 'presence', '密码输入框')

    def connect_wifi_step(self, name, passwd):
        """
        连接wifi操作步骤
        :return:
        """
        self.wifi_arrow_elem.click()
        sleep(2)
        self.wifi_name(name).click()
        self.send_password(passwd)
        self.connect_sure_elem.click()

    def send_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        return self.password_input_elem.send_keys(password)

    def tap_wifi_screen(self):
        """
        点击屏幕空白处，关闭wifi连接弹出框
        :return:
        """
        self.tap_screen(2200, 400)

    @property
    def connect_exist(self) -> bool:
        """
        是否连接
        :return:
        """
        try:
            if self.connect_already_elem:
                return True
        except Exception as e:
            logger.warning(e)
            return False

    @property
    def wifi_button_property(self) -> bool:
        """
        wifi开关属性
        :return:
        """
        if self.wifi_switch_widget_elem.get_attribute('checked') == 'true':
            return True
        return False

    def wifi_name(self, name):
        """
        选择要链接的wifi名称
        :param name:
        :return:
        """
        return self.wait_click_element((By.XPATH, f'//android.widget.TextView[contains(@text, "{name}")]'))
