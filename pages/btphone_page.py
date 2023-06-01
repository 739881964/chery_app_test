# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：btphone_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/18
# 当前系统时间：18:01
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage
from appium.webdriver.webelement import WebElement
from scripts.logger import logger


class BTPhonePage(BasePage):
    """
    蓝牙电话
    """
    conn_bt_locator = (By.ID, 'com.mega.btphone:id/go_setting_in_disconnect')
    edit_bt_name_locator = (By.XPATH, '//android.widget.TextView[@content-desc="蓝牙名称"]')
    bt_name_input_locator = (By.ID, 'com.mega.carsettings:id/et_content')
    save_locator = (By.ID, 'com.mega.carsettings:id/tv_sure')
    bt_name_locator = (By.ID, 'android:id/summary')
    back_locator = (By.ID, 'com.mega.carsettings:id/iv_back')
    connect_failed_locator = (By.ID, 'com.mega.carsettings:id/tv_title')
    know_locator = (By.ID, 'com.mega.carsettings:id/tv_sure')
    disconnect_locator = (By.ID, 'com.mega.carsettings:id/tv_connect_state')

    @property
    def disconnect_elem(self) -> WebElement:
        """
        未连接设备
        :return:
        """
        return self.wait_presence_element(self.disconnect_locator)

    @property
    def know_elem(self) -> WebElement:
        """
        '知道了' alert
        :return:
        """
        return self.wait_presence_element(self.know_locator)

    @property
    def connect_failed_elem(self) -> WebElement:
        """
        配对失败alert
        :return:
        """
        return self.wait_presence_element(self.connect_failed_locator)

    @property
    def back_elem(self) -> WebElement:
        """
        返回按钮
        :return:
        """
        return self.wait_click_element(self.back_locator)

    @property
    def conn_bt_elem(self) -> WebElement:
        """
        获取连接蓝牙按钮
        :return:
        """
        return self.wait_click_element(self.conn_bt_locator)

    @property
    def edit_bt_name_elem(self) -> WebElement:
        """
        编辑蓝牙名称按钮
        :return:
        """
        return self.wait_click_element(self.edit_bt_name_locator)

    @property
    def bt_name_input_elem(self) -> WebElement:
        """
        编辑蓝牙名称输入框
        :return:
        """
        return self.wait_presence_element(self.bt_name_input_locator)

    @property
    def save_elem(self) -> WebElement:
        """
        保存按钮
        :return:
        """
        return self.wait_click_element(self.save_locator)

    def new_bt_name(self, new_name):
        """
        编辑蓝牙name并保存操作
        :return:
        """
        self.edit_bt_name_elem.click()
        e = self.bt_name_input_elem
        logger.info(e)
        e.send_keys(new_name)
        self.save_elem.click()

    def input_name(self, name):
        """
        编辑蓝牙名称不保存
        :return:
        """
        self.edit_bt_name_elem.click()
        e = self.bt_name_input_elem
        logger.info(e)
        e.send_keys(name)

    @property
    def bt_name_elem(self) -> WebElement:
        """
        蓝牙名称
        :return:
        """
        return self.wait_presence_element(self.bt_name_locator)


if __name__ == '__main__':
    pass
