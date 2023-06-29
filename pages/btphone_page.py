# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：btphone_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/5/18
# 当前系统时间：18:01
# 用于创建文件的IDE的名称: PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage, Element
from appium.webdriver.webelement import WebElement
from scripts.logger import logger


class BTPhonePage(BasePage):
    """
    蓝牙电话
    """
    # locators
    conn_bt_locator = (By.ID, 'com.mega.btphone:id/go_setting_in_disconnect')
    edit_bt_name_locator = (By.XPATH, '//android.widget.TextView[@content-desc="蓝牙名称"]')
    bt_name_input_locator = (By.ID, 'com.mega.carsettings:id/et_content')
    save_locator = (By.ID, 'com.mega.carsettings:id/tv_sure')
    bt_name_locator = (By.ID, 'android:id/summary')
    cancel_locator = (By.ID, 'com.mega.carsettings:id/tv_cancel')
    connect_failed_locator = (By.ID, 'com.mega.carsettings:id/tv_title')
    know_locator = (By.ID, 'com.mega.carsettings:id/tv_sure')
    disconnect_locator = (By.ID, 'com.mega.carsettings:id/tv_connect_state')
    iv_arrow_locator = (By.ID, 'com.mega.carsettings:id/iv_arrow')
    device_id_locator = (By.ID, 'android:id/title')

    # elements
    disconnect_elem = Element(locator=disconnect_locator, method='click', desc='未连接设备')
    know_elem = Element(locator=know_locator, method='presence', desc="'知道了' alert")
    connect_failed_elem = Element(locator=connect_failed_locator, method='visibility', desc='配对失败alert')
    cancel_elem = Element(locator=cancel_locator, method='click', desc='取消按钮')
    conn_bt_elem = Element(locator=conn_bt_locator, method='click', desc='获取连接蓝牙按钮')
    edit_bt_name_elem = Element(locator=edit_bt_name_locator, method='click', desc='编辑蓝牙名称按钮')
    bt_name_input_elem = Element(locator=bt_name_input_locator, method='presence', desc='编辑蓝牙名称输入框')
    save_elem = Element(locator=save_locator, method='click', desc='保存按钮')
    bt_name_elem = Element(locator=bt_name_locator, method='presence', desc='蓝牙名称')
    iv_arrow_elem = Element(locator=iv_arrow_locator, method='click', desc='连接设备历史')
    device_id_elem = Element(locator=device_id_locator, method='click', desc='连接设备id', is_elems=True, one_elem=True,
                             one_from_elems=True, index=-1)

    def tap_bt_screen(self):
        """
        点击屏幕空白处，关闭蓝牙配对历史弹出框
        :return:
        """
        self.tap_screen(2200, 400)

    def new_bt_name(self, new_name):
        """
        编辑蓝牙name并保存操作
        :return:
        """
        self.edit_bt_name_elem.click()
        e = self.bt_name_input_elem
        logger.info(e)
        e.send_keys(new_name)
        # 收起键盘
        self.hide_keyboard()
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


if __name__ == '__main__':
    pass
