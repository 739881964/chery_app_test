# coding:utf-8
# 当前的项目名：chery_app_test
# 当前编辑文件名：weather_page.py
# 当前用户的登录名：yuxiang
# 当前系统日期：2023/6/28
# 当前系统时间：13:39
# 用于创建文件的IDE的名称: PyCharm


from pages.base_page import Element, BasePage
from appium.webdriver.common.mobileby import MobileBy as By

from appium.webdriver.webelement import WebElement
from scripts.logger import logger


class WeatherPage(BasePage, Element):
    """
    天气App
    """
    # locator
    more_action_locator = (By.ID, 'com.lion.weather:id/more_action')
    lighting_warning_locator = (By.ID, 'com.lion.weather:id/alert_title')
    alert_play_locator = (By.ID, 'com.lion.weather:id/play')
    alert_close_locator = (By.ID, 'com.lion.weather:id/close')
    add_city_locator = (By.ID, 'com.lion.weather:id/add_city')
    search_input_locator = (By.ID, 'com.lion.weather:id/search_input')
    search_button_locator = (By.ID, 'com.lion.weather:id/search')
    home_city_name_locator = (By.ID, 'com.lion.weather:id/city_name')

    # element
    more_action_elem = Element(more_action_locator, 'click', '首页更多按钮')
    lighting_warning_elem = Element(lighting_warning_locator, 'presence', '预警弹窗')
    alert_play_elem = Element(alert_play_locator, 'click', '播报')
    alert_close_elem = Element(alert_close_locator, 'click', '关闭')
    add_city_elem = Element(add_city_locator, 'click', '添加城市按钮')
    search_input_elem = Element(search_input_locator, 'presence', '查找城市输入框')
    search_button_elem = Element(search_button_locator, 'click', '查找成功按钮')
    home_city_name_elem = Element(home_city_name_locator, 'presence', '主页城市名称')
    first_add_elem = Element(add_city_locator, 'click', '添加城市', is_elems=True, one_elem=True, index=0,
                             one_from_elems=True)

    @property
    def gain_city_name(self) -> str:
        """
        获取主页城市名称
        """
        return self.home_city_name_elem.text

    def search_city(self, city_name):
        """
        输入城市
        :return:
        """
        self.search_input_elem.send_keys(city_name)

    @property
    def add_city(self):
        """
        获取第一个查询后的城市列表
        :return:
        """
        return Element(self.add_city_locator, 'click', '添加城市', is_elems=True, one_elem=True, index=1,
                       one_from_elems=True)

    @property
    def gain_warning_attribute(self) -> bool:
        """
        获取预警bool值
        :return:
        """
        try:
            if '预警' in self.lighting_warning_elem.text:
                return True
        except Exception as e:
            logger.warning(e)
            return False
