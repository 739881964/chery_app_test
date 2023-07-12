# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：common_used_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/7/3
# 当前系统时间：16:19
# 用于创建文件的IDE的名称: PyCharm

from pages.base_page import Element, BasePage
from appium.webdriver.common.mobileby import MobileBy as By
from scripts.logger import logger


class CommonUsed(BasePage):
    """
    车辆设置-常用
    """
    menu_common_used_locator = (By.ID, 'com.mega.carsettings:id/menu_common_used')
    sw_right_child_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_right_child_lock')
    sw_left_child_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_left_child_lock')
    sw_central_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_central_lock')
    sw_window_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_window_lock')
    sw_epb_locator = (By.ID, 'com.mega.carsettings:id/sw_epb')
    sw_charge_port_locator = (By.ID, 'com.mega.carsettings:id/sw_charge_port')
    sw_rearview_mirror_locator = (By.ID, 'com.mega.carsettings:id/sw_rearview_mirror')
    # sw_right_child_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_right_child_lock')
    # sw_right_child_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_right_child_lock')
    # sw_right_child_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_right_child_lock')
    # sw_right_child_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_right_child_lock')
    # sw_right_child_lock_locator = (By.ID, 'com.mega.carsettings:id/sw_right_child_lock')

    menu_common_used_elem = Element(menu_common_used_locator, 'click', '常用按钮')
    sw_right_child_lock_elem = Element(sw_right_child_lock_locator, 'click', '右儿童锁')
    sw_left_child_lock_elem = Element(sw_left_child_lock_locator, 'click', '左儿童锁')
    sw_central_lock_elem = Element(sw_central_lock_locator, 'click', '中控锁')
    sw_window_lock_elem = Element(sw_window_lock_locator, 'click', '车窗锁')
    sw_epb_elem = Element(sw_epb_locator, 'click', 'EPB')
    sw_charge_port_elem = Element(sw_charge_port_locator, 'click', '充电接口锁')
    sw_rearview_mirror_elem = Element(sw_rearview_mirror_locator, 'click', '后视镜折叠锁')

    def select_lock(self, kind):
        """
        锁元素
        :param kind:
        :return:
        """
        return self.wait_click_element((By.ID, f'com.mega.carsettings:id/{kind}'))

    def gain_elem_property(self, elem, py_type='checked'):
        """
        获取元素属性
        :param elem:
        :param py_type:
        :return:
        """
        try:
            if self.select_lock(elem):
                return self.select_lock(elem).get_attribute(py_type)
        except Exception as e:
            logger.error(e)
            raise 'element {} is not exist'.format(elem)


if __name__ == '__main__':
    pass
